from collections import deque


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

def subst_generate(nums):

    results = []

    def bactrack(start,current):
        results.append(current[:])

        for i in range(start, len(nums)):

            current.append(nums[i])

            bactrack(i + 1, current)


            current.pop()

    bactrack(0,[])
    return results


nums = [1, 2, 3]

permut = subst_generate(nums)

print(permut)