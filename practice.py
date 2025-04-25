from collections import defaultdict, deque


def dfs(graph,start):

    visited = set()
    result = []

    def dfs_helper(node):

        if node not in visited:
            visited.add(node)
            result.append(node)


            for neighbor in graph.get(node,[]):
                dfs_helper(neighbor)

    dfs_helper(start)
    return result

graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: [3]
}
start = 0

dfs_results = dfs(graph,start)
print(dfs_results)


def bfs(graph,start):

    visited =set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)


            for neighbor in graph.get(node,[]):
                if neighbor not in visited:
                    queue.append(neighbor)
    return result

graph = {
    0: [1, 2],  # Node 0 is connected to nodes 1 and 2
    1: [2],     # Node 1 is connected to node 2
    2: [3],     # Node 2 is connected to node 3
    3: [3]      # Node 3 has a self-loop (connected to itself)
}

start = 0

bfs_result = bfs(graph,start)

print(f"bfs result {bfs_result}")

from collections import OrderedDict

def topology_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):  # No sorting here
                dfs(neighbor)
            stack.append(node)

    for node in graph:  # Use insertion order
        if node not in visited:
            dfs(node)

    return stack[::-1]

# Use OrderedDict to preserve the order: 5, 4, 2, 3, 1, 0
graph = OrderedDict([
    (5, [2, 0]),
    (4, [0, 1]),
    (2, [3]),
    (3, [1]),
    (1, []),
    (0, [])
])

res_topology_sort = topology_sort(graph)
print(res_topology_sort)


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

def subst_backtracking(nums):

    results = []

    def backtrack(start,current):
        results.append(current[:])

        for i in range(start, len(nums)):
            current.append(nums[i])

            backtrack(i + 1, current)

            current.pop()

    backtrack(0,[])
    return results

nums = [1, 2, 3]

value_subset = subst_backtracking(nums)

print (value_subset)


def backtrack_permutation(nums):

    reslut = []

    def backtrack(path,used):

        if len(path) == len(nums):

            reslut.append(path[:])
            return
        
        for i in range(len(nums)):

            if used[i]:
                continue

            used[i] = True

            path.append(nums[i])

            backtrack(path,used)

            path.pop()

            used[i] = False


    backtrack([],[False] * len(nums))

    return reslut

nums = [1, 2, 3]

value_permutation = backtrack_permutation(nums)

print(value_permutation)


def commibination_sum(candidates,target):

    results = []

    def backtrack(start,current,remaining):
        if remaining == 0:
            results.append(current[:])
            return
        if remaining < 0:
            return
        
        for i in range(start,len(candidates)):

            current.append(candidates[i])

            backtrack(i,current, remaining - candidates[i])

            current.pop()

    backtrack(0,[],target)
    return results
candidates = [2, 3, 6, 7]
target = 7

value_combination = commibination_sum(candidates, target)

print(value_combination)


def combination_sum2(candidates,target):

    resuts = []

    candidates.sort()

    def backtrack(start,current, remaining):
        if remaining == 0:
            resuts.append(current[:])
            return
        if remaining < 0:
            return
        
        for i in range(start,len(candidates)):
            if i < start and candidates[i] == candidates[i - 1]:
                continue

            current.append(candidates[i])

            backtrack(i+1, current, remaining - candidates[i])

            current.pop()

    backtrack(0,[],target)

    return resuts

candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8

combinationsum2_value = combination_sum2(candidates,target)

print(combinationsum2_value)



def dfs(graph,start):

    visited = set()
    results = []

    def dfs_helper(node):

        if node not in visited:
            visited.add(node)
            results.append(node)

            for neighbor in graph.get(node,[]):
                dfs_helper(neighbor)

    dfs_helper(start)
    return results

graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: [3]
}
start = 0

value_dfs = dfs(graph,start)

print(value_dfs)


def bfs(graph,start):

    visisted = set()

    queue = deque([start])

    results = []

    while queue:
        node = queue.popleft()

        if node not in visisted:
            visisted.add(node)

            results.append(node)


            for neighbor in graph.get(node,[]):
                if neighbor not in visisted:
                    queue.append(neighbor)

    return results

graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: [3]
}
start = 0

bfs_value = bfs(graph,start)
print(bfs_value)


def rooms_shartes_path_in_bfs(graph,start,end):

    if start not in graph or end not in graph:
        return []
    
    visisted = set()
    queue = deque([(start,[start])])

    while queue:
        node,path = queue.popleft()

        if node == end:
            return path
        
        if node not in visisted:
            visisted.add(node)


            for neighbor in graph.get(node,[]):
                if neighbor not in visisted:
                    queue.append((neighbor, path + [neighbor]))

    return []

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

value_of_short_path = rooms_shartes_path_in_bfs(graph,start,end)

print(value_of_short_path)

def bellman_ford_algorithms_short_distance(edges,num_vertices,source):

    distances = [float('inf')] * num_vertices
    distances[source] = 0

    for _ in range(num_vertices - 1):
        for u,v,weight in edges:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    for u,v,weight in edges:
        if distances[u] + weight < distances[v]:
            return("The edges contains circle")
    return distances
edges = [
    (0, 1, 4),  # Edge from vertex 0 to vertex 1 with weight 4
    (0, 2, 1),  # Edge from vertex 0 to vertex 2 with weight 1
    (2, 1, 2),  # Edge from vertex 2 to vertex 1 with weight 2
    (1, 3, 1),  # Edge from vertex 1 to vertex 3 with weight 1
    (2, 3, 5)   # Edge from vertex 2 to vertex 3 with weight 5
]

num_vertices = 4  # Total number of vertices in the graph
source = 0     

bellman_value = bellman_ford_algorithms_short_distance(edges,num_vertices,source)
print(bellman_value)

def find_all_availble_routes(graph,source,destination):

    result = []

    def backtrack_dfs(current,path):

        if current == destination:
            result.append(path[:])
            return 
        
        for neigbhor in graph.get(current,[]):

            path.append(neigbhor)

            backtrack_dfs(neigbhor,path)


            path.pop()

    backtrack_dfs(source,[source])
    return result

            
graph = {
    0: [1, 2],
    1: [2, 3],
    2: [3],
    3: []
}
source = 0
destination = 3

value_backtrack = find_all_availble_routes(graph,source,destination)

print(value_backtrack)


def recommend_friend(graph,user):

    recommended = defaultdict(int)

    visited = set()

    queue = deque([user])

    visited.add(user)

    while queue:
        current_user = queue.popleft()

        for friend in graph.get(current_user,[]):
            if friend not in visited:

                visited.add(friend)
                queue.append(friend)

                for matual_friend in graph.get(friend,[]):
                    if matual_friend not in visited and matual_friend not in graph[user]:
                        recommended[matual_friend] += 1

    return sorted(recommended.keys(), key=lambda x: recommended[x], reverse = True)
graph = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'Charlie', 'David'],
    'Charlie': ['Alice', 'Bob'],
    'David': ['Bob']
}
    
user = 'Alice'

reommend_user_names = recommend_friend(graph,user)

print (reommend_user_names)

def find_short_routes_airplane_bfs(graph,start,end):

    if start not in graph  or end not in graph:
        return None
    
    visited = set()

    queue = deque([(start,[start])])

    while queue:
        node,path = queue.popleft()

        if node == end:
            return path
        
        if node not in visited:
            visited.add(node)

            for neighbor in graph.get(node,[]):
                if neighbor not in visited:
                    queue.append((neighbor,path +[neighbor]))

    return []


graph = {
    'JFK': ['LAX', 'ATL'],
    'LAX': ['JFK', 'ATL'],
    'ATL': ['JFK', 'LAX', 'ORD'],
    'ORD': ['ATL']
}

start = 'JFK'
end = 'ORD'

short = find_short_routes_airplane_bfs(graph,start,end)

print(short)