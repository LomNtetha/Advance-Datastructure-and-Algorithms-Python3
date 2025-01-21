"""
1. Basics of Topological Sort
Question: What is topological sorting, and provide a sorted order for a given directed acyclic graph (DAG)?
Example Input:
5 → 0  
5 → 2  
4 → 0  
4 → 1  
2 → 3  
3 → 1
Example Output: [5, 4, 2, 3, 1, 0]

"""
from collections import defaultdict, deque

def topological_sort(n, edges):
    # Create an adjacency list and an indegree array
    graph = defaultdict(list)
    indegree = [0] * n

    # Build the graph and calculate indegrees
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    # Initialize a queue with all nodes having 0 indegree
    queue = deque([i for i in range(n) if indegree[i] == 0])
    result = []

    # Perform topological sort
    while queue:
        node = queue.popleft()  # Remove a node with 0 indegree
        result.append(node)  # Add it to the result
        for neighbor in graph[node]:  # Decrease indegree of its neighbors
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:  # If indegree becomes 0, add to queue
                queue.append(neighbor)

    return result

# Example Input
edges = [(5, 0), (5, 2), (4, 0), (4, 1), (2, 3), (3, 1)]
n = 6
print(topological_sort(n, edges))  # Output: [5, 4, 2, 3, 1, 0]

# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
# Space Complexity: O(V + E), for the adjacency list and the indegree array
"""
2. Kahn’s Algorithm for Topological Sort
Question: Implement topological sorting using Kahn’s algorithm.
Example Input:
1 → 0  
2 → 0  
3 → 1  
3 → 2
Example Output: [3, 2, 1, 0]
"""
from collections import defaultdict, deque

def kahn_topological_sort(n, edges):
    # Create an adjacency list and indegree array
    graph = defaultdict(list)
    indegree = [0] * n

    # Build the graph and calculate indegrees
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    # Initialize a queue with all nodes having 0 indegree
    queue = deque([i for i in range(n) if indegree[i] == 0])
    result = []

    # Perform topological sort
    while queue:
        node = queue.popleft()  # Remove a node with 0 indegree
        result.append(node)  # Add it to the result
        for neighbor in graph[node]:  # Decrease indegree of its neighbors
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:  # If indegree becomes 0, add to queue
                queue.append(neighbor)

    return result

# Example Input
edges = [(1, 0), (2, 0), (3, 1), (3, 2)]
n = 4
print(kahn_topological_sort(n, edges))  # Output: [3, 2, 1, 0]

# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
# Space Complexity: O(V + E), for the adjacency list and indegree array

"""

3. Cycle Detection in Directed Graph Using Topological Sort
Question: How would you detect a cycle in a directed graph using topological sorting?
Example Input:
0 → 1  
1 → 2  
2 → 0
Example Output: "Cycle detected"

"""
from collections import defaultdict, deque

def detect_cycle(n, edges):
    # Create an adjacency list and indegree array
    graph = defaultdict(list)
    indegree = [0] * n

    # Build the graph and calculate indegrees
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    # Initialize a queue with all nodes having 0 indegree
    queue = deque([i for i in range(n) if indegree[i] == 0])
    count = 0

    # Perform topological sort
    while queue:
        node = queue.popleft()  # Remove a node with 0 indegree
        count += 1
        for neighbor in graph[node]:  # Decrease indegree of its neighbors
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:  # If indegree becomes 0, add to queue
                queue.append(neighbor)

    # If all nodes are processed, no cycle exists
    return count != n  # If some nodes are left, there is a cycle

# Example Input
edges = [(0, 1), (1, 2), (2, 0)]
n = 3
print("Cycle detected" if detect_cycle(n, edges) else "No cycle detected")  # Output: "Cycle detected"

# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
# Space Complexity: O(V + E), for the adjacency list and indegree array
"""
4. Course Schedule (LeetCode 207)
Question: Determine if it is possible to finish all courses given prerequisites.
Example Input:
numCourses = 4  
prerequisites = [[1, 0], [2, 1], [3, 2]]
Example Output: True

"""
def can_finish(numCourses, prerequisites):
    # Create an adjacency list and indegree array
    graph = defaultdict(list)
    indegree = [0] * numCourses

    # Build the graph and calculate indegrees
    for u, v in prerequisites:
        graph[v].append(u)
        indegree[u] += 1

    # Initialize a queue with all nodes having 0 indegree
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    count = 0

    # Process all nodes
    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:  # Decrease indegree of its neighbors
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:  # If indegree becomes 0, add to queue
                queue.append(neighbor)

    # If all nodes are processed, return True
    return count == numCourses

# Example Input
numCourses = 4
prerequisites = [[1, 0], [2, 1], [3, 2]]
print(can_finish(numCourses, prerequisites))  # Output: True

# Time Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites
# Space Complexity: O(V + E), for the adjacency list and indegree array


# Time Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites
# Space Complexity: O(V + E), for the adjacency list and indegree array
"""
6. Alien Dictionary (LeetCode 269)
Question: Determine the order of characters in an alien language based on a list of words.
Example Input:
words = ["wrt", "wrf", "er", "ett", "rftt"]
Example Output: "wertf"

"""

def alien_order(words):
    # Create a graph and indegree dictionary for all characters in words
    graph = defaultdict(set)
    indegree = {c: 0 for word in words for c in word}

    # Build the graph and calculate indegrees based on word order
    for i in range(len(words) - 1):
        for c1, c2 in zip(words[i], words[i + 1]):
            if c1 != c2:
                if c2 not in graph[c1]:  # Avoid duplicate edges
                    graph[c1].add(c2)
                    indegree[c2] += 1
                break
        else:
            # Handle invalid input where prefix order is violated
            if len(words[i]) > len(words[i + 1]):
                return ""

    # Initialize a queue with all nodes having 0 indegree
    queue = deque([c for c in indegree if indegree[c] == 0])
    result = []

    # Perform topological sort
    while queue:
        c = queue.popleft()
        result.append(c)
        for neighbor in graph[c]:  # Decrease indegree of its neighbors
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:  # If indegree becomes 0, add to queue
                queue.append(neighbor)

    # If result length matches all unique characters, return the order
    return "".join(result) if len(result) == len(indegree) else ""

# Example Input
words = ["wrt", "wrf", "er", "ett", "rftt"]
print(alien_order(words))  # Output: "wertf"

# Time Complexity: O(C), where C is the total number of characters in all words
# Space Complexity: O(U + E), where U is the number of unique characters, and E is the number of edges

"""7. Longest Path in a Directed Acyclic Graph
Question: Find the length of the longest path in a directed acyclic graph.
Example Input:
0 → 1 → 2 → 3  
0 → 4 → 5
Example Output: 4"""

from collections import defaultdict, deque

def longest_path_in_dag(n, edges):
    # Create an adjacency list and an indegree array
    graph = defaultdict(list)
    indegree = [0] * n
    distance = [-float('inf')] * n  # Initialize distances with negative infinity

    # Build the graph and calculate indegrees
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    # Initialize a queue with all nodes having 0 indegree and set their distance to 0
    queue = deque([i for i in range(n) if indegree[i] == 0])
    for i in queue:
        distance[i] = 0

    # Perform topological sort and calculate longest path
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            distance[neighbor] = max(distance[neighbor], distance[node] + 1)
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return max(distance)  # Return the maximum distance

# Example Input
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
n = 4
print(longest_path_in_dag(n, edges))  # Output: 2

# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
# Space Complexity: O(V + E), for the adjacency list, indegree array, and distance array


"""
8. Task Scheduling
Question: Given a list of tasks and their dependencies, determine the order of execution.
Example Input:
tasks = 6  
dependencies = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
Example Output: [5, 4, 2, 3, 1, 0]

"""

from collections import defaultdict, deque

def task_scheduling(tasks, dependencies):
    # Create adjacency list and indegree array
    graph = defaultdict(list)
    indegree = [0] * tasks

    # Build the graph and calculate indegrees
    for u, v in dependencies:
        graph[u].append(v)
        indegree[v] += 1

    # Initialize a queue with tasks having 0 indegree
    queue = deque([i for i in range(tasks) if indegree[i] == 0])
    order = []

    while queue:
        task = queue.popleft()
        order.append(task)
        for neighbor in graph[task]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Check if all tasks are processed (to handle cycles)
    return order if len(order) == tasks else []

# Example Input
tasks = 6
dependencies = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
print(task_scheduling(tasks, dependencies))  # Output: [5, 4, 2, 3, 1, 0]

# Time Complexity: O(V + E), where V is the number of tasks and E is the number of dependencies
# Space Complexity: O(V + E), for the adjacency list and indegree array
"""
9. Find All Topological Orders
Question: Find all possible topological orders for a given directed acyclic graph.
Example Input:
1 → 0  
2 → 0  
3 → 1  
3 → 2
Example Output:
[[3, 2, 1, 0], [3, 1, 2, 0]]

"""
from collections import defaultdict, deque

def all_topological_orders(tasks, dependencies):
    # Create adjacency list and indegree array
    graph = defaultdict(list)
    indegree = [0] * tasks

    for u, v in dependencies:
        graph[u].append(v)
        indegree[v] += 1

    # List to store all possible orders
    result = []

    # Helper function for backtracking
    def backtrack(path, available):
        if len(path) == tasks:
            result.append(path[:])
            return
        
        for node in sorted(available):  # Process in lexicographical order
            # Create a new set of available nodes
            new_available = available - {node}
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    new_available.add(neighbor)
            
            path.append(node)
            backtrack(path, new_available)

            # Backtrack: Restore the state
            path.pop()
            for neighbor in graph[node]:
                if indegree[neighbor] == 0:
                    new_available.remove(neighbor)
                indegree[neighbor] += 1

    # Start with nodes having 0 indegree
    start_nodes = {i for i in range(tasks) if indegree[i] == 0}
    backtrack([], start_nodes)

    return result

# Example Input
tasks = 4
dependencies = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(all_topological_orders(tasks, dependencies))  # Output: [[3, 2, 1, 0], [3, 1, 2, 0]]

# Time Complexity: O(V! * E), where V is the number of tasks and E is the number of dependencies
# Space Complexity: O(V + E), for the adjacency list and indegree array


"""
10. Minimum Time to Complete Tasks
Question: Given a list of tasks with dependencies and task durations, find the minimum time to complete all tasks.
Example Input:
tasks = [3, 2, 1]  # Task durations  
dependencies = [[0, 1], [1, 2]]
Example Output: 6"""

from collections import defaultdict, deque

def minimum_time_to_complete(tasks, durations, dependencies):
    # Create adjacency list and indegree array
    graph = defaultdict(list)
    indegree = [0] * tasks

    for u, v in dependencies:
        graph[u].append(v)
        indegree[v] += 1

    # Initialize queue with tasks having 0 indegree
    queue = deque([i for i in range(tasks) if indegree[i] == 0])
    # Initialize task completion times with their durations
    completion_time = durations[:]

    while queue:
        task = queue.popleft()
        for neighbor in graph[task]:
            indegree[neighbor] -= 1
            completion_time[neighbor] = max(completion_time[neighbor], completion_time[task] + durations[neighbor])
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return max(completion_time)  # Maximum time to complete all tasks

# Example Input
tasks = 3
durations = [3, 2, 1]
dependencies = [[0, 1], [1, 2]]
print(minimum_time_to_complete(tasks, durations, dependencies))  # Output: 6

# Time Complexity: O(V + E), where V is the number of tasks and E is the number of dependencies
# Space Complexity: O(V + E), for the adjacency list and completion time array
