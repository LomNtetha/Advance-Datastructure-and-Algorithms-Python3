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

dfs_answe = dfs(graph,start)

print(dfs_answe)

from collections import deque

def bfs(graph,start):

    visited = set()
    queue = deque([start])
    result = []


    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            result.append(node)

            for neigbhor in graph.get(node,[]):
                if neigbhor not in visited:
                    queue.append(neigbhor)
    return result
graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: [3]
}
start = 0

bfs_ans = bfs(graph,start)
print(bfs_ans)

def bfs_shortest_path(graph,start,end):

    if start not in graph or end not in graph:
        return []
    
    visited = set()
    queue = deque([(start,[start])])


    while queue:
        node,path = queue.popleft()

        if node == end:
            return path
        

        if node not in visited:
            visited.add(node)


            for neigbhor in graph.get(node,[]):
                if neigbhor not in visited:
                    queue.append((neigbhor, path +[neigbhor]))

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

short_path = bfs_shortest_path(graph,start,end)

print(short_path)

import heapq

def dijstra_algarithm(graph,source):

    distances = {i:float('inf') for i in graph}

    distances[source] = 0

    min_heap = [(0,source)]

    while min_heap:

        current_distance,current_node = heapq.heappop(min_heap)

        if current_distance > distances[current_node]:
            continue


        for neighbor,weight in graph[current_node]:
            dist = current_distance + weight

            if dist < distances[neighbor]:
                distances[neighbor] = dist

                heapq.heappush(min_heap, (dist,neighbor))

    return [distances[i] for i in range(len(graph))]

graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

source = 0

dijkstra_ans = dijstra_algarithm(graph,source)

print(dijkstra_ans)


def find_all_path(graph,source,destination):
    result = []
    def dfs(current,path):
        if current == destination:
            result.append(path[:])
            return
        
        for neigbhor in graph.get(current,[]):
            path.append(neigbhor)
            dfs(neigbhor,path)
            path.pop()

    dfs(source,[source])
    return result


graph = {
    0: [1, 2],
    1: [2, 3],
    2: [3],
    3: []
}
source = 0
destination = 3

all = find_all_path(graph,source,destination)

print(all)

from collections import deque, defaultdict

def recommend_friends(graph,user):

    visited = set()

    recommend = defaultdict(int)

    queue = deque([user])

    visited.add(user)

    while queue:
        current_user = queue.popleft()

        for friend in graph.get(current_user,[]):

            if friend not in visited:
                visited.add(friend)
                queue.append(friend)

            for mutual_friend in graph.get(friend,[]):
                    if mutual_friend not in visited and mutual_friend not in graph[user]:
                        recommend[mutual_friend] += 1

    return sorted(recommend.keys(), key=lambda x: recommend[x], reverse=True)

graph = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'Charlie', 'David'],
    'Charlie': ['Alice', 'Bob'],
    'David': ['Bob']
}
user = 'Alice'

friends = recommend_friends(graph,user)

print(friends)

