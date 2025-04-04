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