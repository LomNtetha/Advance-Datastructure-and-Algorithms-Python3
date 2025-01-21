"""
1. Find Connected Components in a Graph
Question: Given a graph with n nodes, count the number of connected components.
Input:
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
Output: 2
"""

def find_connected_components(n, edges):
    # Initialize parent and rank arrays for Union-Find
    parent = list(range(n))  # Each node is its own parent initially
    rank = [0] * n  # Rank (tree depth) is 0 for all nodes initially

    def find(x):
        # Path compression: Make every node point to the root
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        # Union by rank: Attach smaller tree under the larger tree
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

    # Apply union for all edges
    for u, v in edges:
        union(u, v)

    # Find unique roots to count connected components
    roots = {find(i) for i in range(n)}
    return len(roots)

# Example usage
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(find_connected_components(n, edges))  # Output: 2

# Time Complexity: O(E * α(N)), where E is the number of edges and α is the inverse Ackermann function.
# Space Complexity: O(N), for parent and rank arrays.

"""
2. Check if a Graph Contains a Cycle
Question: Determine whether an undirected graph contains a cycle using Union-Find.
Input:
n = 3
edges = [[0, 1], [1, 2], [2, 0]]
Output: True
"""

def has_cycle(n, edges):
    # Initialize parent array for Union-Find
    parent = list(range(n))  # Each node is its own parent initially

    def find(x):
        # Path compression: Make every node point to the root
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        # Try to union two nodes
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            # If they already share the same root, there's a cycle
            return True
        parent[root_y] = root_x
        return False

    # Check all edges for cycles
    for u, v in edges:
        if union(u, v):
            return True
    return False

# Example usage
n = 3
edges = [[0, 1], [1, 2], [2, 0]]
print(has_cycle(n, edges))  # Output: True

# Time Complexity: O(E * α(N)), where E is the number of edges and α is the inverse Ackermann function.
# Space Complexity: O(N), for the parent array.

"""
3. Find the Redundant Connection
Question: In a graph where a single redundant edge makes it cyclic, find that edge.
Input:
edges = [[1, 2], [1, 3], [2, 3]]
Output: [2, 3]

"""

def find_redundant_connection(edges):
    # Initialize parent array for Union-Find
    n = len(edges)
    parent = list(range(n + 1))  # Include 1-based indexing

    def find(x):
        # Path compression
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        # Union two nodes, return False if they are already connected
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            return False
        parent[root_y] = root_x
        return True

    # Process each edge
    for u, v in edges:
        if not union(u, v):
            # Return the first edge that creates a cycle
            return [u, v]

# Example usage
edges = [[1, 2], [1, 3], [2, 3]]
print(find_redundant_connection(edges))  # Output: [2, 3]

# Time Complexity: O(E * α(N)), where E is the number of edges and α is the inverse Ackermann function.
# Space Complexity: O(N), for the parent array.

"""
4. Count Number of Provinces
Question: Given a matrix representing friendships, find the number of connected provinces (groups of friends).
Input:
isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
Output: 2"""

def count_provinces(is_connected):
    n = len(is_connected)
    parent = list(range(n))  # Each node is its own parent initially

    def find(x):
        # Path compression
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        # Union two nodes
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x

    # Process the adjacency matrix
    for i in range(n):
        for j in range(i + 1, n):  # Only process the upper triangle
            if is_connected[i][j] == 1:
                union(i, j)

    # Count unique roots
    roots = {find(i) for i in range(n)}
    return len(roots)

# Example usage
is_connected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
print(count_provinces(is_connected))  # Output: 2

# Time Complexity: O(N^2 * α(N)), where N is the number of nodes.
# Space Complexity: O(N), for the parent array.


"""
5. Smallest String with Swaps
Question: Given a string and pairs of indices that can be swapped, find the lexicographically smallest string.
Input:
s = "dcab"
pairs = [[0, 3], [1, 2]]
Output: "bacd"
"""

def smallest_string_with_swaps(s, pairs):
    # Union-Find (Disjoint Set Union) with Path Compression and Union by Rank
    parent = list(range(len(s)))  # Initialize parent array for Union-Find
    rank = [0] * len(s)  # Initialize rank array to optimize union by rank

    # Find function with path compression (flattens the tree structure)
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Compress the path recursively
        return parent[x]

    # Union function with union by rank (keeps the tree shallow)
    def union(x, y):
        root_x = find(x)  # Find the root of x
        root_y = find(y)  # Find the root of y
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x  # Root of y becomes root of x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y  # Root of x becomes root of y
            else:
                parent[root_y] = root_x  # Choose root_x as root and increment its rank
                rank[root_x] += 1

    # Perform union for each pair
    for u, v in pairs:
        union(u, v)

    # Group all indices by their root parent
    from collections import defaultdict
    groups = defaultdict(list)  # Dictionary to store groups of indices
    for i in range(len(s)):
        root = find(i)  # Find the root of each index
        groups[root].append(i)  # Add index to the corresponding group

    # Convert string to list for easier mutation
    s = list(s)
    # For each group of indices, sort the characters and assign them back
    for indices in groups.values():
        sorted_chars = sorted(s[i] for i in indices)  # Sort characters in each group
        for i, char in zip(sorted(indices), sorted_chars):  # Place sorted chars back
            s[i] = char

    return ''.join(s)  # Convert list back to string and return

# Example usage
s = "dcab"
pairs = [[0, 3], [1, 2]]
print(smallest_string_with_swaps(s, pairs))  # Output: "bacd"

# Time Complexity: O(N log N) where N is the length of the string.
# Space Complexity: O(N) for parent and rank arrays and dictionary for groups.

"""
6. Find the Longest Path in a Tree
Question: Given a tree represented as an edge list, find the length of its longest path.
Input:
edges = [[0, 1], [1, 2], [2, 3]]
Output: 3
"""
def longest_path_in_tree(edges):
    from collections import defaultdict

    # Build the graph as an adjacency list (tree structure)
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)  # Add edge u-v
        graph[v].append(u)  # Add edge v-u

    # Function to perform Depth First Search (DFS) and return the farthest node and distance
    def dfs(node, parent):
        farthest_node = node  # Initialize farthest node
        max_distance = 0  # Initialize max distance
        for neighbor in graph[node]:  # Traverse neighbors
            if neighbor != parent:  # Avoid going back to the parent
                dist, far_node = dfs(neighbor, node)  # Recursive DFS call
                if dist + 1 > max_distance:  # Update max distance
                    max_distance = dist + 1
                    farthest_node = far_node
        return max_distance, farthest_node  # Return distance and farthest node

    # Find farthest node from node 0 (arbitrary start)
    _, farthest_node = dfs(0, -1)
    # Now find the farthest distance from the farthest node (i.e., tree diameter)
    max_distance, _ = dfs(farthest_node, -1)

    return max_distance  # Return the length of the longest path

# Example usage
edges = [[0, 1], [1, 2], [2, 3]]
print(longest_path_in_tree(edges))  # Output: 3

# Time Complexity: O(N), where N is the number of nodes.
# Space Complexity: O(N), for the adjacency list.

"""
7. Number of Operations to Connect All Computers
Question: Given n computers and a list of connections, return the minimum number of operations to make all computers connected. If impossible, return -1.
Input:
n = 4
connections = [[0, 1], [0, 2], [1, 2]]
Output: 1
"""

def make_connected(n, connections):
    if len(connections) < n - 1:
        # If there are fewer than (n - 1) connections, it's impossible to connect all computers
        return -1

    parent = list(range(n))  # Initialize parent array for Union-Find

    # Find function with path compression
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    # Union function to connect two nodes (computers)
    def union(x, y):
        root_x = find(x)  # Find root of x
        root_y = find(y)  # Find root of y
        if root_x != root_y:
            parent[root_y] = root_x  # Union the two components

    # Perform union for each connection
    for u, v in connections:
        union(u, v)

    # Count the number of disconnected components
    components = sum(1 for i in range(n) if parent[i] == i)  # Count root nodes
    return components - 1  # The number of operations required is components - 1

# Example usage
n = 4
connections = [[0, 1], [0, 2], [1, 2]]
print(make_connected(n, connections))  # Output: 1

# Time Complexity: O(N + E), where N is the number of computers and E is the number of connections.
# Space Complexity: O(N), for parent array.

"""
8. Accounts Merge
Question: Merge accounts belonging to the same user based on shared email addresses.
Input:
accounts = [
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["John", "johnnybravo@mail.com"],
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"]
]
Output:
[
    ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
    ["John", "johnnybravo@mail.com"]
]"""

def accounts_merge(accounts):
    from collections import defaultdict

    parent = {}  # Dictionary to store the parent of each email
    email_to_name = {}  # Dictionary to store the name associated with each email

    # Find function with path compression
    def find(x):
        if parent.get(x, x) != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    # Union function to link two emails
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x  # Union the two email roots

    # Build the union-find structure by processing each account
    for account in accounts:
        name = account[0]
        first_email = account[1]
        email_to_name[first_email] = name  # Store the name associated with the first email
        for email in account[1:]:
            union(first_email, email)  # Union all emails in the account

    # Group emails by their root parent
    email_groups = defaultdict(list)
    for email in email_to_name:
        root = find(email)  # Find the root email for each email
        email_groups[root].append(email)  # Group emails by their root parent

    # Merge accounts by combining emails and sorting them
    merged_accounts = []
    for emails in email_groups.values():
        name = email_to_name[emails[0]]  # Get the name from the first email in the group
        merged_accounts.append([name] + sorted(emails))  # Sort emails and add name to the result

    return merged_accounts

# Example usage
accounts = [
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["John", "johnnybravo@mail.com"],
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"]
]
print(accounts_merge(accounts))  # Output: [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["John", "johnnybravo@mail.com"]]

# Time Complexity: O(E log E), where E is the number of emails.
# Space Complexity: O(E + N), where E is the number of emails and N is the number of accounts.


"""
9. Find the Minimum Spanning Tree Using Kruskal's Algorithm
Question: Implement Kruskal's algorithm to find the minimum spanning tree of a weighted graph.
Input:
n = 4
edges = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
Output: Minimum Spanning Tree: [[2, 3], [0, 3], [0, 1]]
"""

def kruskal_mst(n, edges):
    parent = list(range(n))  # Initialize parent array for Union-Find
    rank = [0] * n  # Initialize rank array for union by rank

    # Find function with path compression
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    # Union function to merge two sets
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x  # Union by rank
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y  # Union by rank
            else:
                parent[root_y] = root_x  # Choose root_x and increment its rank
                rank[root_x] += 1

    # Sort edges by weight (ascending order)
    edges.sort(key=lambda x: x[2])
    mst = []  # List to store the edges of the MST
    total_cost = 0  # Variable to store the total cost of MST

    # Process edges and form MST
    for u, v, weight in edges:
        if find(u) != find(v):  # Check if the nodes belong to different sets
            union(u, v)  # Union the two nodes
            mst.append([u, v])  # Add edge to MST
            total_cost += weight  # Add edge weight to total cost


"""
10. Optimize Network Connections
Question: Given a network with n nodes and existing connections, find the minimum cost to add new connections to ensure the network is fully connected.
Input:
n = 6
existing_connections = [[1, 4], [4, 5], [2, 3]]
new_connections = [[1, 2, 1], [3, 4, 2], [3, 5, 3]]
Output: 6"""

def optimize_network(n, existing_connections, new_connections):
    parent = list(range(n))  # Initialize parent array for Union-Find
    rank = [0] * n  # Initialize rank array for union by rank

    # Find function with path compression
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    # Union function to connect two nodes
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x  # Union by rank
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y  # Union by rank
            else:
                parent[root_y] = root_x  # Choose root_x and increment its rank
                rank[root_x] += 1

    # Union the existing connections
    for u, v in existing_connections:
        union(u - 1, v - 1)  # Adjust for 0-based indexing

    # Sort the new connections by cost
    new_connections.sort(key=lambda x: x[2])

    total_cost = 0  # Variable to track the total cost of added connections

    # Process the new connections
    for u, v, cost in new_connections:
        if find(u - 1) != find(v - 1):  # If u and v are not connected
            union(u - 1, v - 1)  # Connect the two nodes
            total_cost += cost  # Add the cost of this connection

    return total_cost

# Example usage
n = 6
existing_connections = [[1, 4], [4, 5], [2, 3]]
new_connections = [[1, 2, 1], [3, 4, 2], [3, 5, 3]]
print(optimize_network(n, existing_connections, new_connections))  # Output: 6
