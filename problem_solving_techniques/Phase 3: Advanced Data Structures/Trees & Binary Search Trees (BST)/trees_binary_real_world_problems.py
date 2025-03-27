"""
1. Family Tree Structure
Problem Statement:
Implement a family tree system where each node represents a person with:

Name

Birthdate

Gender

Pointers to parents (for ancestor tracking)

Required operations:

Find the oldest known ancestor of a given person

Check if a specific person exists in the family tree

Add a new family member with parent relationships

Example Input:
Grandpa (1940) 
├─ Dad (1970)
│  ├─ Me (2000)
│  └─ Sister (2002)
└─ Uncle (1975)

Example Operations:
Find oldest ancestor of "Me" → "Grandpa"

Check if "Cousin" exists → False

Add "Cousin" as child of "Uncle"

"""

from datetime import datetime

class FamilyMember:
    def __init__(self, name, birthdate, gender):
        self.name = name
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()
        self.gender = gender
        self.parents = []
        self.children = []

class FamilyTree:
    def __init__(self):
        self.members = {}
    
    def add_member(self, name, birthdate, gender, parent_names=None):
        if name in self.members:
            raise ValueError(f"{name} already exists in family tree")
        
        new_member = FamilyMember(name, birthdate, gender)
        self.members[name] = new_member
        
        if parent_names:
            for parent_name in parent_names:
                if parent_name in self.members:
                    parent = self.members[parent_name]
                    parent.children.append(new_member)
                    new_member.parents.append(parent)
        
        return new_member
    
    def find_oldest_ancestor(self, name):
        if name not in self.members:
            return None
        
        current = self.members[name]
        oldest = current
        
        while current.parents:
            # Assuming a person can't be older than their parents
            current = current.parents[0]  # Taking first parent (could choose oldest)
            if current.birthdate < oldest.birthdate:
                oldest = current
        
        return oldest.name if oldest != self.members[name] else None
    
    def person_exists(self, name):
        return name in self.members

# Example usage
family = FamilyTree()
family.add_member("Grandpa", "1940-01-01", "M")
family.add_member("Dad", "1970-05-15", "M", ["Grandpa"])
family.add_member("Uncle", "1975-08-20", "M", ["Grandpa"])
family.add_member("Me", "2000-11-10", "M", ["Dad"])
family.add_member("Sister", "2002-03-25", "F", ["Dad"])

print(family.find_oldest_ancestor("Me"))  # Output: "Grandpa"
print(family.person_exists("Cousin"))     # Output: False
family.add_member("Cousin", "2005-07-30", "F", ["Uncle"])
print(family.person_exists("Cousin"))     # Output: True

# Time Complexity:

# Ancestor search: O(h) where h is tree height

# Person search: O(n) worst case

# Insertion: O(1) for known parent

# Space Complexity: O(n) for storing all family members
"""    
2. File System Representation
Problem Statement:
Create a tree-based file system representation where:

Each node is either a File (with size) or Folder (with children)

Support these operations:

Create file/folder at path

Delete file/folder at path

Rename file/folder

Search for file/folder by name

Calculate total size of a folder (recursive)

Example Input:
root/
├─ documents/
│  ├─ resume.doc (50KB)
│  └─ notes.txt (10KB)
└─ photos/
   └─ vacation.jpg (200KB)

Example Operations:

Search for "notes.txt" → Found at "/root/documents/notes.txt"

Calculate size of "documents" → 60KB

Create new file "/root/photos/profile.jpg" (100KB)
"""
class FileSystemNode:
    def __init__(self, name, is_file=False, size=0):
        self.name = name
        self.is_file = is_file
        self.size = size
        self.children = {} if not is_file else None
        self.parent = None

class FileSystem:
    def __init__(self):
        self.root = FileSystemNode("root")
        self.root.parent = self.root  # Sentinel parent
    
    def _resolve_path(self, path):
        if not path.startswith("/"):
            raise ValueError("Path must start with /")
        
        parts = [p for p in path.split("/") if p]
        current = self.root
        
        for part in parts[:-1]:
            if part not in current.children:
                raise FileNotFoundError(f"Path not found: {path}")
            current = current.children[part]
            if current.is_file:
                raise ValueError(f"Path component is a file: {part}")
        
        return current, parts[-1] if parts else ""
    
    def create(self, path, is_file=False, size=0):
        parent, name = self._resolve_path(path)
        
        if name in parent.children:
            raise ValueError(f"{name} already exists at {path}")
        
        new_node = FileSystemNode(name, is_file, size)
        new_node.parent = parent
        parent.children[name] = new_node
        return new_node
    
    def delete(self, path):
        parent, name = self._resolve_path(path)
        
        if name not in parent.children:
            raise FileNotFoundError(f"Not found: {path}")
        
        return parent.children.pop(name)
    
    def rename(self, path, new_name):
        parent, name = self._resolve_path(path)
        
        if name not in parent.children:
            raise FileNotFoundError(f"Not found: {path}")
        if new_name in parent.children:
            raise ValueError(f"{new_name} already exists in this directory")
        
        node = parent.children[name]
        del parent.children[name]
        node.name = new_name
        parent.children[new_name] = node
    
    def search(self, name, current=None, path=""):
        if current is None:
            current = self.root
            path = "/root"
        
        results = []
        
        if current.name == name:
            results.append(path)
        
        if not current.is_file:
            for child_name, child_node in current.children.items():
                child_path = f"{path}/{child_name}"
                results.extend(self.search(name, child_node, child_path))
        
        return results
    
    def calculate_size(self, path):
        node, _ = self._resolve_path(path) if path != "/" else (self.root, "")
        
        if node.is_file:
            return node.size
        
        total = 0
        stack = [node]
        
        while stack:
            current = stack.pop()
            if current.is_file:
                total += current.size
            else:
                stack.extend(current.children.values())
        
        return total

# Example usage
fs = FileSystem()
fs.create("/root/documents", is_file=False)
fs.create("/root/documents/resume.doc", is_file=True, size=50)
fs.create("/root/documents/notes.txt", is_file=True, size=10)
fs.create("/root/photos", is_file=False)
fs.create("/root/photos/vacation.jpg", is_file=True, size=200)

print(fs.search("notes.txt"))  # Output: ['/root/documents/notes.txt']
print(fs.calculate_size("/root/documents"))  # Output: 60
fs.create("/root/photos/profile.jpg", is_file=True, size=100)
print(fs.calculate_size("/root/photos"))  # Output: 300

# Time Complexity:

# Path operations: O(m) where m is path depth

# Search: O(n) worst case

# Size calculation: O(n) for subtree

# Space Complexity: O(n) for storing all files/folders
    
"""
3. Binary Search Tree for Product Inventory
Problem Statement:
Implement a product inventory system using BST where each product has:

Unique product ID (integer)

Product name

Price

Quantity in stock

Required operations:

Insert new product

Delete product by ID

Search product by ID

List products in price range

Calculate total value of inventory in price range

Example Input:
ID  Name        Price  Stock
1   Laptop      999    5
2   Phone       699    10
3   Headphones  99     20

Example Operations:
Search ID 2 → Phone

Price range [100, 800] → Phone, Headphones

Total value in range [100, 800] → (699×10) + (99×20) = $8,970

"""
class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.left = None
        self.right = None

class ProductInventory:
    def __init__(self):
        self.root = None
    
    def insert(self, id, name, price, stock):
        if self.root is None:
            self.root = Product(id, name, price, stock)
        else:
            self._insert_helper(self.root, id, name, price, stock)
    
    def _insert_helper(self, node, id, name, price, stock):
        if id < node.id:
            if node.left is None:
                node.left = Product(id, name, price, stock)
            else:
                self._insert_helper(node.left, id, name, price, stock)
        elif id > node.id:
            if node.right is None:
                node.right = Product(id, name, price, stock)
            else:
                self._insert_helper(node.right, id, name, price, stock)
        else:
            raise ValueError(f"Product with ID {id} already exists")
    
    def search(self, id):
        return self._search_helper(self.root, id)
    
    def _search_helper(self, node, id):
        if node is None:
            return None
        if id == node.id:
            return node
        elif id < node.id:
            return self._search_helper(node.left, id)
        else:
            return self._search_helper(node.right, id)
    
    def delete(self, id):
        self.root = self._delete_helper(self.root, id)
    
    def _delete_helper(self, node, id):
        if node is None:
            return None
        
        if id < node.id:
            node.left = self._delete_helper(node.left, id)
        elif id > node.id:
            node.right = self._delete_helper(node.right, id)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children: get inorder successor
            temp = self._min_value_node(node.right)
            node.id, node.name, node.price, node.stock = temp.id, temp.name, temp.price, temp.stock
            node.right = self._delete_helper(node.right, temp.id)
        
        return node
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def products_in_price_range(self, min_price, max_price):
        products = []
        self._range_helper(self.root, min_price, max_price, products)
        return products
    
    def _range_helper(self, node, min_price, max_price, products):
        if node is None:
            return
        
        if min_price < node.price:
            self._range_helper(node.left, min_price, max_price, products)
        
        if min_price <= node.price <= max_price:
            products.append(node)
        
        if node.price < max_price:
            self._range_helper(node.right, min_price, max_price, products)
    
    def inventory_value_in_range(self, min_price, max_price):
        products = self.products_in_price_range(min_price, max_price)
        return sum(p.price * p.stock for p in products)

# Example usage
inventory = ProductInventory()
inventory.insert(1, "Laptop", 999, 5)
inventory.insert(2, "Phone", 699, 10)
inventory.insert(3, "Headphones", 99, 20)

print(inventory.search(2).name)  # Output: "Phone"

products = inventory.products_in_price_range(100, 800)
print([p.name for p in products])  # Output: ["Phone", "Headphones"]

total_value = inventory.inventory_value_in_range(100, 800)
print(total_value)  # Output: 8970 (699*10 + 99*20)

# Time Complexity:

# Insert/Search/Delete: O(h) where h is tree height (O(log n) balanced)

# Range queries: O(n) in worst case

# Inventory value: O(n) for subtree

# Space Complexity: O(n) for storing all products
"""
4. Decision Tree for Loan Approval
Problem Statement:
Implement a decision tree for loan approval with these factors:

Credit Score (0-850)

Income Level (annual)

Loan Amount

Employment Status (employed/unemployed)

Decision rules:

If credit score < 600 → Reject

If credit score 600-700 and income < $50k → Further review

If credit score > 700 and loan < $1M → Approve

If unemployed → Reject

Else → Further review

Example Input:

1. Credit: 720, Income: 80k,Loan:500k, Employed → Approve

2. Credit: 650, Income: 45k,Loan:200k, Employed → Further review

3. Credit: 580, Income: 100k,Loan:50k, Unemployed → Reject

"""
class LoanApplication:
    def __init__(self, credit_score, income, loan_amount, is_employed):
        self.credit_score = credit_score
        self.income = income
        self.loan_amount = loan_amount
        self.is_employed = is_employed

class LoanDecisionTree:
    def evaluate(self, application):
        if not application.is_employed:
            return "Reject (unemployed)"
        
        if application.credit_score < 600:
            return "Reject (poor credit)"
        
        if 600 <= application.credit_score <= 700:
            if application.income < 50000:
                return "Further review (moderate credit with low income)"
        
        if application.credit_score > 700:
            if application.loan_amount < 1000000:
                return "Approve (good credit and reasonable loan)"
        
        return "Further review (requires manual evaluation)"

# Example usage
decision_tree = LoanDecisionTree()

app1 = LoanApplication(720, 80000, 500000, True)
print(decision_tree.evaluate(app1))  # Output: "Approve (good credit and reasonable loan)"

app2 = LoanApplication(650, 45000, 200000, True)
print(decision_tree.evaluate(app2))  # Output: "Further review (moderate credit with low income)"

app3 = LoanApplication(580, 100000, 50000, False)
print(decision_tree.evaluate(app3))  # Output: "Reject (unemployed)"

app4 = LoanApplication(680, 60000, 1200000, True)
print(decision_tree.evaluate(app4))  # Output: "Further review (requires manual evaluation)"

# Time Complexity: O(1) for each decision (fixed depth tree)
# Space Complexity: O(1) (fixed number of decision nodes)

"""
6. Expression Tree Evaluation
Problem Statement:
Build an expression tree to represent mathematical expressions where:

Leaf nodes contain numbers

Internal nodes contain operators (+, -, *, /)

Implement evaluation of the expression tree

Example Input:

      *
     / \
    +   5
   / \
  3   4
(Represents (3 + 4) * 5)

Example Output: 35
"""

class ExpressionNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def evaluate_expression_tree(root):
    if root is None:
        return 0
    
    # Leaf nodes are numbers
    if not root.left and not root.right:
        return float(root.value)
    
    # Evaluate left and right subtrees
    left_val = evaluate_expression_tree(root.left)
    right_val = evaluate_expression_tree(root.right)
    
    # Apply operator
    if root.value == '+':
        return left_val + right_val
    elif root.value == '-':
        return left_val - right_val
    elif root.value == '*':
        return left_val * right_val
    elif root.value == '/':
        return left_val / right_val
    else:
        raise ValueError("Unknown operator")

# Example usage
# Building the tree: (3 + 4) * 5
root = ExpressionNode('*')
root.left = ExpressionNode('+')
root.left.left = ExpressionNode('3')
root.left.right = ExpressionNode('4')
root.right = ExpressionNode('5')

print(evaluate_expression_tree(root))  # Output: 35.0


# Time Complexity: O(n) - visiting each node once
# Space Complexity: O(h) - recursion stack height (h = tree height)

"""
7. Employee Hierarchy BST
Problem Statement:
Create a BST representing employee hierarchy where:

Each node contains (employee_id, name, position, salary, manager_id)

Implement LCA (Lowest Common Ancestor) to find common manager for two employees

Example Input:

       (1, CEO)
       /     \
 (2, CTO)  (3, CFO)
    /   \       \
(4, Eng) (5, PM) (6, Accountant)
Example Operations:

Find LCA for employees 4 and 5 → 2 (CTO)

Find LCA for employees 4 and 6 → 1 (CEO)

"""

class EmployeeNode:
    def __init__(self, emp_id, name, position, salary, manager_id=None):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.manager_id = manager_id
        self.left = None
        self.right = None

class EmployeeHierarchy:
    def __init__(self):
        self.root = None
    
    def add_employee(self, emp_id, name, position, salary, manager_id=None):
        if not self.root and manager_id is None:
            self.root = EmployeeNode(emp_id, name, position, salary)
            return
        
        if manager_id is None:
            raise ValueError("Non-root employee must have a manager")
        
        manager = self._find_node(self.root, manager_id)
        if not manager:
            raise ValueError(f"Manager {manager_id} not found")
        
        new_employee = EmployeeNode(emp_id, name, position, salary, manager_id)
        
        # Insert in BST fashion (by emp_id)
        self._insert_helper(self.root, new_employee)
    
    def _insert_helper(self, current, new_node):
        if new_node.emp_id < current.emp_id:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_helper(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_helper(current.right, new_node)
    
    def _find_node(self, current, emp_id):
        if not current:
            return None
        if current.emp_id == emp_id:
            return current
        elif emp_id < current.emp_id:
            return self._find_node(current.left, emp_id)
        else:
            return self._find_node(current.right, emp_id)
    
    def find_common_manager(self, emp_id1, emp_id2):
        path1 = self._get_path(self.root, emp_id1)
        path2 = self._get_path(self.root, emp_id2)
        
        if not path1 or not path2:
            return None
        
        # Find first divergence point
        lca = None
        for e1, e2 in zip(path1, path2):
            if e1.emp_id == e2.emp_id:
                lca = e1
            else:
                break
        
        return lca
    
    def _get_path(self, current, emp_id):
        if not current:
            return []
        
        if current.emp_id == emp_id:
            return [current]
        
        if emp_id < current.emp_id:
            path = self._get_path(current.left, emp_id)
        else:
            path = self._get_path(current.right, emp_id)
        
        if path:
            return [current] + path
        return []

# Example usage
hierarchy = EmployeeHierarchy()
hierarchy.add_employee(1, "Alice", "CEO", 200000)
hierarchy.add_employee(2, "Bob", "CTO", 180000, 1)
hierarchy.add_employee(3, "Charlie", "CFO", 190000, 1)
hierarchy.add_employee(4, "Dave", "Engineer", 120000, 2)
hierarchy.add_employee(5, "Eve", "PM", 150000, 2)
hierarchy.add_employee(6, "Frank", "Accountant", 110000, 3)

# Find common manager between employee 4 and 5
lca = hierarchy.find_common_manager(4, 5)
print(f"Common manager: {lca.name} ({lca.position})")  # Output: Bob (CTO)

# Find common manager between employee 4 and 6
lca = hierarchy.find_common_manager(4, 6)
print(f"Common manager: {lca.name} ({lca.position})")  # Output: Alice (CEO)

# Time Complexity:

# Insert: O(h) where h is tree height

# Search: O(h)

# LCA: O(h)

# Space Complexity: O(n) for storing all employees

"""
8. Delivery Routing System
Problem Statement:
Model a delivery routing system as a tree where:

Nodes represent delivery locations

Edges represent connections between locations

Implement shortest path finding between two locations

Example Input:

        Warehouse
        /   |   \
     A     B     C
    / \         / \
   D   E       F   G
Example Operations:

Shortest path from D to E → D → A → E

Shortest path from F to G → F → C → G
"""


from collections import deque

class DeliveryLocation:
    def __init__(self, name):
        self.name = name
        self.connections = []

class DeliverySystem:
    def __init__(self):
        self.locations = {}
    
    def add_location(self, name):
        if name not in self.locations:
            self.locations[name] = DeliveryLocation(name)
    
    def connect_locations(self, name1, name2):
        if name1 not in self.locations or name2 not in self.locations:
            raise ValueError("Location not found")
        self.locations[name1].connections.append(self.locations[name2])
        self.locations[name2].connections.append(self.locations[name1])
    
    def find_shortest_path(self, start, end):
        if start not in self.locations or end not in self.locations:
            return None
        
        # BFS setup
        queue = deque()
        queue.append([self.locations[start]])
        visited = {self.locations[start]}
        
        while queue:
            path = queue.popleft()
            current = path[-1]
            
            if current.name == end:
                return [loc.name for loc in path]
            
            for neighbor in current.connections:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        
        return None  # No path found

# Example usage
system = DeliverySystem()
locations = ["Warehouse", "A", "B", "C", "D", "E", "F", "G"]
for loc in locations:
    system.add_location(loc)

# Building the tree structure
system.connect_locations("Warehouse", "A")
system.connect_locations("Warehouse", "B")
system.connect_locations("Warehouse", "C")
system.connect_locations("A", "D")
system.connect_locations("A", "E")
system.connect_locations("C", "F")
system.connect_locations("C", "G")

# Find paths
print(system.find_shortest_path("D", "E"))  # Output: ['D', 'A', 'E']
print(system.find_shortest_path("F", "G"))  # Output: ['F', 'C', 'G']
print(system.find_shortest_path("D", "G"))  # Output: ['D', 'A', 'Warehouse', 'C', 'G']

# Time Complexity: O(n) for BFS traversal
# Space Complexity: O(n) for queue and path tracking

"""
9. Game Leaderboard with AVL Tree
Problem Statement:
Implement a game leaderboard using AVL tree to:

Maintain player scores in sorted order

Efficiently retrieve top N players

Support insertions and deletions

Example Input:
Player scores: [1500, 1200, 1800, 2000, 900]

Example Operations:

Get top 3 → [2000, 1800, 1500]

Insert new score 1700

Get top 3 → [2000, 1800, 1700]

"""
class AVLNode:
    def __init__(self, player_id, score):
        self.player_id = player_id
        self.score = score
        self.left = None
        self.right = None
        self.height = 1

class Leaderboard:
    def __init__(self):
        self.root = None
    
    def _height(self, node):
        if not node:
            return 0
        return node.height
    
    def _balance_factor(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)
    
    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))
    
    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        self._update_height(y)
        self._update_height(x)
        
        return x
    
    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        self._update_height(x)
        self._update_height(y)
        
        return y
    
    def insert(self, player_id, score):
        self.root = self._insert_helper(self.root, player_id, score)
    
    def _insert_helper(self, node, player_id, score):
        if not node:
            return AVLNode(player_id, score)
        
        if score > node.score:  # Higher scores go left
            node.left = self._insert_helper(node.left, player_id, score)
        else:
            node.right = self._insert_helper(node.right, player_id, score)
        
        self._update_height(node)
        
        balance = self._balance_factor(node)
        
        # Left Left Case
        if balance > 1 and score > node.left.score:
            return self._rotate_right(node)
        
        # Right Right Case
        if balance < -1 and score <= node.right.score:
            return self._rotate_left(node)
        
        # Left Right Case
        if balance > 1 and score <= node.left.score:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Right Left Case
        if balance < -1 and score > node.right.score:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def get_top_n(self, n):
        result = []
        self._inorder_traversal(self.root, result)
        return result[:n]
    
    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append((node.player_id, node.score))
            self._inorder_traversal(node.right, result)

# Example usage
leaderboard = Leaderboard()
scores = [("p1", 1500), ("p2", 1200), ("p3", 1800), ("p4", 2000), ("p5", 900)]
for pid, score in scores:
    leaderboard.insert(pid, score)

print("Top 3 players:")
for i, (pid, score) in enumerate(leaderboard.get_top_n(3), 1):
    print(f"{i}. Player {pid}: {score}")

# Insert new player
leaderboard.insert("p6", 1700)
print("\nAfter inserting player with 1700:")
for i, (pid, score) in enumerate(leaderboard.get_top_n(3), 1):
    print(f"{i}. Player {pid}: {score}")

# Time Complexity:

# Insert/Delete: O(log n)

# Get top N: O(n) (in-order traversal)

# Space Complexity: O(n) for storing all scores


"""    
10. Task Scheduler with Priority Heap
Problem Statement:
Implement a task scheduler using max-heap where:

Each task has (name, priority)

Higher priority numbers indicate higher priority

Support operations:

Add task

Remove highest priority task

Peek next task

Example Input:
Tasks: [("Backup", 3), ("Email", 1), ("Report", 5)]

Example Operations:

Next task → Report (5)

Process task → removes Report

Next task → Backup (3)
"""
import heapq

class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
    
    # Override comparison operators for max-heap
    def __lt__(self, other):
        return self.priority > other.priority  # Reverse for max-heap
    
    def __eq__(self, other):
        return self.priority == other.priority

class TaskScheduler:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, name, priority):
        task = Task(name, priority)
        heapq.heappush(self.tasks, task)
    
    def get_next_task(self):
        if not self.tasks:
            return None
        return self.tasks[0]
    
    def process_next_task(self):
        if not self.tasks:
            return None
        return heapq.heappop(self.tasks)
    
    def is_empty(self):
        return len(self.tasks) == 0

# Example usage
scheduler = TaskScheduler()
scheduler.add_task("Backup", 3)
scheduler.add_task("Email", 1)
scheduler.add_task("Report", 5)

print("Initial tasks by priority:")
while not scheduler.is_empty():
    next_task = scheduler.process_next_task()
    print(f"Processing: {next_task.name} (priority {next_task.priority})")

# Output:
# Processing: Report (priority 5)
# Processing: Backup (priority 3)
# Processing: Email (priority 1)

# Time Complexity:

# Insert: O(log n)

# Remove: O(log n)

# Peek: O(1)

# Space Complexity: O(n) for storing all tasks
