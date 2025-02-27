"""
1. Social Media Friend Suggestion System (BFS)
Problem Statement:
In a social media application, users have a list of friends. To suggest new friends, we want to find friends of friends (FoF) 
who are not already directly connected to the user.

Example Input:



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

"""

from collections import deque
from collections import deque  # Import deque for BFS traversal

def friend_suggestions(connections, user):
    if user not in connections:  # Check if the user exists in the connections dictionary
        return []

    queue = deque([user])  # Initialize the queue with the user
    visited = set([user])  # Keep track of visited users to avoid duplicates
    suggestions = set()  # Store suggested friends

    while queue:
        current_user = queue.popleft()  # Dequeue the current user

        for friend in connections[current_user]:  # Iterate through direct friends
            if friend not in visited:  # Check if the friend is not already visited
                queue.append(friend)  # Add friend to queue for further exploration
                visited.add(friend)  # Mark the friend as visited

                # Iterate through the friends of the friend (fof = friend of friend)
                for fof in connections.get(friend, []):  
                    # Ensure the suggested friend is not the user and not already a direct friend
                    if fof != user and fof not in connections[user]:
                        suggestions.add(fof)  # Add to suggestions

    return list(suggestions)  # Convert set to list for output

# Sample connections dictionary representing a social network
connections = {
    "Alice": ["Bob", "Charlie"],
    "Bob": ["Alice", "David"],
    "Charlie": ["Alice", "Eve"],
    "David": ["Bob"],
    "Eve": ["Charlie"]
}

user = "Alice"
print(friend_suggestions(connections, user))  # Print friend suggestions for Alice

# Complexity:
# Time Complexity: O(V+E), where V is the number of users and E is the number of connections.
# Space Complexity: O(V), for the visited set and queue.

"""
2. Path Finding in a City Grid (BFS)
Problem Statement:
A city is represented as an N×M grid where 0 represents open paths and 1 represents blocked roads. Find the shortest path from 
the top-left (0,0) to the bottom-right (N-1,M-1).

Example Input:

grid = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0]
]

Expected Output:

Shortest Path Length: 5
"""

from collections import deque

from collections import deque  # Import deque for BFS traversal

def shortest_path(grid):
    # Check if the grid is empty or the starting point is blocked
    if not grid or grid[0][0] == 1:
        return -1

    rows, cols = len(grid), len(grid[0])  # Get grid dimensions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Possible movement directions (right, down, left, up)
    
    # Initialize the queue with the starting position (row, col, distance)
    queue = deque([(0, 0, 1)])  
    visited = set([(0, 0)])  # Keep track of visited cells to avoid cycles

    while queue:
        r, c, dist = queue.popleft()  # Dequeue the current cell

        # If we reach the bottom-right corner, return the distance (shortest path length)
        if r == rows - 1 and c == cols - 1:
            return dist  

        # Explore all possible directions (right, down, left, up)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc  # Calculate the new row and column
            
            # Check if the new position is within bounds, not blocked, and not visited
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                queue.append((nr, nc, dist + 1))  # Enqueue the new position with updated distance
                visited.add((nr, nc))  # Mark it as visited

    return -1  # Return -1 if no path to the destination exists

# Example grid where 0 represents an open path and 1 represents an obstacle
grid = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0]
]

# Find and print the shortest path length
print(f"Shortest Path Length: {shortest_path(grid)}")

# Complexity:
# Time Complexity: O(N×M), where N is rows and M is columns.
# Space Complexity: O(N×M), for the visited set and queue.
                    
"""
3. Building Management - Elevator System (BFS)
Problem Statement:
An elevator system has N floors. You start at floor S and want to reach floor T. You can move up U floors or down D floors. 
Find the minimum number of button presses to reach T.

Example Input:

N = 10  # Total floors
S = 1   # Start floor
T = 7   # Target floor
U = 3   # Up movement
D = 1   # Down movement
Expected Output:

Minimum button presses: 3

"""

from collections import deque  # Import deque for BFS traversal

def min_button_presses(N, S, T, U, D):
    # If the starting floor is the same as the target floor, no button presses are needed
    if S == T:
        return 0

    # Initialize the queue with the starting floor and zero button presses
    queue = deque([(S, 0)])  # (current floor, presses)
    visited = set([S])  # Keep track of visited floors to avoid cycles

    while queue:
        floor, presses = queue.popleft()  # Dequeue the current floor and button presses count

        # Try moving up (U) and down (D) from the current floor
        for next_floor in (floor + U, floor - D):
            # If the next floor is the target, return the number of presses taken to reach it
            if next_floor == T:
                return presses + 1
            
            # Ensure the next floor is within the valid range and hasn't been visited before
            if 1 <= next_floor <= N and next_floor not in visited:
                queue.append((next_floor, presses + 1))  # Enqueue the new floor with updated presses count
                visited.add(next_floor)  # Mark it as visited

    return -1  # If we exhaust all options and never reach T, return -1 (not possible to reach target)

# Example usage: Building with 10 floors, starting at 1, target is 7, can move up 3 floors or down 1 floor
print(f"Minimum button presses: {min_button_presses(10, 1, 7, 3, 1)}")

# Complexity:
# Time Complexity: O(N), as we process each floor once.
# Space Complexity: O(N), for visited set.
"""
4. Virus Spread in a Network (BFS)
Problem Statement:
A computer network is represented as a graph. A virus starts from a given node and spreads to connected computers in 1 minute per connection. 
Find how many minutes until all computers are infected.

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


"""
from collections import deque  # Import deque for BFS traversal

def virus_spread(network, start):
    """
    Simulates the spread of a computer virus in a network.

    :param network: A dictionary representing the network graph where keys are computers (nodes)
                    and values are lists of directly connected computers (edges).
    :param start: The starting computer (node) where the virus begins spreading.
    :return: The number of minutes until all connected computers are infected.
    """

    # Initialize the queue with the starting node and 0 minutes elapsed
    queue = deque([(start, 0)])  # (current node, minutes)
    visited = set([start])  # Track visited nodes to prevent reprocessing
    max_minutes = 0  # Track the longest time taken to reach a computer

    while queue:
        node, minutes = queue.popleft()  # Dequeue the current node and minutes elapsed
        max_minutes = max(max_minutes, minutes)  # Update max infection time

        # Explore all directly connected computers (neighbors)
        for neighbor in network.get(node, []):
            if neighbor not in visited:  # If not already infected
                queue.append((neighbor, minutes + 1))  # Add to queue with updated time
                visited.add(neighbor)  # Mark as infected (visited)

    return max_minutes  # Return the total time required to infect all reachable computers

# Example network where each key represents a computer, and values are its direct connections
network = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3]
}

# Start virus spread from computer 1
print(f"Minutes until all computers are infected: {virus_spread(network, 1)}")

# Complexity:
# Time Complexity: O(V+E)
# Space Complexity: O(V)
"""
5. Product Recommendation System (DFS)
Problem Statement:
An e-commerce website wants to recommend products to customers based on product categories. 
The category structure is a tree where each node represents a category, and leaf nodes represent products. 
Given a category, list all products under that category.

 Example Input:

categories = {
    "Electronics": ["Phones", "Laptops"],
    "Phones": ["iPhone", "Samsung Galaxy"],
    "Laptops": ["MacBook", "Dell Inspiron"],
    "Clothing": ["T-Shirts", "Jeans"],
    "T-Shirts": ["Nike Tee", "Adidas Tee"]
}
category = "Electronics"

 Expected Output:

['iPhone', 'Samsung Galaxy', 'MacBook', 'Dell Inspiron']
"""
def get_products(categories, category):
    """
    Retrieves all products (leaf nodes) under a given category using Depth-First Search (DFS).

    :param categories: A dictionary where keys are categories and values are lists of subcategories/products.
    :param category: The starting category from which we want to retrieve products.
    :return: A list of all products under the given category.
    """
    
    result = []  # List to store the final product names

    def dfs(cat):
        """
        Performs a Depth-First Search (DFS) to traverse the category tree.

        :param cat: The current category being explored.
        """
        # If the category has no subcategories, it's a product; add it to the result list
        if cat not in categories:
            result.append(cat)
            return
        
        # Recursively explore all subcategories/products
        for sub_cat in categories[cat]:
            dfs(sub_cat)

    # Start DFS traversal from the given category
    dfs(category)
    return result  # Return the list of products

# Example category tree where keys represent categories, and values represent subcategories or products
categories = {
    "Electronics": ["Phones", "Laptops"],
    "Phones": ["iPhone", "Samsung Galaxy"],
    "Laptops": ["MacBook", "Dell Inspiron"],
    "Clothing": ["T-Shirts", "Jeans"],
    "T-Shirts": ["Nike Tee", "Adidas Tee"]
}

# Get all products under "Electronics"
print(get_products(categories, "Electronics"))

#  Complexity:
# - Time Complexity: O(N), where N is the total number of categories and products.
# - Space Complexity: O(N), for the recursion stack.


"""
 6. Company Organizational Hierarchy (DFS)
 Problem Statement:
A company has an organizational hierarchy represented by a tree. Given the CEO node, list all employees under the CEO in the order of reporting.

 Example Input:

org = {
    "CEO": ["Manager1", "Manager2"],
    "Manager1": ["Employee1", "Employee2"],
    "Manager2": ["Employee3"]
}

 Expected Output:

['Manager1', 'Employee1', 'Employee2', 'Manager2', 'Employee3']

"""

def get_employees(org, ceo):
    """
    Retrieves all employees in an organization starting from the CEO using Depth-First Search (DFS).

    :param org: A dictionary where keys are managers and values are lists of their direct reports (subordinates).
    :param ceo: The starting position (root of the hierarchy), typically the CEO.
    :return: A list of all employees in the organization.
    """

    result = []  # List to store all employees in the hierarchy

    def dfs(employee):
        """
        Performs a Depth-First Search (DFS) to traverse the organizational hierarchy.

        :param employee: The current employee (manager or individual contributor) being explored.
        """
        result.append(employee)  # Add the employee to the result list

        # If the employee has subordinates, recursively explore each of them
        if employee in org:
            for sub in org[employee]:
                dfs(sub)

    # Start DFS traversal from the CEO
    dfs(ceo)
    return result  # Return the complete list of employees

# Example organization structure
org = {
    "CEO": ["Manager1", "Manager2"],  # CEO manages Manager1 and Manager2
    "Manager1": ["Employee1", "Employee2"],  # Manager1 manages Employee1 and Employee2
    "Manager2": ["Employee3"]  # Manager2 manages Employee3
}

# Get all employees starting from the CEO
print(get_employees(org, "CEO"))


#  Complexity:
# - Time Complexity: O(N)
# - Space Complexity: O(N)

"""
 7. Route Optimization in Delivery Services (BFS)
 Problem Statement:
A delivery service needs to find the shortest route between two locations on a city map represented as a graph.

 Example Input:

city_map = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"]
}
start = "A"
end = "E"

 Expected Output:

['A', 'C', 'D', 'E']"""

from collections import deque

from collections import deque

def shortest_route(city_map, start, end):
    """
    Finds the shortest route between two locations in a city using Breadth-First Search (BFS).

    :param city_map: A dictionary where keys are locations and values are lists of directly connected locations.
    :param start: The starting location.
    :param end: The destination location.
    :return: A list representing the shortest path from start to end. Returns an empty list if no path exists.
    """

    queue = deque([(start, [start])])  # Queue stores (current location, path taken)
    visited = set([start])  # Set to keep track of visited locations

    while queue:
        node, path = queue.popleft()  # Dequeue the front element (current location, path so far)

        # If we reached the destination, return the path
        if node == end:
            return path

        # Explore all neighboring locations
        for neighbor in city_map[node]:
            if neighbor not in visited:  # Only visit unvisited locations
                queue.append((neighbor, path + [neighbor]))  # Add neighbor and updated path to the queue
                visited.add(neighbor)  # Mark the neighbor as visited

    return []  # Return empty list if no path exists between start and end

# Example city map with roads between locations
city_map = {
    "A": ["B", "C"],  # A is connected to B and C
    "B": ["A", "D"],  # B is connected to A and D
    "C": ["A", "D"],  # C is connected to A and D
    "D": ["B", "C", "E"],  # D is connected to B, C, and E
    "E": ["D"]  # E is connected to D
}

# Define start and end points
start = "A"
end = "E"

# Find and print the shortest route
print(shortest_route(city_map, "A", "E"))


#  Complexity:
# - Time Complexity: O(V + E)
# - Space Complexity: O(V)

"""
 8. File System Explorer (DFS)
 Problem Statement:
Given a file system directory structure represented as a tree, list all files under a directory recursively.

 Example Input:
file_system = {
    "root": ["folder1", "folder2"],
    "folder1": ["file1.txt", "folder3"],
    "folder3": ["file2.txt"],
    "folder2": ["file3.txt"]
}

 Expected Output:
['file1.txt', 'file2.txt', 'file3.txt']
"""
def list_files(file_system, directory):
    """
    Recursively lists all files within a given directory using Depth-First Search (DFS).

    :param file_system: A dictionary representing the file system. 
                        Keys are folder names, and values are lists of subfolders or files.
    :param directory: The starting directory from which to list all files.
    :return: A list of all files found within the specified directory and its subdirectories.
    """

    files = []  # List to store the collected files

    def dfs(folder):
        """
        Helper function that performs a depth-first traversal of the file system.

        :param folder: The current directory being explored.
        """
        # If the current folder is not in the file system, it is a file, so add it to the list
        if folder not in file_system:
            files.append(folder)
            return

        # Recursively explore all subdirectories and files within the current folder
        for sub in file_system[folder]:
            dfs(sub)

    dfs(directory)  # Start DFS traversal from the given directory
    return files  # Return the collected list of files

# Example file system structure
file_system = {
    "root": ["folder1", "folder2"],        # "root" contains "folder1" and "folder2"
    "folder1": ["file1.txt", "folder3"],   # "folder1" contains a file and another folder
    "folder3": ["file2.txt"],              # "folder3" contains a file
    "folder2": ["file3.txt"]               # "folder2" contains a file
}

# Call the function and print the result
print(list_files(file_system, "root"))  # Output: ['file1.txt', 'file2.txt', 'file3.txt']

# Complexity Analysis:
# - Time Complexity: O(N)  (where N is the total number of files and folders in the file system)
# - Space Complexity: O(N) (due to recursive calls and storage of files in the list)


"""
 9. Airport Connection System (BFS)
 Problem Statement:
Given airports and their direct flight connections, find the shortest path from one airport to another.

 Example Input:
flights = {
    "JFK": ["LAX", "ATL"],
    "LAX": ["ORD"],
    "ATL": ["ORD", "MIA"],
    "ORD": ["MIA"],
    "MIA": []
}
start = "JFK"
end = "MIA"

 Expected Output:

['JFK', 'ATL', 'MIA']

"""
from collections import deque

from collections import deque

def shortest_flight_path(flights, start, end):
    """
    Finds the shortest flight path between two airports using Breadth-First Search (BFS).

    :param flights: A dictionary representing direct flight connections between airports.
                    Keys are airport codes, and values are lists of directly reachable airports.
    :param start: The starting airport.
    :param end: The destination airport.
    :return: A list representing the shortest path from start to end. If no path exists, returns an empty list.
    """

    queue = deque([(start, [start])])  # Queue stores (current airport, path taken)
    visited = set([start])  # Set to keep track of visited airports to avoid cycles

    while queue:
        airport, path = queue.popleft()  # Get the current airport and path taken so far
        
        # If we reach the destination airport, return the path
        if airport == end:
            return path

        # Explore all direct flight connections from the current airport
        for next_airport in flights.get(airport, []):
            if next_airport not in visited:
                queue.append((next_airport, path + [next_airport]))  # Add next airport to queue
                visited.add(next_airport)  # Mark it as visited

    return []  # Return an empty list if no path is found

# Example flight connections
flights = {
    "JFK": ["LAX", "ATL"],   # Flights from JFK to LAX and ATL
    "LAX": ["ORD"],          # Flight from LAX to ORD
    "ATL": ["ORD", "MIA"],   # Flights from ATL to ORD and MIA
    "ORD": ["MIA"],          # Flight from ORD to MIA
    "MIA": []                # No outbound flights from MIA
}

# Define the start and end airports
start = "JFK"
end = "MIA"

# Call the function and print the result
print(shortest_flight_path(flights, "JFK", "MIA"))  # Output: ['JFK', 'ATL', 'MIA']

# Complexity Analysis:
# - Time Complexity: O(N + E)  (where N is the number of airports and E is the number of direct flights)
# - Space Complexity: O(N) (for storing visited airports and the queue)


#  Complexity:
# - Time Complexity: O(V + E)
# - Space Complexity: O(V)


"""
 10. Word Ladder Transformation (BFS)
 Problem Statement:
Given two words and a dictionary, find the shortest transformation sequence from the start word to the end word such that only one 
letter can be changed at a time.

 Example Input:

start = "hit"
end = "cog"
dictionary = {"hot", "dot", "dog", "lot", "log", "cog"}

 Expected Output:

['hit', 'hot', 'dot', 'dog', 'cog']

"""
from collections import deque

def word_ladder(start, end, dictionary):
    """
    Finds the shortest transformation sequence from 'start' to 'end' by changing one letter at a time,
    ensuring that each intermediate word exists in the given dictionary.

    :param start: The starting word.
    :param end: The target word.
    :param dictionary: A set of valid words that can be used in the transformation.
    :return: A list representing the shortest transformation sequence. If no sequence exists, returns an empty list.
    """

    queue = deque([(start, [start])])  # Queue stores (current word, transformation path)
    dictionary.add(end)  # Ensure the end word is considered in the transformation

    while queue:
        word, path = queue.popleft()  # Get the current word and path taken so far
        
        # If we reach the target word, return the transformation path
        if word == end:
            return path

        # Try changing each letter in the word
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":  # Try all possible letters a-z
                new_word = word[:i] + c + word[i+1:]  # Generate a new word by replacing the character at index i
                
                if new_word in dictionary:  # Check if the new word is in the dictionary
                    queue.append((new_word, path + [new_word]))  # Add to queue with updated path
                    dictionary.remove(new_word)  # Remove to prevent revisiting

    return []  # Return an empty list if no transformation sequence is found

# Example usage
print(word_ladder("hit", "cog", {"hot", "dot", "dog", "lot", "log"}))  # Expected Output: ['hit', 'hot', 'dot', 'dog', 'cog']

# Complexity Analysis:
# - Time Complexity: O(N * 26^L), where N is the number of words in the dictionary and L is the length of each word.
# - Space Complexity: O(N), as we store words in the queue and dictionary.

"""
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
"""


from collections import deque

def recommend_products(purchases, product):
    """
    Finds related products that are frequently bought together with the given product.
    Uses BFS (Breadth-First Search) to explore product relationships.

    :param purchases: A dictionary where keys are product names and values are lists of related products.
    :param product: The product for which recommendations are needed.
    :return: A list of recommended products excluding the input product.
    """

    queue = deque([product])  # Initialize queue with the given product
    visited = set([product])  # Track visited products to avoid cycles
    recommendations = set()  # Store recommended products

    while queue:
        current = queue.popleft()  # Get the current product from the queue

        # Iterate through all related products
        for p in purchases.get(current, []):
            if p not in visited:  # Avoid revisiting products
                recommendations.add(p)  # Add to recommendations
                queue.append(p)  # Continue exploring related products
                visited.add(p)  # Mark as visited

    return list(recommendations)  # Convert set to list before returning

# Sample product purchase relationships
purchases = {
    "Laptop": ["Mouse", "Keyboard"],
    "Mouse": ["Laptop", "Headphones"],
    "Keyboard": ["Laptop", "Mouse"]
}
product = "Laptop"

# Get product recommendations
print(recommend_products(purchases, "Laptop"))  # Expected Output: ['Mouse', 'Keyboard', 'Headphones']

# Complexity Analysis:
# - Time Complexity: O(N), where N is the number of products in the dictionary.
# - Space Complexity: O(N), due to storing visited products and recommendations.


# Complexity:

# Time Complexity: O(V + E)

# Space Complexity: O(V)

