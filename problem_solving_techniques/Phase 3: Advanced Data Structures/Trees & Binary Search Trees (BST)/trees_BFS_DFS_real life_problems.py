"""
1. Social Media Friend Suggestion System (BFS)
Problem Statement:
In a social media application, users have a list of friends. To suggest new friends, we want to find friends of friends (FoF) who are not already directly connected to the user.

Example Input:

"""

connections = {
    "Alice": ["Bob", "Charlie"],
    "Bob": ["Alice", "David"],
    "Charlie": ["Alice", "Eve"],
    "David": ["Bob"],
    "Eve": ["Charlie"]
}
user = "Alice"
Expected Output:



["David", "Eve"]
Solution:



from collections import deque

def friend_suggestions(connections, user):
    if user not in connections:
        return []

    queue = deque([user])
    visited = set([user])
    suggestions = set()

    while queue:
        current_user = queue.popleft()

        for friend in connections[current_user]:
            if friend not in visited:
                queue.append(friend)
                visited.add(friend)

                for fof in connections.get(friend, []):
                    if fof != user and fof not in connections[user]:
                        suggestions.add(fof)

    return list(suggestions)

connections = {
    "Alice": ["Bob", "Charlie"],
    "Bob": ["Alice", "David"],
    "Charlie": ["Alice", "Eve"],
    "David": ["Bob"],
    "Eve": ["Charlie"]
}

print(friend_suggestions(connections, "Alice"))
# Complexity:
# Time Complexity: O(V+E), where V is the number of users and E is the number of connections.
# Space Complexity: O(V), for the visited set and queue.

2. Path Finding in a City Grid (BFS)
Problem Statement:
A city is represented as an 
𝑁
×
𝑀
N×M grid where 0 represents open paths and 1 represents blocked roads. Find the shortest path from the top-left (0,0) to the bottom-right (N-1,M-1).

Example Input:



grid = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0]
]
Expected Output:



Shortest Path Length: 5
Solution:



from collections import deque

def shortest_path(grid):
    if not grid or grid[0][0] == 1:
        return -1

    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, 0, 1)])  # (row, col, distance)
    visited = set([(0, 0)])

    while queue:
        r, c, dist = queue.popleft()
        if r == rows - 1 and c == cols - 1:
            return dist  # Found the shortest path

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                queue.append((nr, nc, dist + 1))
                visited.add((nr, nc))

    return -1  # No path found

grid = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0]
]

print(f"Shortest Path Length: {shortest_path(grid)}")
Complexity:
Time Complexity: 
𝑂
(
𝑁
×
𝑀
)
O(N×M), where 
𝑁
N is rows and 
𝑀
M is columns.
Space Complexity: 
𝑂
(
𝑁
×
𝑀
)
O(N×M), for the visited set and queue.
3. Building Management - Elevator System (BFS)
Problem Statement:
An elevator system has N floors. You start at floor S and want to reach floor T. You can move up U floors or down D floors. Find the minimum number of button presses to reach T.

Example Input:



N = 10  # Total floors
S = 1   # Start floor
T = 7   # Target floor
U = 3   # Up movement
D = 1   # Down movement
Expected Output:



Minimum button presses: 3
Solution:



def min_button_presses(N, S, T, U, D):
    if S == T:
        return 0

    queue = deque([(S, 0)])  # (current floor, presses)
    visited = set([S])

    while queue:
        floor, presses = queue.popleft()

        for next_floor in (floor + U, floor - D):
            if next_floor == T:
                return presses + 1
            if 1 <= next_floor <= N and next_floor not in visited:
                queue.append((next_floor, presses + 1))
                visited.add(next_floor)

    return -1  # No way to reach target floor

print(f"Minimum button presses: {min_button_presses(10, 1, 7, 3, 1)}")
Complexity:
Time Complexity: 
𝑂
(
𝑁
)
O(N), as we process each floor once.
Space Complexity: 
𝑂
(
𝑁
)
O(N), for visited set.
4. Virus Spread in a Network (BFS)
Problem Statement:
A computer network is represented as a graph. A virus starts from a given node and spreads to connected computers in 1 minute per connection. Find how many minutes until all computers are infected.

Example Input:



network = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3]
}
start = 1
Expected Output:



Minutes until all computers are infected: 2
Solution:



def virus_spread(network, start):
    queue = deque([(start, 0)])  # (current node, minutes)
    visited = set([start])
    max_minutes = 0

    while queue:
        node, minutes = queue.popleft()
        max_minutes = max(max_minutes, minutes)

        for neighbor in network.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, minutes + 1))
                visited.add(neighbor)

    return max_minutes

network = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3]
}

print(f"Minutes until all computers are infected: {virus_spread(network, 1)}")
Complexity:
Time Complexity: 
O(V+E)
Space Complexity: 
O(V)

## 5. **Product Recommendation System (DFS)**
### Problem Statement:
An e-commerce website wants to recommend products to customers based on product categories. The category structure is a tree where each node represents a category, and leaf nodes represent products. Given a category, list all products under that category.

### Example Input:

categories = {
    "Electronics": ["Phones", "Laptops"],
    "Phones": ["iPhone", "Samsung Galaxy"],
    "Laptops": ["MacBook", "Dell Inspiron"],
    "Clothing": ["T-Shirts", "Jeans"],
    "T-Shirts": ["Nike Tee", "Adidas Tee"]
}
category = "Electronics"

### Expected Output:

['iPhone', 'Samsung Galaxy', 'MacBook', 'Dell Inspiron']


### Solution:

def get_products(categories, category):
    result = []

    def dfs(cat):
        if cat not in categories:
            result.append(cat)
            return
        for sub_cat in categories[cat]:
            dfs(sub_cat)

    dfs(category)
    return result

print(get_products(categories, "Electronics"))

### Complexity:
- **Time Complexity**: O(N), where N is the total number of categories and products.
- **Space Complexity**: O(N), for the recursion stack.

---

## 6. **Company Organizational Hierarchy (DFS)**
### Problem Statement:
A company has an organizational hierarchy represented by a tree. Given the CEO node, list all employees under the CEO in the order of reporting.

### Example Input:

org = {
    "CEO": ["Manager1", "Manager2"],
    "Manager1": ["Employee1", "Employee2"],
    "Manager2": ["Employee3"]
}

### Expected Output:

['Manager1', 'Employee1', 'Employee2', 'Manager2', 'Employee3']


### Solution:

def get_employees(org, ceo):
    result = []

    def dfs(employee):
        result.append(employee)
        if employee in org:
            for sub in org[employee]:
                dfs(sub)

    dfs(ceo)
    return result

print(get_employees(org, "CEO"))

### Complexity:
- **Time Complexity**: O(N)
- **Space Complexity**: O(N)

---

## 7. **Route Optimization in Delivery Services (BFS)**
### Problem Statement:
A delivery service needs to find the shortest route between two locations on a city map represented as a graph.

### Example Input:

city_map = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"]
}
start = "A"
end = "E"

### Expected Output:

['A', 'C', 'D', 'E']

from collections import deque

def shortest_route(city_map, start, end):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        for neighbor in city_map[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

    return []

print(shortest_route(city_map, "A", "E"))

### Complexity:
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)


## 8. **File System Explorer (DFS)**
### Problem Statement:
Given a file system directory structure represented as a tree, list all files under a directory recursively.

### Example Input:
file_system = {
    "root": ["folder1", "folder2"],
    "folder1": ["file1.txt", "folder3"],
    "folder3": ["file2.txt"],
    "folder2": ["file3.txt"]
}

### Expected Output:
['file1.txt', 'file2.txt', 'file3.txt']

def list_files(file_system, directory):
    files = []

    def dfs(folder):
        if folder not in file_system:
            files.append(folder)
            return
        for sub in file_system[folder]:
            dfs(sub)

    dfs(directory)
    return files

print(list_files(file_system, "root"))

### Complexity:
- **Time Complexity**: O(N)
- **Space Complexity**: O(N)


## 9. **Airport Connection System (BFS)**
### Problem Statement:
Given airports and their direct flight connections, find the shortest path from one airport to another.

### Example Input:
flights = {
    "JFK": ["LAX", "ATL"],
    "LAX": ["ORD"],
    "ATL": ["ORD", "MIA"],
    "ORD": ["MIA"],
    "MIA": []
}
start = "JFK"
end = "MIA"

### Expected Output:

['JFK', 'ATL', 'MIA']
from collections import deque

def shortest_flight_path(flights, start, end):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        airport, path = queue.popleft()
        if airport == end:
            return path
        for next_airport in flights.get(airport, []):
            if next_airport not in visited:
                queue.append((next_airport, path + [next_airport]))
                visited.add(next_airport)

    return []

print(shortest_flight_path(flights, "JFK", "MIA"))

### Complexity:
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)

---

## 10. **Word Ladder Transformation (BFS)**
### Problem Statement:
Given two words and a dictionary, find the shortest transformation sequence from the start word to the end word such that only one letter can be changed at a time.

### Example Input:

start = "hit"
end = "cog"
dictionary = {"hot", "dot", "dog", "lot", "log", "cog"}

### Expected Output:

['hit', 'hot', 'dot', 'dog', 'cog']


### Solution:

from collections import deque

def word_ladder(start, end, dictionary):
    queue = deque([(start, [start])])
    dictionary.add(end)

    while queue:
        word, path = queue.popleft()
        if word == end:
            return path

        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + c + word[i+1:]
                if new_word in dictionary:
                    queue.append((new_word, path + [new_word]))
                    dictionary.remove(new_word)

    return []

print(word_ladder("hit", "cog", {"hot", "dot", "dog", "lot", "log"}))

### Complexity:
- **Time Complexity**: O(N * 26^L)
- **Space Complexity**: O(N)


10. Product Recommendation System (BFS)

Problem Statement:

Given a list of products and customer purchase history, recommend products based on what other customers bought along with the current product.

Example Input:

purchases = {
    "Laptop": ["Mouse", "Keyboard"],
    "Mouse": ["Laptop", "Headphones"],
    "Keyboard": ["Laptop", "Mouse"]
}
product = "Laptop"

Expected Output:

["Mouse", "Keyboard", "Headphones"]

Solution:

def recommend_products(purchases, product):
    queue = deque([product])
    visited = set([product])
    recommendations = set()

    while queue:
        current = queue.popleft()
        for p in purchases.get(current, []):
            if p not in visited:
                recommendations.add(p)
                queue.append(p)
                visited.add(p)

    return list(recommendations)

print(recommend_products(purchases, "Laptop"))

Complexity:

Time Complexity: O(V + E)

Space Complexity: O(V)

