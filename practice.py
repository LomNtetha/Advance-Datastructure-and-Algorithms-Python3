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

def bfs_shortest_path_in_rooms(graph,start,end):

    if start not in graph or end not in graph:
        return []
    
    visited = set()
    queue = deque([(start, [start])])


    while queue:
        node,path = queue.popleft()

        if node == end:
            return path
        if node not in visited:
            visited.add(node)

            for neigbhor in graph.get(node,[]):
                if neigbhor not in visited:
                    queue.append((neigbhor, path + [neigbhor]))

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

short = bfs_shortest_path_in_rooms(graph,start,end)

print(short)

from collections import defaultdict
def recommend_friends(graph,user):

    visited = set()
    recommended =defaultdict(int)
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

    return sorted(recommended.keys(), key=lambda x: recommended[x], reverse=True)

    

graph = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'Charlie', 'David'],
    'Charlie': ['Alice', 'Bob'],
    'David': ['Bob']
}
user = 'Alice'

friendss = recommend_friends(graph,user)

print (friendss)
