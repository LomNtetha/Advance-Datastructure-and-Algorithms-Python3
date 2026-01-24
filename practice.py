def mincoindenominations(denominations,amount):

    count_coin = 0
    coin_used = []

    for coin in denominations:
        while coin <= amount:
            coin_used.append(coin)
            count_coin +=1
            amount -= coin
    return coin_used,count_coin


denominations = [25,12,10, 5, 1]
amount = 41  # Target amount in cents

used, count = mincoindenominations(denominations,amount)

print(used)
print(count)

def dfs(gragh,start):

    visited = set()
    result = []


    def dfs_backtrack(node):

        if node not in visited:
            visited.add(node)
            result.append(node)


            for neigbhor in gragh.get(node,[]):
                dfs_backtrack(neigbhor)
    dfs_backtrack(start)
    return result

graph = {
    0: [1, 2],  # Node 0 is connected to nodes 1 and 2
    1: [2],     # Node 1 is connected to node 2
    2: [3],     # Node 2 is connected to node 3
    3: [3]      # Node 3 has a self-loop (connected to itself)
}
start =0

num = dfs(graph,start)

print(num)

from collections import deque

def bfs(graph,start):

    visisted = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()

        if node not in visisted:
            visisted.add(node)
            result.append(node)

            for neighbor in graph.get(node,[]):
                if neighbor not in visisted:
                    queue.append(neighbor)

    return result
graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: [3]
}
start = 0

bfs_result = bfs(graph,start)

print(bfs_result)