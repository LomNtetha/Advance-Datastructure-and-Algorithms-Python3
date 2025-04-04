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