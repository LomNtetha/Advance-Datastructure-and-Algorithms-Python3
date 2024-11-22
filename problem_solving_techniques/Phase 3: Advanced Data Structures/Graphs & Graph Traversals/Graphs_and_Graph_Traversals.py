"""
1. Depth-First Search (DFS) on a Graph
Problem Statement:
Given a graph represented as an adjacency list, perform DFS starting from a given node and return the order of traversal.

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
class Solution:
    def dfs(self, graph, start):
        visited = set()
        result = []

        def dfs_helper(node):
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in graph.get(node, []):
                    dfs_helper(neighbor)

        dfs_helper(start)
        return result

# Example
sol = Solution()
graph = {0: [1, 2], 1: [2], 2: [3], 3: [3]}
print(sol.dfs(graph, 0))


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
from collections import deque

class Solution:
    def bfs(self, graph, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in graph.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

        return result

# Example
sol = Solution()
graph = {0: [1, 2], 1: [2], 2: [3], 3: [3]}
print(sol.bfs(graph, 0))


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
        visited = set()
        stack = []

        def dfs(node):
            if node not in visited:
                visited.add(node)
                for neighbor in graph.get(node, []):
                    dfs(neighbor)
                stack.append(node)

        for node in graph:
            if node not in visited:
                dfs(node)

        return stack[::-1]

# Example
sol = Solution()
graph = {5: [2, 0], 4: [0, 1], 2: [3], 3: [1], 0: [], 1: []}
print(sol.topological_sort(graph))

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
        visited = set()
        recursion_stack = set()

        def dfs(node):
            if node in recursion_stack:
                return True
            if node in visited:
                return False

            visited.add(node)
            recursion_stack.add(node)
            for neighbor in graph.get(node, []):
                if dfs(neighbor):
                    return True
            recursion_stack.remove(node)
            return False

        for node in graph:
            if dfs(node):
                return True

        return False

# Example
sol = Solution()
graph = {0: [1], 1: [2], 2: [0]}
print(sol.has_cycle(graph))

"""
Question:
You are developing a text-based adventure game where players navigate through a series of interconnected rooms. Each room is represented as a node in a graph, and the connections between the rooms are represented as edges in the graph. Players can move from one room to another if there is a direct connection between them.

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
    def __init__(self):
        self.graph = {}  # Represents the rooms and their connections as an adjacency list

    def add_room(self, room):
        """
        Adds a room to the graph.
        :param room: The name of the room (node)
        """
        if room not in self.graph:
            self.graph[room] = []

    def connect_rooms(self, room1, room2):
        """
        Creates a two-way connection between two rooms.
        :param room1: First room
        :param room2: Second room
        """
        self.graph[room1].append(room2)
        self.graph[room2].append(room1)

    def find_shortest_path(self, start, end):
        """
        Finds the shortest path between two rooms using BFS.
        :param start: Starting room
        :param end: Destination room
        :return: List representing the shortest path or None if no path exists
        """
        if start not in self.graph or end not in self.graph:
            return None  # Return None if either room doesn't exist

        visited = set()  # To keep track of visited rooms
        queue = deque([[start]])  # Queue to store paths, starting with the `start` room

        while queue:
            path = queue.popleft()  # Get the next path from the queue
            room = path[-1]  # Get the last room in the current path

            if room in visited:
                continue

            visited.add(room)

            # Check if we've reached the destination
            if room == end:
                return path

            # Add connected rooms to the queue
            for neighbor in self.graph[room]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append(new_path)

        return None  # No path found


# Example Usage
solution = Solution()
solution.add_room("Entrance")
solution.add_room("Hallway")
solution.add_room("Kitchen")
solution.add_room("Living Room")
solution.add_room("Bedroom")

solution.connect_rooms("Entrance", "Hallway")
solution.connect_rooms("Hallway", "Kitchen")
solution.connect_rooms("Kitchen", "Living Room")
solution.connect_rooms("Living Room", "Bedroom")

# Find the shortest path
shortest_path = solution.find_shortest_path("Entrance", "Bedroom")
print("Shortest Path:", shortest_path)



"""
5. Find the Shortest Path Using Dijkstra's Algorithm
Problem Statement:
Given a graph represented as an adjacency list with edge weights and a starting node, find the shortest distance to all nodes using Dijkstra's algorithm.

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

import heapq

class Solution:
    def dijkstra(self, graph, start):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        pq = [(0, start)]  # (distance, node)

        while pq:
            curr_distance, curr_node = heapq.heappop(pq)
            if curr_distance > distances[curr_node]:
                continue

            for neighbor, weight in graph.get(curr_node, []):
                distance = curr_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

# Example
sol = Solution()
graph = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}
print(sol.dijkstra(graph, 0))

    
"""
6. Find the Shortest Path Using Bellman-Ford Algorithm
Problem Statement:
Given a directed graph with weighted edges, find the shortest path from a source node to all other nodes. The graph may contain negative weights, but no negative weight cycles.

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
        distances = [float('inf')] * num_vertices
        distances[source] = 0

        # Relax all edges V-1 times
        for _ in range(num_vertices - 1):
            for u, v, weight in edges:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

        # Check for negative weight cycles
        for u, v, weight in edges:
            if distances[u] + weight < distances[v]:
                return "Graph contains a negative weight cycle"

        return distances

# Example
sol = Solution()
edges = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5)]
num_vertices = 4
print(sol.bellman_ford(edges, num_vertices, 0))


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
        def dfs(current, path):
            if current == destination:
                result.append(path[:])
                return

            for neighbor in graph.get(current, []):
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()

        result = []
        dfs(source, [source])
        return result

# Example
sol = Solution()
graph = {0: [1, 2], 1: [2, 3], 2: [3], 3: []}
print(sol.find_all_paths(graph, 0, 3))

"""
8. Check if a Graph is Bipartite
Problem Statement:
Determine if a graph is bipartite (i.e., can its vertices be divided into two disjoint sets such that no two vertices within the same set are adjacent).

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
        colors = {}

        def dfs(node, color):
            if node in colors:
                return colors[node] == color
            colors[node] = color
            for neighbor in graph.get(node, []):
                if not dfs(neighbor, 1 - color):
                    return False
            return True

        for node in graph:
            if node not in colors:
                if not dfs(node, 0):
                    return False
        return True

# Example
sol = Solution()
graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
print(sol.is_bipartite(graph))


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
        visited = set()
        count = 0

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph.get(node, []):
                dfs(neighbor)

        for node in graph:
            if node not in visited:
                count += 1
                dfs(node)

        return count

# Example
sol = Solution()
graph = {0: [1], 1: [0], 2: [3], 3: [2], 4: []}
print(sol.count_connected_components(graph))
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
        visited = set()
        mst = []
        min_heap = [(0, 0, -1)]  # (cost, current_node, parent_node)

        while min_heap:
            cost, node, parent = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            if parent != -1:
                mst.append((parent, node, cost))
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor, node))

        return mst

# Example
sol = Solution()
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8)],
    2: [(1, 3), (3, 7)],
    3: [(0, 6), (1, 8), (2, 7)]
}
print(sol.prims_mst(graph))
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
        if parent[node] != node:
            parent[node] = self.find(parent, parent[node])
        return parent[node]

    def union(self, parent, rank, node1, node2):
        root1 = self.find(parent, node1)
        root2 = self.find(parent, node2)

        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
            return False  # No cycle
        return True  # Cycle detected

    def has_cycle(self, edges, num_vertices):
        parent = [i for i in range(num_vertices)]
        rank = [0] * num_vertices

        for u, v in edges:
            if self.union(parent, rank, u, v):
                return True
        return False

# Example
sol = Solution()
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
num_vertices = 4
print(sol.has_cycle(edges, num_vertices))

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
        visited = set()
        recursion_stack = set()

        def dfs(node):
            if node in recursion_stack:
                return True
            if node in visited:
                return False

            visited.add(node)
            recursion_stack.add(node)
            for neighbor in graph.get(node, []):
                if dfs(neighbor):
                    return True
            recursion_stack.remove(node)
            return False

        for node in graph:
            if node not in visited:
                if dfs(node):
                    return True
        return False

# Example
sol = Solution()
graph = {0: [1], 1: [2], 2: [0]}
print(sol.detect_cycle_dfs(graph))
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
        if parent[node] != node:
            parent[node] = self.find(parent, parent[node])
        return parent[node]

    def union(self, parent, rank, node1, node2):
        root1 = self.find(parent, node1)
        root2 = self.find(parent, node2)

        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

    def kruskal_mst(self, edges, num_vertices):
        edges.sort(key=lambda x: x[2])  # Sort by weight
        parent = [i for i in range(num_vertices)]
        rank = [0] * num_vertices
        mst = []

        for u, v, weight in edges:
            if self.find(parent, u) != self.find(parent, v):
                self.union(parent, rank, u, v)
                mst.append((u, v, weight))
        return mst

# Example
sol = Solution()
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
num_vertices = 4
print(sol.kruskal_mst(edges, num_vertices))

"""
14. Count the Number of Islands in a 2D Grid
Problem Statement:
Given a 2D grid representing water (0) and land (1), count the number of islands. An island is surrounded by water and connected horizontally or vertically.

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
        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
                return
            grid[x][y] = 0  # Mark as visited
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
                    dfs(i, j)
        return count

# Example
sol = Solution()
grid = [
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]
print(sol.num_islands(grid))

"""
15. Floyd-Warshall Algorithm for All-Pairs Shortest Paths
Problem Statement:
Given a graph represented as an adjacency matrix, compute the shortest distances between all pairs of nodes using the Floyd-Warshall algorithm. If a node is unreachable, return inf for that pair.

Example Input:

plaintext
Copy code
graph = [
    [0, 3, inf, inf],
    [inf, 0, 1, inf],
    [inf, inf, 0, 2],
    [4, inf, inf, 0]
]
Example Output:

plaintext
Copy code
[
    [0, 3, 4, 6],
    [inf, 0, 1, 3],
    [inf, inf, 0, 2],
    [4, 7, 8, 0]
]
"""
class Solution:
    def floyd_warshall(self, graph):
        num_vertices = len(graph)
        dist = [row[:] for row in graph]  # Create a copy of the graph

        for k in range(num_vertices):
            for i in range(num_vertices):
                for j in range(num_vertices):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist

# Example
inf = float('inf')
sol = Solution()
graph = [
    [0, 3, inf, inf],
    [inf, 0, 1, inf],
    [inf, inf, 0, 2],
    [4, inf, inf, 0]
]
print(sol.floyd_warshall(graph))

"""
16. Bellman-Ford Algorithm for Single Source Shortest Path
Problem Statement:
Given a weighted graph and a starting node, compute the shortest path from the start to all other nodes using the Bellman-Ford algorithm. Detect negative weight cycles.

Example Input:
edges = [(0, 1, 4), (0, 2, 5), (1, 2, -2), (2, 3, 3)]
num_vertices = 4
start = 0
Example Output:
[0, 4, 2, 5]
"""
class Solution:
    def bellman_ford(self, edges, num_vertices, start):
        dist = [float('inf')] * num_vertices
        dist[start] = 0

        for _ in range(num_vertices - 1):
            for u, v, weight in edges:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        for u, v, weight in edges:  # Check for negative weight cycle
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                return "Graph contains a negative weight cycle"
        
        return dist

# Example
sol = Solution()
edges = [(0, 1, 4), (0, 2, 5), (1, 2, -2), (2, 3, 3)]
num_vertices = 4
start = 0
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
        pq = [(0 + heuristic[start], start)]  # (f_score, node)
        g_score = {start: 0}
        came_from = {}

        while pq:
            _, current = heappop(pq)
            if current == target:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]

            for neighbor, weight in graph.get(current, []):
                tentative_g_score = g_score[current] + weight
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic[neighbor]
                    heappush(pq, (f_score, neighbor))
        return "Path not found"

# Example
sol = Solution()
graph = {0: [(1, 1), (2, 4)], 1: [(2, 2), (3, 5)], 2: [(3, 1)]}
heuristic = {0: 7, 1: 6, 2: 2, 3: 0}
start = 0
target = 3
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
        def dfs(node, visited, stack):
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor, visited, stack)
            stack.append(node)

        def reverse_graph(graph):
            reversed_graph = {}
            for node in graph:
                for neighbor in graph[node]:
                    reversed_graph.setdefault(neighbor, []).append(node)
            return reversed_graph

        def dfs_scc(node, visited, component):
            visited.add(node)
            component.append(node)
            for neighbor in reversed_graph.get(node, []):
                if neighbor not in visited:
                    dfs_scc(neighbor, visited, component)

        stack = []
        visited = set()
        for node in graph:
            if node not in visited:
                dfs(node, visited, stack)

        reversed_graph = reverse_graph(graph)
        visited.clear()
        scc_count = 0

        while stack:
            node = stack.pop()
            if node not in visited:
                scc_count += 1
                dfs_scc(node, visited, [])

        return scc_count

# Example
sol = Solution()
graph = {0: [1], 1: [2], 2: [0], 3: [4]}
print(sol.kosaraju(graph))

"""
19. Detect Articulation Points (Critical Nodes) in a Graph
Problem Statement:
Given an undirected graph, find all articulation points (critical nodes) using Depth-First Search (DFS). A node is an articulation point if its removal increases the number of connected components.

Example Input:

graph = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2, 4, 5], 4: [3], 5: [3]}
Example Output:
[2, 3]
"""
class Solution:
    def find_articulation_points(self, graph):
        def dfs(node, parent, time):
            visited[node] = True
            discovery[node] = low[node] = time
            children = 0
            is_articulation = False

            for neighbor in graph.get(node, []):
                if not visited[neighbor]:
                    children += 1
                    dfs(neighbor, node, time + 1)
                    low[node] = min(low[node], low[neighbor])

                    if low[neighbor] >= discovery[node] and parent is not None:
                        is_articulation = True
                elif neighbor != parent:
                    low[node] = min(low[node], discovery[neighbor])

            if parent is None and children > 1:
                is_articulation = True

            if is_articulation:
                articulation_points.add(node)

        visited = {}
        discovery = {}
        low = {}
        articulation_points = set()

        for node in graph:
            visited[node] = False
            discovery[node] = float('inf')
            low[node] = float('inf')

        for node in graph:
            if not visited[node]:
                dfs(node, None, 0)

        return list(articulation_points)

# Example
sol = Solution()
graph = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2, 4, 5], 4: [3], 5: [3]}
print(sol.find_articulation_points(graph))

"""
20. Prim’s Algorithm for Minimum Spanning Tree
Problem Statement:
Given a weighted undirected graph, find the Minimum Spanning Tree (MST) using Prim's algorithm. The MST connects all vertices with the minimum possible total edge weight.

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
        mst = []
        visited = set()
        pq = [(0, start, None)]  # (cost, node, parent)

        while pq and len(visited) < len(graph):
            cost, node, parent = heappop(pq)
            if node not in visited:
                visited.add(node)
                if parent is not None:
                    mst.append((parent, node, cost))
                for neighbor, weight in graph.get(node, []):
                    if neighbor not in visited:
                        heappush(pq, (weight, neighbor, node))
        return mst

# Example
sol = Solution()
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8)],
    2: [(1, 3), (3, 7)],
    3: [(0, 6), (1, 8), (2, 7)]
}
start = 0
print(sol.prim_mst(graph, start))
