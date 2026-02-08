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


def denominations_coins(denominations,amount):

    used_coins = []
    count = 0

    for coin in denominations:

        if coin <= amount:
            used_coins.append(coin)
            count += 1
            amount -= coin

    return count,used_coins

denominations = [25,16,10, 5, 1]
# Example usage
amount = 41  # Target amount in cents

u,c = denominations_coins(denominations,amount)

print(u)
print(c)

def max_activities(start,end):

    activities = list(zip(start,end))

    activities.sort(key=lambda x:x[1])

    last_end_time = activities[0][1]
    count = 1
    selected_activities = [0]


    for i in range(1,len(activities)):

        if activities[i][0] >= last_end_time:
            count += 1
            selected_activities.append(i)
            last_end_time = activities[i][0]

    return count,selected_activities

start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

cnt,sela = max_activities(start,end)
print(cnt)
print(sela)

def max_transactions(transactions):

    transactions.sort(key=lambda x:x[1])

    selected = []
    last_end = float('-inf')


    for  start,end in transactions:
        if start >= last_end:
            selected.append((start,end))
            last_end = end

    return selected

transactions = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9)]

tran = max_transactions(transactions)

print(tran)

def max_platform_needed(arrival,departure):

    arrival = [time.zfill(5) for time in arrival]
    departure = [time.zfill(5) for time in departure]

    arrival.sort()
    departure.sort()

    i,j = 0,0
    platform_needed = 0
    max_platform = 0
    n = len(arrival)

    while i < n and j < n:
        if arrival[i] < departure[j]:
            platform_needed += 1
            max_platform = max(max_platform,platform_needed)
            i += 1
        else:
            platform_needed -= 1
            j += 1

    return max_platform 
arrival = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
departure = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]

platform = max_platform_needed(arrival,departure)
print(platform)


def job_sequencing(jobs):

    jobs.sort(key=lambda x:x[1], reverse=True)

    max_dealine = max(job[0] for job in jobs)

    slots = [-1] * (max_dealine + 1)
    total_profit = 0

    for dealine,profit in jobs:

        for j in range(min(dealine,max_dealine),0,-1):

            if slots[j] == -1:
                slots[j] = profit
                total_profit += profit
                break
    return total_profit

jobs = [(2, 100), (1, 19), (2, 27), (1, 25), (3, 15)]


profit = job_sequencing(jobs)

print(profit)

def minimize_diffrence(heights,k):

    heights.sort()

    n = len(heights)

    min_diffirence = heights[-1] - heights[0]

    for i in range(n - 1):

        new_max = max(heights[-1]-k,heights[i]+k)
        new_min = min(heights[0]+k,heights[i+1] -k)

        min_diffirence = min(min_diffirence,new_max-new_min)

    return min_diffirence



heights = [1, 5, 15, 10]
k = 3

mini = minimize_diffrence(heights,k)

print(mini)


def best_time_sell(prices):

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price,price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

prices = [7, 1, 5, 3, 6, 4]

mxprofit = best_time_sell(prices)

print(mxprofit)

def maxProfit(prices):

    profit = 0

    for i in range(1,len(prices)):

        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]

    return profit

prices = [7, 1, 5, 3, 6, 4]

prft = maxProfit(prices)
print(prft)


def min_cost_travel(days,costs):

    dp = {}

    travel_days = set(days)

    for day in range(1,days[-1] + 1):

        if day not in travel_days:

            dp[day] = dp.get(day -1 , 0)

        else:
            dp[day] = min(
                dp.get(day -1 , 0) + costs[0],
                dp.get(day -7 , 0)+ costs[1],
                dp.get(day -30 , 0)+ costs[2]

            )
    return dp[days[-1]]


days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]

dp_min = min_cost_travel(days,costs)

print(dp_min)

def robHouses(houses):

    prev = curr = 0

    for house in houses:

        prev,curr = curr,max(curr,prev+house)

    return curr
houses = [2, 7, 9, 3, 1]

mxrob = robHouses(houses)

print(mxrob)

def ways_climb_stairs(n):
    if n <= 2:
        return n
    
    dp = [1] * (n+1)

    dp[1],dp[2] = 1,2

    for i in range(3,n+1):

        dp[i] = dp[i-1] + dp[i-2]

    return dp[i]


n = 5

ways = ways_climb_stairs(n)

print(ways)
