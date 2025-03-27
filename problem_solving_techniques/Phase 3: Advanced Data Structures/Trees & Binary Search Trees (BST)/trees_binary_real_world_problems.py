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