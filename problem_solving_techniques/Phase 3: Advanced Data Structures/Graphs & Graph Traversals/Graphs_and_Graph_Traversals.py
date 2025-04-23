"""
1. Depth-First Search (DFS) on a Graph
Problem Statement:
You are given a directed graph represented as an adjacency list, where each key represents a node, and its corresponding
value is a list of nodes that it connects to. Your task is to implement the Depth-First Search (DFS) algorithm starting 
from a given node and return the order of traversal.

DFS is a graph traversal technique that explores as far as possible along each branch before backtracking. 
It can be implemented using recursion or an explicit stack.

Example Input:

graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: [3]
}
start = 0
Example Output:
[0, 1, 2, 3]
"""

class Solution:
    def dfs(self, graph, start):
        """
        Perform a Depth-First Search (DFS) on a graph starting from the given node.

        Args:
        - graph (dict): A dictionary representation of the graph where keys are nodes
          and values are lists of neighbors.
        - start (int): The starting node for the DFS traversal.

        Returns:
        - list: A list of nodes visited during the DFS traversal in the order they were visited.
        """
        visited = set()  # To track the visited nodes and prevent revisiting them
        result = []  # To store the order of nodes visited during the traversal

        def dfs_helper(node):
            """
            Helper function to perform DFS recursively.
            Args:
            - node (int): The current node being visited.
            """
            if node not in visited:  # Only process the node if it hasn't been visited yet
                visited.add(node)  # Mark the node as visited
                result.append(node)  # Add the node to the result list
                # Recursively visit all the neighbors of the current node
                for neighbor in graph.get(node, []):
                    dfs_helper(neighbor)  # Recursive call for the neighbor nodes

        dfs_helper(start)  # Start the DFS traversal from the 'start' node
        return result  # Return the list of nodes visited during DFS

# Example usage
sol = Solution()
# Define a graph as an adjacency list where keys are nodes and values are lists of neighbors
graph = {
    0: [1, 2],  # Node 0 is connected to nodes 1 and 2
    1: [2],     # Node 1 is connected to node 2
    2: [3],     # Node 2 is connected to node 3
    3: [3]      # Node 3 has a self-loop (connected to itself)
}
# Perform DFS starting from node 0
print(sol.dfs(graph, 0))  # Output: [0, 1, 2, 3]

# Final Complexity Summary
# Time Complexity: O(N+E)
# Space Complexity: O(N) (due to recursion and visited storage)




"""
2. Breadth-First Search (BFS) on a Graph
Problem Statement:
Given a graph represented as an adjacency list, perform BFS starting from a given node and return the order of traversal.

Example Input:
graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: [3]
}
start = 0
Example Output:
[0, 1, 2, 3]
Solution:
"""
from collections import deque  # Import deque for efficient queue operations

class Solution:
    def bfs(self, graph, start):
        """
        Perform a Breadth-First Search (BFS) on a graph starting from the given node.

        Args:
        - graph (dict): A dictionary representation of the graph where keys are nodes
          and values are lists of neighbors.
        - start (int): The starting node for the BFS traversal.

        Returns:
        - list: A list of nodes visited during the BFS traversal in the order they were visited.
        """
        visited = set()  # Set to track visited nodes and avoid revisiting them
        queue = deque([start])  # Queue to manage nodes to be processed; initialize with 'start'
        result = []  # List to store the order of nodes visited during BFS

        # While there are nodes to process in the queue
        while queue:
            node = queue.popleft()  # Remove the leftmost node from the queue
            if node not in visited:  # Process the node only if it hasn't been visited
                visited.add(node)  # Mark the node as visited
                result.append(node)  # Add the node to the result list
                # Iterate over neighbors of the current node
                for neighbor in graph.get(node, []):
                    if neighbor not in visited:  # If the neighbor hasn't been visited
                        queue.append(neighbor)  # Add the neighbor to the queue for future processing

        return result  # Return the order of nodes visited during BFS

# Example usage
sol = Solution()
# Define a graph as an adjacency list where keys are nodes and values are lists of neighbors
graph = {
    0: [1, 2],  # Node 0 is connected to nodes 1 and 2
    1: [2],     # Node 1 is connected to node 2
    2: [3],     # Node 2 is connected to node 3
    3: [3]      # Node 3 has a self-loop (connected to itself)
}
# Perform BFS starting from node 0
print(sol.bfs(graph, 0))  # Output: [0, 1, 2, 3]

# Final Complexity Summary
# Time Complexity: O(N+E)
# Space Complexity: O(N) (due to visited set and queue storage)



"""
3. Topological Sorting of a Directed Acyclic Graph (DAG)
Problem Statement:
Given a Directed Acyclic Graph (DAG) represented as an adjacency list, return one valid topological order of nodes.

Example Input:


graph = {
    5: [2, 0],
    4: [0, 1],
    2: [3],
    3: [1],
    0: [],
    1: []
}
Example Output:

[5, 4, 2, 3, 1, 0]
Solution:

"""

class Solution:
    def topological_sort(self, graph):
        """
        Perform a topological sort on a directed acyclic graph (DAG).

        Args:
        - graph (dict): A dictionary representation of the graph where keys are nodes
          and values are lists of neighboring nodes (edges).

        Returns:
        - list: A list of nodes in topologically sorted order.

        Raises:
        - TypeError: If graph is not a dictionary.
        - ValueError: If the graph contains a cycle.

        Example:
        >>> sol = Solution()
        >>> graph = {
            5: [2, 0],
            4: [0, 1],
            2: [3],
            3: [1],
            0: [],
            1: []
        }
        >>> sol.topological_sort(graph)
        [5, 4, 2, 3, 1, 0]
        """

        visited = set()
        result_stack = []
        recursion_stack = set()  # To detect cycles

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            recursion_stack.add(node)

            for neighbor in graph.get(node, []):
                dfs(neighbor)

            recursion_stack.remove(node)
            result_stack.append(node)

        # Process nodes in sorted order for deterministic output
        for node in sorted(graph.keys()):
            if node not in visited:
                dfs(node)

        return result_stack[::-1]


 
    graph = {
        5: [2, 0],
        4: [0, 1],
        2: [3],
        3: [1],
        0: [],
        1: []
    }

sol = Solution()
print(sol.topological_sort(graph))  # Output: [5, 4, 2, 3, 1, 0]

# Final Complexity Summary
# Time Complexity: O(N + E)  # Each node and edge is processed once
# Space Complexity: O(N)  # Due to recursion stack and visited storage



"""
4. Detect a Cycle in a Directed Graph
Problem Statement:
Determine if a directed graph contains a cycle.

Example Input:
graph = {
    0: [1],
    1: [2],
    2: [0]
}
Example Output:
True
Solution:

"""
class Solution:
    def has_cycle(self, graph):
        """
        Detect if a directed graph contains a cycle.

        Args:
        - graph (dict): A dictionary where keys are nodes and values are lists of neighbors.

        Returns:
        - bool: True if the graph contains a cycle, otherwise False.
        """
        visited = set()          # Set to keep track of all visited nodes
        recursion_stack = set()  # Set to track nodes in the current recursion path

        def dfs(node):
            """
            Perform a Depth-First Search (DFS) to detect cycles.

            Args:
            - node: The current node being explored.

            Returns:
            - bool: True if a cycle is detected, otherwise False.
            """
            # If the node is already in the recursion stack, a cycle is detected
            if node in recursion_stack:
                return True
            # If the node is already visited and not in the current path, no cycle from here
            if node in visited:
                return False

            # Mark the current node as visited and add it to the recursion stack
            visited.add(node)
            recursion_stack.add(node)

            # Explore all neighbors of the current node
            for neighbor in graph.get(node, []):
                if dfs(neighbor):  # If any neighbor leads to a cycle, return True
                    return True

            # Remove the node from the recursion stack once all its neighbors are processed
            recursion_stack.remove(node)
            return False

        # Perform DFS from each node in the graph
        for node in graph:
            if dfs(node):  # If any component has a cycle, return True
                return True

        # If no cycles are found, return False
        return False

# Example usage
sol = Solution()
# Define a graph with a cycle (0 -> 1 -> 2 -> 0)
graph = {0: [1], 1: [2], 2: [0]}
print(sol.has_cycle(graph))  # Output: True

# Final Complexity Summary
# Time Complexity: O(N + E)  # Each node and edge is processed once in DFS
# Space Complexity: O(N)  # Due to recursion stack, visited, and recursion_stack storage



"""
Question:
You are developing a text-based adventure game where players navigate through a series of interconnected rooms. Each room is represented
as a node in a graph, and the connections between the rooms are represented as edges in the graph. Players can move from one room to another
if there is a direct connection between them.

Your task is to implement a function that finds the shortest path between two rooms using the Breadth-First Search (BFS) algorithm.

Requirements:
Represent the graph as an adjacency list.
Write a function find_shortest_path(start, end) that:
Takes the starting room start and the destination room end.
Returns a list of rooms representing the shortest path from start to end. If no path exists, return None.
Ensure the function handles edge cases such as:
The starting room or destination room does not exist.
No path exists between the two rooms.
Constraints:
The graph is unweighted (all edges have the same "cost").
The graph is undirected (connections work both ways).
The graph is connected (all rooms are reachable) or may have some isolated components.
Example:
Graph Structure:
The game map is represented as follows:

Rooms: "Entrance", "Hallway", "Kitchen", "Living Room", "Bedroom".

Connections:
Entrance ↔ Hallway
Hallway ↔ Kitchen
Kitchen ↔ Living Room
Living Room ↔ Bedroom

Input:
start = "Entrance"
end = "Bedroom"

Output:
['Entrance', 'Hallway', 'Kitchen', 'Living Room', 'Bedroom']
Explanation:
The shortest path from "Entrance" to "Bedroom" passes through all intermediate rooms in the order shown.

"""
from collections import deque

class Solution:
    def bfs_shortest_path(self, graph, start, end):
          # Check if both start and end rooms exist in the graph
        if start not in graph or end not in graph:
            return []  # Return empty list if start or end node is not in the graph
        
        queue = deque([(start, [start])])  # Queue stores (current_node, path_to_node)
        visited = set()  # Set to track visited nodes | Set to keep track of visited rooms to prevent cycles
        
        while queue:
            node, path = queue.popleft()  # Dequeue the first element
            
            if node == end:
                return path  # Return path when we reach the end node
            # If the room has not been visited, process its neighbors
            if node not in visited:
                visited.add(node)  # Mark node as visited | # Mark the room as visited
                
                for neighbor in graph.get(node, []):# Loop through adjacent rooms
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))  # Append new path
        
        return []  # Return empty list if no path is found

# Example usage
sol = Solution()
graph = {
    "Entrance": ["Hallway"],
    "Hallway": ["Entrance", "Kitchen"],
    "Kitchen": ["Hallway", "Living Room"],
    "Living Room": ["Kitchen", "Bedroom"],
    "Bedroom": ["Living Room"]
}

# Find shortest path from "Entrance" to "Bedroom"
start = "Entrance"
end = "Bedroom"
print(sol.bfs_shortest_path(graph, start, end))

# Final Complexity Summary
# Time Complexity: O(N + E)  # Each node and edge is processed once in BFS
# Space Complexity: O(N)  # Due to queue and visited storage



"""
5. Find the Shortest Path Using Dijkstra's Algorithm
Problem Statement:
Given a graph represented as an adjacency list with edge weights and a starting node, find the shortest distance to all nodes
using Dijkstra's algorithm.

Example Input:
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
start = 0
Example Output:

{0: 0, 1: 3, 2: 1, 3: 4}
Solution:
"""

import heapq  # Importing the heapq module for priority queue operations

class Solution:
    def dijkstra(self, graph, start):
        """
        Find the shortest distances from the start node to all other nodes in a graph using Dijkstra's algorithm.

        Args:
        - graph (dict): A dictionary where keys are nodes and values are lists of tuples (neighbor, weight).
        - start (int): The starting node for Dijkstra's algorithm.

        Returns:
        - distances (dict): A dictionary where keys are nodes and values are the shortest distances from the start node.
        """

        # Initialize distances to all nodes as infinity
        distances = {node: float('inf') for node in graph}
        distances[start] = 0  # Distance to the start node is 0

        # Priority queue to process nodes by the shortest known distance first
        pq = [(0, start)]  # Each element is a tuple (distance, node)

        # Process the priority queue until all reachable nodes are visited
        while pq:
            # Pop the node with the smallest distance from the queue
            curr_distance, curr_node = heapq.heappop(pq)

            # If the current distance is greater than the recorded shortest distance, skip
            if curr_distance > distances[curr_node]:
                continue

            # Iterate over neighbors of the current node
            for neighbor, weight in graph.get(curr_node, []):
                # Calculate the distance to the neighbor through the current node
                distance = curr_distance + weight

                # If this path is shorter, update the distance and add it to the queue
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        # Return the dictionary containing shortest distances to all nodes
        return distances

# Example usage
sol = Solution()
# Define a weighted graph as an adjacency list
# For example, graph[0] contains (1, 4) and (2, 1) meaning:
# There is an edge from 0 to 1 with weight 4, and an edge from 0 to 2 with weight 1.
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

# Compute shortest paths from node 0
print(sol.dijkstra(graph, 0))  # Output: {0: 0, 1: 3, 2: 1, 3: 4}

# Final Complexity Summary
# Time Complexity: O((N + E) log N)  # Priority queue operations dominate the complexity
# Space Complexity: O(N + E)  # Storing distances and priority queue data



    
"""
6. Find the Shortest Path Using Bellman-Ford Algorithm
Problem Statement:
Given a directed graph with weighted edges, find the shortest path from a source node to all other nodes. The graph may contain negative weights,
but no negative weight cycles.

Example Input:
edges = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5)]
num_vertices = 4
source = 0
Example Output:
[0, 3, 1, 4]
Solution:

"""
class Solution:
    def bellman_ford(self, edges, num_vertices, source):
        """
        Implements the Bellman-Ford algorithm to find the shortest path from a single source to all other vertices.

        Args:
        - edges (list): A list of tuples (u, v, weight) where u is the starting vertex,
                        v is the ending vertex, and weight is the cost of the edge.
        - num_vertices (int): The number of vertices in the graph.
        - source (int): The source vertex from which to calculate shortest distances.

        Returns:
        - distances (list or str): A list of shortest distances from the source to each vertex,
                                   or a message if a negative weight cycle is detected.
        """

        # Step 1: Initialize distances to all vertices as infinity
        # The distance to the source vertex is set to 0
        distances = [float('inf')] * num_vertices
        distances[source] = 0

        # Step 2: Relax all edges num_vertices - 1 times
        # This ensures that the shortest paths (in terms of the number of edges) are considered
        for _ in range(num_vertices - 1):
            for u, v, weight in edges:
                # If the distance to u plus the weight of the edge (u, v) is less than the distance to v, update it
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

        # Step 3: Check for negative weight cycles
        # If we can still relax any edge, it indicates a negative weight cycle
        for u, v, weight in edges:
            if distances[u] + weight < distances[v]:
                return "Graph contains a negative weight cycle"

        # Return the computed shortest distances
        return distances

# Example usage
sol = Solution()

# Define a graph as a list of edges
# Each edge is represented as a tuple (u, v, weight)
edges = [
    (0, 1, 4),  # Edge from vertex 0 to vertex 1 with weight 4
    (0, 2, 1),  # Edge from vertex 0 to vertex 2 with weight 1
    (2, 1, 2),  # Edge from vertex 2 to vertex 1 with weight 2
    (1, 3, 1),  # Edge from vertex 1 to vertex 3 with weight 1
    (2, 3, 5)   # Edge from vertex 2 to vertex 3 with weight 5
]

num_vertices = 4  # Total number of vertices in the graph
source = 0        # Starting vertex

# Print the result of running Bellman-Ford algorithm
print(sol.bellman_ford(edges, num_vertices, source))

# Final Complexity Summary
# Time Complexity: O(V * E) # The algorithm relaxes all edges V-1 times, and for each relaxation, all edges are checked.

# Space Complexity: O(V) # Storing the distances for each vertex.



"""
7. Find All Paths From a Source to a Destination in a Graph
Problem Statement:
Given a directed graph, find all possible paths from a source node to a destination node.

Example Input:
graph = {
    0: [1, 2],
    1: [2, 3],
    2: [3],
    3: []
}
source = 0
destination = 3
Example Output:

[[0, 1, 3], [0, 2, 3], [0, 1, 2, 3]]
Solution:
"""
class Solution:
    def find_all_paths(self, graph, source, destination):
        """
        Finds all possible paths from the source node to the destination node in a directed graph.

        Args:
        - graph (dict): A dictionary where keys are nodes and values are lists of neighbors.
        - source (int): The starting node.
        - destination (int): The target node.

        Returns:
        - result (list): A list of all paths from source to destination. Each path is represented as a list of nodes.
        """
        # Initialize the result list to store all paths
        result = []

        def dfs(current, path):
            """
            Depth-first search helper function to explore all paths from the current node to the destination.

            Args:
            - current (int): The current node being visited.
            - path (list): The path taken to reach the current node.

            Adds complete paths to the result list when the destination is reached.
            """
            # Base case: If the current node is the destination, add the path to the result
            if current == destination:
                result.append(path[:])  # Append a copy of the current path
                return

            # Explore neighbors of the current node
            for neighbor in graph.get(current, []):
                # Add the neighbor to the path
                path.append(neighbor)
                # Recursively visit the neighbor
                dfs(neighbor, path)
                # Backtrack: remove the neighbor from the path
                path.pop()

        
        # Start DFS from the source node, initializing the path with the source
        dfs(source, [source])
        return result

# Example usage
sol = Solution()

# Define a graph as a dictionary where keys are nodes and values are lists of neighbors
graph = {
    0: [1, 2],  # Node 0 has neighbors 1 and 2
    1: [2, 3],  # Node 1 has neighbors 2 and 3
    2: [3],     # Node 2 has neighbor 3
    3: []       # Node 3 has no neighbors
}

# Find all paths from node 0 to node 3
print(sol.find_all_paths(graph, 0, 3))

# Final Complexity Summary
# Time Complexity: O(2^V) # In the worst case, each node can have two choices (if branching factor is large), leading to exponential growth in 
# the number of paths.

# Space Complexity: O(V) # The depth of the recursion tree and the maximum path length can go up to the number of vertices.

"""
8. Check if a Graph is Bipartite
Problem Statement:
Determine if a graph is bipartite (i.e., can its vertices be divided into two disjoint sets such that no vertices
within the same set are adjacent).

Example Input:
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}
Example Output:
True
"""


class Solution:
    def is_bipartite(self, graph):
        """
        Determines if a graph is bipartite.

        A graph is bipartite if its vertices can be divided into two disjoint sets such that 
        no two adjacent vertices are in the same set.

        Args:
        - graph (dict): An adjacency list representation of the graph. 
                        Keys are nodes, and values are lists of adjacent nodes.

        Returns:
        - bool: True if the graph is bipartite, False otherwise.
        """

        # Dictionary to store the color assigned to each node (0 or 1)
        colors = {}

        def dfs(node, color):
            """
            Performs depth-first search (DFS) to try coloring the graph.

            Args:
            - node (int): The current node being visited.
            - color (int): The color to assign to the current node.

            Returns:
            - bool: True if the graph is bipartite up to this point, False otherwise.
            """
            # If the node has already been colored, check if the color is consistent
            if node in colors:
                return colors[node] == color

            # Assign the current node the specified color
            colors[node] = color

            # Visit all neighbors of the current node
            for neighbor in graph.get(node, []):
                # Recursively attempt to color the neighbor with the opposite color
                if not dfs(neighbor, 1 - color):  # Flip color (0 -> 1, 1 -> 0)
                    return False

            return True  # If all neighbors are colored successfully, return True

        # Check each component of the graph
        for node in graph:
            # If the node has not been visited, start a new DFS from it
            if node not in colors:
                if not dfs(node, 0):  # Start coloring with color 0
                    return False  # If any component fails, the graph is not bipartite

        return True  # All components are bipartite

# Example usage
sol = Solution()

# Example graph represented as an adjacency list
graph = {
    0: [1, 3],  # Node 0 is connected to nodes 1 and 3
    1: [0, 2],  # Node 1 is connected to nodes 0 and 2
    2: [1, 3],  # Node 2 is connected to nodes 1 and 3
    3: [0, 2]   # Node 3 is connected to nodes 0 and 2
}

# Determine if the graph is bipartite
print(sol.is_bipartite(graph))  # Output: True

# Final Complexity Summary
# Time Complexity: O(V + E) # The algorithm visits each node once (O(V)) and explores each edge once (O(E)) during the DFS traversal.

# Space Complexity: O(V) # The space complexity is dominated by the storage of the colors dictionary, which stores the color of each vertex. The depth of the recursion 
# stack is also O(V) in the worst case.



"""
9. Count Connected Components in an Undirected Graph
Problem Statement:
Given an undirected graph, count the number of connected components.

Example Input:
graph = {
    0: [1],
    1: [0],
    2: [3],
    3: [2],
    4: []
}
Example Output:
3
"""
class Solution:
    def count_connected_components(self, graph):
        """
        Counts the number of connected components in an undirected graph.

        A connected component is a subset of nodes such that there is a path between any 
        two nodes in the subset, and the subset is not connected to any other nodes in the graph.

        Args:
        - graph (dict): An adjacency list representation of the graph. 
                        Keys are nodes, and values are lists of adjacent nodes.

        Returns:
        - int: The number of connected components in the graph.
        """

        # Set to keep track of all visited nodes
        visited = set()
        # Counter to keep track of the number of connected components
        count = 0

        def dfs(node):
            """
            Depth-First Search (DFS) to traverse and mark all nodes in the current component.

            Args:
            - node (int): The current node being visited.

            Returns:
            - None
            """
            # If the node is already visited, do nothing
            if node in visited:
                return

            # Mark the current node as visited
            visited.add(node)

            # Visit all unvisited neighbors of the current node
            for neighbor in graph.get(node, []):
                dfs(neighbor)

        # Iterate through all nodes in the graph
        for node in graph:
            # If the node is not visited, it starts a new connected component
            if node not in visited:
                count += 1  # Increment the connected component counter
                dfs(node)   # Perform DFS to mark all nodes in this component

        return count  # Return the total number of connected components


# Example usage
sol = Solution()

# Example graph represented as an adjacency list
graph = {
    0: [1],  # Node 0 is connected to node 1
    1: [0],  # Node 1 is connected back to node 0 (forms one connected component with node 0)
    2: [3],  # Node 2 is connected to node 3
    3: [2],  # Node 3 is connected back to node 2 (forms another connected component with node 2)
    4: []    # Node 4 is isolated (forms its own connected component)
}

# Calculate and print the number of connected components in the graph
print(sol.count_connected_components(graph))  # Output: 3

# Final Complexity Summary
# Time Complexity: O(V + E) # Each node is visited once (O(V)), and each edge is examined once (O(E)) during the DFS traversal.

# Space Complexity: O(V) # The space complexity is dominated by the storage of the visited set, which tracks the visited nodes, 
# and the recursion stack during DFS, which can be O(V) in the worst case.

"""

10. Minimum Spanning Tree (Prim's Algorithm)
Problem Statement:
Given a connected, undirected graph represented as an adjacency list with edge weights, find the Minimum Spanning Tree (MST) using Prim's algorithm.

Example Input:

graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8)],
    2: [(1, 3), (3, 7)],
    3: [(0, 6), (1, 8), (2, 7)]
}
Example Output:

[(0, 1, 2), (1, 2, 3), (0, 3, 6)]
"""

import heapq

class Solution:
    def prims_mst(self, graph):
        """
        Implements Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph.

        Prim's algorithm starts from an arbitrary node and grows the MST by adding the 
        smallest edge that connects a visited node to an unvisited node.

        Args:
        - graph (dict): An adjacency list where keys are nodes and values are lists of tuples.
                        Each tuple represents a neighbor and the weight of the edge.

        Returns:
        - mst (list): A list of tuples representing the edges of the MST.
                      Each tuple is (parent_node, current_node, edge_weight).
        """

        # Set to keep track of visited nodes to avoid cycles
        visited = set()

        # List to store the edges of the resulting MST
        mst = []

        # Min-heap to prioritize edges with the smallest weights
        # Start with an arbitrary node (node 0) with cost 0 and no parent (-1)
        min_heap = [(0, 0, -1)]  # (cost, current_node, parent_node)

        # Process the nodes until the heap is empty
        while min_heap:
            # Extract the edge with the smallest cost
            cost, node, parent = heapq.heappop(min_heap)

            # If the node has already been visited, skip it
            if node in visited:
                continue

            # Mark the node as visited
            visited.add(node)

            # If the node has a valid parent, add the edge to the MST
            if parent != -1:
                mst.append((parent, node, cost))

            # Explore all neighbors of the current node
            for neighbor, weight in graph.get(node, []):
                # If the neighbor is unvisited, add it to the heap
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor, node))

        return mst


# Example usage
sol = Solution()

# Graph represented as an adjacency list
# Each key is a node, and its value is a list of tuples (neighbor, weight)
graph = {
    0: [(1, 2), (3, 6)],  # Node 0 is connected to node 1 with weight 2, and node 3 with weight 6
    1: [(0, 2), (2, 3), (3, 8)],  # Node 1 connections
    2: [(1, 3), (3, 7)],          # Node 2 connections
    3: [(0, 6), (1, 8), (2, 7)]   # Node 3 connections
}

# Find the MST and print it
print(sol.prims_mst(graph))

# Final Complexity Analysis
# Time Complexity: O(E * log V)

# Heap Operations: Each node is added and removed from the heap, resulting in O(V * log V) operations.

# Edge Relaxation: Each edge is processed once, and for each edge, we perform a heap push operation (O(log V)), 
# resulting in O(E * log V) for all edges.

# Therefore, the overall time complexity is O(E * log V), where E is the number of edges and V is the number of vertices in the graph.

# Space Complexity: O(V + E)

# Visited Set: O(V) for tracking visited nodes.

# Heap: O(V) for storing nodes and edges in the heap.

# MST List: O(E) for storing the resulting MST edges.

# The space complexity is dominated by the storage of these data structures, so it is O(V + E).

"""

11. Detect a Cycle in an Undirected Graph Using Union-Find
Problem Statement:
Given an undirected graph, determine if it contains any cycles.

Example Input:
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
num_vertices = 4
Example Output:
True
"""
class Solution:
    def find(self, parent, node):
        """
        A helper function to find the root of a given node with path compression.
        Path compression helps to flatten the structure of the tree, making future lookups faster.

        Args:
        - parent (list): The parent array where each index represents a node, and the value at that index is the node's parent.
        - node (int): The node for which the root is being found.

        Returns:
        - (int): The root of the given node.
        """
        # If the node is not its own parent, recursively find its root
        if parent[node] != node:
            parent[node] = self.find(parent, parent[node])  # Path compression
        return parent[node]

    def union(self, parent, rank, node1, node2):
        """
        Union by rank - this function unites two sets (represented by node1 and node2).
        The set with the higher rank (tree depth) will become the parent of the set with the lower rank,
        helping to keep the tree flatter and optimizing future find operations.

        Args:
        - parent (list): The parent array.
        - rank (list): The rank array where each index represents the "height" of the tree.
        - node1 (int): The first node to unite.
        - node2 (int): The second node to unite.

        Returns:
        - (bool): Returns False if no cycle is detected (i.e., the nodes were not connected), True if a cycle is detected.
        """
        # Find the roots of both nodes
        root1 = self.find(parent, node1)
        root2 = self.find(parent, node2)

        # If the roots are different, no cycle, so we unite the sets
        if root1 != root2:
            # Union by rank: attach the smaller tree under the root of the larger tree
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1  # Increase the rank if both trees have the same rank
            return False  # No cycle formed
        return True  # A cycle is detected since both nodes have the same root

    def has_cycle(self, edges, num_vertices):
        """
        Determines if the graph, represented by the edges, contains a cycle.
        Uses Union-Find with path compression and union by rank to check for cycles efficiently.

        Args:
        - edges (list of tuples): Each tuple represents an edge between two nodes (u, v).
        - num_vertices (int): The total number of vertices in the graph.

        Returns:
        - (bool): Returns True if a cycle is detected, False otherwise.
        """
        # Initialize parent and rank arrays
        parent = [i for i in range(num_vertices)]  # Each node is its own parent initially
        rank = [0] * num_vertices  # Initially, all nodes have rank 0

        # Iterate over all edges
        for u, v in edges:
            # Try to unite the two nodes; if they are already in the same set, a cycle is found
            if self.union(parent, rank, u, v):
                return True  # Cycle detected
        return False  # No cycle detected after processing all edges

# Example usage
sol = Solution()
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]  # A graph with a cycle
num_vertices = 4
print(sol.has_cycle(edges, num_vertices))  # Output: True


"""
12. Detect a Cycle in a Directed Graph Using DFS
Problem Statement:
Given a directed graph, determine if it contains any cycles.

Example Input:
graph = {
    0: [1],
    1: [2],
    2: [0]
}
Example Output:
True
Solution:
"""
class Solution:
    def detect_cycle_dfs(self, graph):
        """
        This function detects if there is a cycle in a directed graph using Depth-First Search (DFS).
        The approach uses two sets:
        - visited: Keeps track of all nodes that have been fully explored.
        - recursion_stack: Keeps track of the nodes that are currently being explored (part of the current path).

        Args:
        - graph (dict): The graph represented as an adjacency list, where keys are nodes and values are lists of neighboring nodes.

        Returns:
        - (bool): Returns True if a cycle is detected, False otherwise.
        """
        visited = set()  # Set to track all nodes that are completely visited.
        recursion_stack = set()  # Set to track nodes in the current DFS path.

        def dfs(node):
            """
            This helper function performs a DFS from the given node to detect cycles.
            - If the node is already in the recursion_stack, it means we have encountered a cycle.
            - If the node is already fully visited (i.e., in the visited set), then it’s safe to skip it.
            
            Args:
            - node (int): The current node being explored.

            Returns:
            - (bool): Returns True if a cycle is detected, False otherwise.
            """
            # If node is in recursion_stack, it means we've encountered a cycle
            if node in recursion_stack:
                return True
            # If node has been visited fully, no cycle from this node
            if node in visited:
                return False

            # Mark the current node as visited and part of the recursion stack
            visited.add(node)
            recursion_stack.add(node)
            
            # Explore all neighbors of the current node
            for neighbor in graph.get(node, []):
                # If any neighbor leads to a cycle, return True
                if dfs(neighbor):
                    return True
            
            # After exploring all neighbors, remove the node from recursion_stack
            recursion_stack.remove(node)
            return False

        # Perform DFS from all nodes in the graph to detect cycles
        for node in graph:
            if node not in visited:
                # If DFS from this node finds a cycle, return True
                if dfs(node):
                    return True
        # If no cycles are found after exploring all nodes
        return False

# Example usage:
sol = Solution()
graph = {0: [1], 1: [2], 2: [0]}  # This graph contains a cycle (0 -> 1 -> 2 -> 0)
print(sol.detect_cycle_dfs(graph))  # Output: True

"""

13. Kruskal's Algorithm for Minimum Spanning Tree
Problem Statement:
Given an undirected graph with weighted edges, find its Minimum Spanning Tree using Kruskal’s algorithm.

Example Input:
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
num_vertices = 4
Example Output:
[(2, 3, 4), (0, 3, 5), (0, 1, 10)]
"""

class Solution:
    def find(self, parent, node):
        """
        This function implements the 'find' operation of the union-find (disjoint-set) data structure.
        It helps to find the representative (root) of the set to which the node belongs. 
        The function uses path compression to optimize future queries.

        Args:
        - parent (list): A list where each element represents the parent of the node.
        - node (int): The node whose set representative is to be found.

        Returns:
        - (int): The root of the set containing the node.
        """
        if parent[node] != node:
            # Path compression: recursively find the root and make it the direct parent of all intermediate nodes.
            parent[node] = self.find(parent, parent[node])
        return parent[node]

    def union(self, parent, rank, node1, node2):
        """
        This function implements the 'union' operation of the union-find (disjoint-set) data structure.
        It merges the sets containing node1 and node2. The set with the higher rank is made the parent 
        of the set with the lower rank to maintain a balanced tree structure.

        Args:
        - parent (list): A list where each element represents the parent of the node.
        - rank (list): A list where each element represents the rank (or depth) of the tree for each node.
        - node1 (int): The first node to be unioned.
        - node2 (int): The second node to be unioned.
        """
        # Find the root of both nodes
        root1 = self.find(parent, node1)
        root2 = self.find(parent, node2)

        # If the roots are different, we perform union
        if root1 != root2:
            # Union by rank: attach the smaller tree under the larger tree (higher rank)
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                # If ranks are equal, make one root the parent of the other and increase its rank
                parent[root2] = root1
                rank[root1] += 1

    def kruskal_mst(self, edges, num_vertices):
        """
        This function implements Kruskal's algorithm to find the Minimum Spanning Tree (MST) of a graph.
        It uses the union-find data structure to efficiently detect cycles while adding edges to the MST.

        Args:
        - edges (list of tuples): A list of edges where each edge is represented as a tuple (u, v, weight)
                                  indicating an edge between nodes u and v with the given weight.
        - num_vertices (int): The number of vertices in the graph.

        Returns:
        - (list of tuples): A list of edges that form the MST, each represented as a tuple (u, v, weight).
        """
        # Sort edges in increasing order of weight
        edges.sort(key=lambda x: x[2])

        # Initialize the parent and rank arrays for the union-find structure
        parent = [i for i in range(num_vertices)]
        rank = [0] * num_vertices
        mst = []  # This will store the edges in the MST

        # Iterate over the sorted edges
        for u, v, weight in edges:
            # If u and v belong to different sets, add this edge to the MST
            if self.find(parent, u) != self.find(parent, v):
                self.union(parent, rank, u, v)
                mst.append((u, v, weight))

        # Return the MST
        return mst

# Example usage:
sol = Solution()
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
num_vertices = 4
print(sol.kruskal_mst(edges, num_vertices))  


"""
14. Count the Number of Islands in a 2D Grid
Problem Statement:
Given a 2D grid representing water (0) and land (1), count the number of islands. An island is surrounded by water and connected horizontally
or vertically.

Example Input:
grid = [
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]
Example Output:
3
"""
class Solution:
    def num_islands(self, grid):
        """
        This function counts the number of islands in a grid. 
        An island is surrounded by water and is formed by 1s connected 
        horizontally or vertically. This problem can be solved using depth-first search (DFS).

        Args:
        - grid (list of list of ints): A 2D grid where 1 represents land and 0 represents water.

        Returns:
        - (int): The number of islands in the grid.
        """

        def dfs(x, y):
            """
            This helper function performs a depth-first search to mark all connected land cells (1) 
            as visited by setting them to 0. It checks all four possible directions (up, down, left, right).
            
            Args:
            - x (int): The current row index in the grid.
            - y (int): The current column index in the grid.
            """
            # Base case: if the current position is out of bounds or is water (0), return immediately.
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
                return
            # Mark the current cell as visited (change land to water).
            grid[x][y] = 0
            # Explore all four possible directions from the current cell.
            dfs(x + 1, y)  # Explore downwards
            dfs(x - 1, y)  # Explore upwards
            dfs(x, y + 1)  # Explore right
            dfs(x, y - 1)  # Explore left

        # Initialize the island count.
        count = 0
        # Traverse the entire grid to find unvisited land (1).
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If the cell contains land (1), it means we have found a new island.
                if grid[i][j] == 1:
                    count += 1  # Increment island count
                    # Perform DFS to mark the entire island as visited.
                    dfs(i, j)
        # Return the total number of islands found.
        return count

# Example usage:
sol = Solution()
grid = [
    [1, 1, 0, 0],  # First island
    [1, 1, 0, 0],  # First island continues
    [0, 0, 1, 0],  # Second island
    [0, 0, 0, 1]   # Third island
]
print(sol.num_islands(grid))  # Output: 3


"""
15. Floyd-Warshall Algorithm for All-Pairs Shortest Paths
Problem Statement:
Given a graph represented as an adjacency matrix, compute the shortest distances between all pairs of nodes using the Floyd-Warshall algorithm.
If a node is unreachable, return inf for that pair.

Example Input:

graph = [
    [0, 3, inf, inf],
    [inf, 0, 1, inf],
    [inf, inf, 0, 2],
    [4, inf, inf, 0]
]
Example Output:

[
    [0, 3, 4, 6],
    [inf, 0, 1, 3],
    [inf, inf, 0, 2],
    [4, 7, 8, 0]
]
"""
class Solution:
    def floyd_warshall(self, graph):
        """
        This function implements the Floyd-Warshall algorithm to find the shortest paths
        between all pairs of vertices in a weighted graph. It updates the distance matrix
        with the shortest path distances.

        Args:
        - graph (list of list of ints): A 2D list representing the adjacency matrix of a graph.
          A value of 'inf' represents that there is no direct edge between the corresponding nodes.

        Returns:
        - (list of list of ints): The updated distance matrix containing the shortest distances 
          between all pairs of vertices.
        """

        # Get the number of vertices in the graph.
        num_vertices = len(graph)

        # Create a copy of the graph to store distances.
        dist = [row[:] for row in graph]  # Create a deep copy of the graph

        # Main Floyd-Warshall algorithm.
        # Three nested loops are used to iterate over all pairs of vertices.
        for k in range(num_vertices):  # Iterate through each vertex as an intermediate vertex.
            for i in range(num_vertices):  # Iterate through each source vertex.
                for j in range(num_vertices):  # Iterate through each destination vertex.
                    # If a shorter path is found by going through vertex 'k', update the distance.
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Return the distance matrix after applying the Floyd-Warshall algorithm.
        return dist

# Example usage:
inf = float('inf')  # Representation for no path (infinity).
sol = Solution()

# Adjacency matrix representing the graph.
graph = [
    [0, 3, inf, inf],  # Vertex 0 is connected to vertex 1 with weight 3.
    [inf, 0, 1, inf],  # Vertex 1 is connected to vertex 2 with weight 1.
    [inf, inf, 0, 2],  # Vertex 2 is connected to vertex 3 with weight 2.
    [4, inf, inf, 0]   # Vertex 3 is connected to vertex 0 with weight 4.
]

# Applying Floyd-Warshall to find all pairs shortest paths.
print(sol.floyd_warshall(graph))


"""
16. Bellman-Ford Algorithm for Single Source Shortest Path
Problem Statement:
Given a weighted graph and a starting node, compute the shortest path from the start to all other nodes using the Bellman-Ford algorithm.
Detect negative weight cycles.

Example Input:
edges = [(0, 1, 4), (0, 2, 5), (1, 2, -2), (2, 3, 3)]
num_vertices = 4
start = 0
Example Output:
[0, 4, 2, 5]
"""
class Solution:
    def bellman_ford(self, edges, num_vertices, start):
        """
        This function implements the Bellman-Ford algorithm to find the shortest paths from a 
        single source vertex to all other vertices in a weighted graph. It also detects if the 
        graph contains a negative weight cycle.

        Args:
        - edges (list of tuples): A list of edges represented by tuples (u, v, weight), where
          u is the source vertex, v is the destination vertex, and weight is the edge weight.
        - num_vertices (int): The number of vertices in the graph.
        - start (int): The starting vertex for the shortest path computation.

        Returns:
        - (list of ints or str): A list of shortest path distances from the start vertex to 
          all other vertices. If a negative weight cycle is detected, returns an error message.
        """
        
        # Step 1: Initialize distances
        # Set the distance to the start vertex as 0 and all others as infinity
        dist = [float('inf')] * num_vertices
        dist[start] = 0

        # Step 2: Relax edges repeatedly
        # Repeat this process num_vertices - 1 times
        # Each time, update the shortest distance for each vertex by checking the edges
        for _ in range(num_vertices - 1):
            for u, v, weight in edges:
                # If the distance to u is not infinity (i.e., u is reachable)
                # and we find a shorter path to v via u, update dist[v]
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        # Step 3: Check for negative weight cycles
        # If we can still relax an edge, it means a negative weight cycle exists
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                return "Graph contains a negative weight cycle"
        
        # Step 4: Return the shortest path distances from the start vertex to all vertices
        return dist

# Example usage:
sol = Solution()
edges = [(0, 1, 4), (0, 2, 5), (1, 2, -2), (2, 3, 3)]  # Define graph edges with weights
num_vertices = 4  # Number of vertices in the graph
start = 0  # Start from vertex 0

# Call the Bellman-Ford algorithm and print the result
print(sol.bellman_ford(edges, num_vertices, start))



"""
17. A Pathfinding Algorithm*
Problem Statement:
Given a weighted graph and a heuristic function, find the shortest path from a start node to a target node using the A* algorithm.

Example Input:
graph = {0: [(1, 1), (2, 4)], 1: [(2, 2), (3, 5)], 2: [(3, 1)]}
heuristic = {0: 7, 1: 6, 2: 2, 3: 0}
start = 0
target = 3
Example Output:
[0, 1, 2, 3]
"""
from heapq import heappop, heappush

class Solution:
    def a_star(self, graph, heuristic, start, target):
        """
        A* (A-star) algorithm for finding the shortest path in a weighted graph 
        with a heuristic function to estimate the cost from the current node to the target.

        Args:
        - graph (dict): A dictionary representing the graph, where each key is a node and 
          the value is a list of tuples (neighbor, weight), representing the neighbors of the node 
          and the weight of the edge to the neighbor.
        - heuristic (dict): A dictionary of heuristic values for each node, where the heuristic 
          value of a node is an estimate of the cost from that node to the target.
        - start (int): The starting node for the search.
        - target (int): The target node that we are trying to reach.

        Returns:
        - list: The list of nodes that forms the shortest path from the start to the target, 
                or a message "Path not found" if no path exists.
        """
        
        # Priority queue (min-heap) to store nodes with their f_score (estimated total cost)
        # f_score = g_score (actual cost from start to node) + heuristic (estimated cost to target)
        pq = [(0 + heuristic[start], start)]  # (f_score, node)
        
        # Dictionary to store the shortest known distance from start to each node
        g_score = {start: 0}
        
        # Dictionary to reconstruct the path once the target is found
        came_from = {}

        # While there are nodes to explore
        while pq:
            # Pop the node with the lowest f_score
            _, current = heappop(pq)

            # If the target is reached, reconstruct the path
            if current == target:
                path = []
                while current in came_from:  # Reconstruct the path from target to start
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]  # Return the reversed path from start to target

            # Explore all neighbors of the current node
            for neighbor, weight in graph.get(current, []):
                # Calculate the tentative g_score for the neighbor
                tentative_g_score = g_score[current] + weight
                
                # If the new g_score is better (lower), update the neighbor's g_score
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    # Record that the best path to the neighbor goes through current
                    came_from[neighbor] = current
                    # Update the g_score for the neighbor
                    g_score[neighbor] = tentative_g_score
                    # Calculate the f_score for the neighbor (g_score + heuristic)
                    f_score = tentative_g_score + heuristic[neighbor]
                    # Add the neighbor to the priority queue with its f_score
                    heappush(pq, (f_score, neighbor))

        # If the priority queue is empty and the target hasn't been found, return no path
        return "Path not found"

# Example usage
sol = Solution()
# Graph where each node points to its neighbors with edge weights
graph = {0: [(1, 1), (2, 4)], 1: [(2, 2), (3, 5)], 2: [(3, 1)]}
# Heuristic values for each node: estimate from each node to the target (node 3)
heuristic = {0: 7, 1: 6, 2: 2, 3: 0}  # Target node 3 has a heuristic of 0 (because it's the target)
start = 0  # Starting node is 0
target = 3  # Target node is 3

# Call the A* algorithm and print the resulting path
print(sol.a_star(graph, heuristic, start, target))


""""
18. Count Strongly Connected Components Using Kosaraju's Algorithm
Problem Statement:
Find the number of strongly connected components (SCCs) in a directed graph using Kosaraju's algorithm.

Example Input:
graph = {0: [1], 1: [2], 2: [0], 3: [4]}
Example Output:
2

"""
class Solution:
    def kosaraju(self, graph):
        """
        Implements Kosaraju's Algorithm to find the number of strongly connected components (SCCs) in a directed graph.

        Parameters:
        graph (dict): A directed graph represented as an adjacency list (dictionary).

        Returns:
        int: The count of strongly connected components in the graph.
        """

        def dfs(node, visited, stack):
            """
            Perform a Depth-First Search (DFS) and push nodes onto the stack in the order of completion.

            Parameters:
            node (int): The current node being visited.
            visited (set): A set to track visited nodes.
            stack (list): A stack to store nodes in their finishing order.
            """
            visited.add(node)  # Mark the current node as visited
            for neighbor in graph.get(node, []):  # Iterate through the neighbors of the current node
                if neighbor not in visited:  # If the neighbor has not been visited
                    dfs(neighbor, visited, stack)  # Recursively visit the neighbor
            stack.append(node)  # Add the node to the stack after exploring all its neighbors

        def reverse_graph(graph):
            """
            Reverse the given graph's edges.

            Parameters:
            graph (dict): A directed graph represented as an adjacency list.

            Returns:
            dict: The reversed graph.
            """
            reversed_graph = {}
            for node in graph:  # Iterate through each node in the graph
                for neighbor in graph[node]:  # For each neighbor, reverse the direction of the edge
                    reversed_graph.setdefault(neighbor, []).append(node)  # Add the reverse edge
            return reversed_graph

        def dfs_scc(node, visited, component):
            """
            Perform a DFS on the reversed graph to identify all nodes in a strongly connected component (SCC).

            Parameters:
            node (int): The current node being visited in the reversed graph.
            visited (set): A set to track visited nodes.
            component (list): A list to store all nodes in the current SCC.
            """
            visited.add(node)  # Mark the current node as visited
            component.append(node)  # Add the node to the current SCC
            for neighbor in reversed_graph.get(node, []):  # Iterate through the neighbors in the reversed graph
                if neighbor not in visited:  # If the neighbor has not been visited
                    dfs_scc(neighbor, visited, component)  # Recursively visit the neighbor

        # Step 1: Perform a DFS on the original graph and record the finishing order of nodes in the stack
        stack = []  # Stack to store nodes in the order of their finishing times
        visited = set()  # Set to track visited nodes
        for node in graph:  # Iterate through each node in the graph
            if node not in visited:  # If the node has not been visited
                dfs(node, visited, stack)  # Perform DFS from the node

        # Step 2: Reverse the graph
        reversed_graph = reverse_graph(graph)  # Get the reversed graph

        # Step 3: Perform DFS on the reversed graph in the order of the stack to find SCCs
        visited.clear()  # Clear the visited set for reuse
        scc_count = 0  # Initialize the count of SCCs

        while stack:  # While there are nodes in the stack
            node = stack.pop()  # Pop the top node
            if node not in visited:  # If the node has not been visited
                scc_count += 1  # Increment the SCC count
                dfs_scc(node, visited, [])  # Perform DFS to mark all nodes in the current SCC

        return scc_count  # Return the total number of SCCs

# Example Usage
sol = Solution()
graph = {0: [1], 1: [2], 2: [0], 3: [4]}  # A directed graph represented as an adjacency list
print(sol.kosaraju(graph))  # Output: 2 (SCCs: {0, 1, 2} and {3, 4})


"""
19. Detect Articulation Points (Critical Nodes) in a Graph
Problem Statement:
Given an undirected graph, find all articulation points (critical nodes) using Depth-First Search (DFS). 
A node is an articulation point if its removal increases the number of connected components.

Example Input:

graph = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2, 4, 5], 4: [3], 5: [3]}
Example Output:
[2, 3]
"""
class Solution:
    def kosaraju(self, graph):
        """
        Kosaraju's algorithm to find the Strongly Connected Components (SCCs) of a directed graph.

        Args:
        - graph (dict): A dictionary representing the directed graph, where each key is a node 
          and the value is a list of neighbors that the node points to.

        Returns:
        - int: The number of strongly connected components (SCCs) in the graph.
        """
        
        # Helper function: Depth First Search (DFS) to fill the stack with nodes in finishing order
        def dfs(node, visited, stack):
            """
            Perform a DFS traversal of the graph, marking nodes as visited and
            adding them to the stack in the order of their finishing times.

            Args:
            - node (int): The current node being visited.
            - visited (set): Set to track visited nodes.
            - stack (list): Stack to store nodes in the order of their finishing times.
            """
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor, visited, stack)
            stack.append(node)  # Push the node onto the stack when the DFS of its neighbors is complete

        # Helper function: Reverse the graph by reversing the direction of all edges
        def reverse_graph(graph):
            """
            Reverse the direction of all edges in the graph.

            Args:
            - graph (dict): The original directed graph.

            Returns:
            - dict: The reversed graph where all edges point in the opposite direction.
            """
            reversed_graph = {}
            for node in graph:
                for neighbor in graph[node]:
                    reversed_graph.setdefault(neighbor, []).append(node)
            return reversed_graph

        # Helper function: DFS to visit all nodes in the SCC and collect them
        def dfs_scc(node, visited, component):
            """
            Perform DFS traversal on the reversed graph to find all nodes in the same SCC.

            Args:
            - node (int): The starting node of the DFS.
            - visited (set): Set to track visited nodes.
            - component (list): List to store all nodes in the current SCC.
            """
            visited.add(node)
            component.append(node)
            for neighbor in reversed_graph.get(node, []):
                if neighbor not in visited:
                    dfs_scc(neighbor, visited, component)

        stack = []  # Stack to store nodes in finishing order from DFS
        visited = set()  # Set to track visited nodes
        
        # Step 1: Perform DFS on the original graph to fill the stack in order of finishing times
        for node in graph:
            if node not in visited:
                dfs(node, visited, stack)

        # Step 2: Reverse the graph
        reversed_graph = reverse_graph(graph)
        
        visited.clear()  # Clear the visited set for the second DFS traversal
        scc_count = 0  # Counter to track the number of strongly connected components

        # Step 3: Perform DFS on the reversed graph, process nodes in order of stack
        while stack:
            node = stack.pop()  # Pop the node with the latest finishing time
            if node not in visited:
                scc_count += 1  # Found a new SCC
                dfs_scc(node, visited, [])  # Collect all nodes in this SCC

        return scc_count  # Return the number of strongly connected components

# Example usage
sol = Solution()
# Graph represented as an adjacency list
graph = {0: [1], 1: [2], 2: [0], 3: [4]}  # A graph with two SCCs: {0, 1, 2} and {3, 4}
print(sol.kosaraju(graph))  # Output: 2


"""
20. Prim’s Algorithm for Minimum Spanning Tree
Problem Statement:
Given a weighted undirected graph, find the Minimum Spanning Tree (MST) using Prim's algorithm. The MST connects all vertices with 
the minimum possible total edge weight.

Example Input:

graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8)],
    2: [(1, 3), (3, 7)],
    3: [(0, 6), (1, 8), (2, 7)]
}
start = 0
Example Output:
[(0, 1, 2), (1, 2, 3), (0, 3, 6)]
Solution:
"""
from heapq import heappop, heappush

class Solution:
    def prim_mst(self, graph, start):
        """
        Prim's algorithm to find the Minimum Spanning Tree (MST) of a connected, undirected graph.

        Args:
        - graph (dict): The graph is represented as an adjacency list, where each key is a node,
          and the value is a list of tuples representing its neighbors and the corresponding edge weights.
        - start (int): The starting node for the MST.

        Returns:
        - list: A list of edges that form the MST, represented as (parent, node, weight).
        """
        
        mst = []  # List to store the edges in the MST
        visited = set()  # Set to track visited nodes to avoid cycles
        pq = [(0, start, None)]  # Priority queue to store edges, initialized with the starting node
        # Each element in pq is a tuple: (cost, node, parent)
        
        while pq and len(visited) < len(graph):  # Continue until all nodes are visited
            cost, node, parent = heappop(pq)  # Pop the edge with the smallest cost
            if node not in visited:  # If the node hasn't been visited
                visited.add(node)  # Mark it as visited
                
                # If the node has a parent (i.e., it's not the starting node), add the edge to the MST
                if parent is not None:
                    mst.append((parent, node, cost))  # Add the edge (parent, node, cost) to the MST
                
                # Explore the neighbors of the current node
                for neighbor, weight in graph.get(node, []):
                    if neighbor not in visited:  # If the neighbor hasn't been visited yet
                        heappush(pq, (weight, neighbor, node))  # Push the neighbor into the priority queue with its edge weight
        return mst  # Return the list of edges in the MST

# Example usage
sol = Solution()
# The graph is represented as an adjacency list with nodes and edge weights
graph = {
    0: [(1, 2), (3, 6)],  # Node 0 is connected to 1 (weight 2) and 3 (weight 6)
    1: [(0, 2), (2, 3), (3, 8)],  # Node 1 is connected to 0 (weight 2), 2 (weight 3), and 3 (weight 8)
    2: [(1, 3), (3, 7)],  # Node 2 is connected to 1 (weight 3) and 3 (weight 7)
    3: [(0, 6), (1, 8), (2, 7)]  # Node 3 is connected to 0 (weight 6), 1 (weight 8), and 2 (weight 7)
}
start = 0  # Start the MST from node 0
print(sol.prim_mst(graph, start))  # Output the edges in the MST

