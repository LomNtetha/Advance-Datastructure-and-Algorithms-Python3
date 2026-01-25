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

import heapq
def dijkstra_short_distance(graph,source):

    distances = {i:float('inf') for i in graph}

    distances[source] = 0

    min_heap = [(0,source)]

    while min_heap:
        current_distance,current_node = heapq.heappop(min_heap)

        if current_distance > distances[current_node]:
            continue
        
        for neigbhor,weight in graph[current_node]:
            dist = current_distance+weight

            if dist < distances[neigbhor]:
                distances[neigbhor] = dist
                heapq.heappush(min_heap, (dist,neigbhor))
               

    return [ distances[i] for i in range(len(graph))]

graph = {
    0: [(1, 4), (7, 8)],
    1: [(0, 4), (2, 8), (7, 11)],
    2: [(1, 8), (3, 7), (8, 2), (5, 4)],
    3: [(2, 7), (4, 9), (5, 14)],
    4: [(3, 9), (5, 10)],
    5: [(4, 10), (3, 14), (2, 4), (6, 2)],
    6: [(5, 2), (7, 1), (8, 6)],
    7: [(0, 8), (1, 11), (8, 7), (6, 1)],
    8: [(2, 2), (7, 7), (6, 6)]
}

source = 0

dj_short_dist = dijkstra_short_distance(graph,source)

print(dj_short_dist)


def max_activities(start,end):

    activities = list(zip(start,end))

    activities. sort(key=lambda x:x[1])

    last_end_time = activities[0][1]
    count = 1
    selected_activities = [0]

    for i in range(1,len(activities)):
        if activities[i][0]>= last_end_time:
            count += 1
            selected_activities.append(i)
            last_end_time = activities[i][1]

    return count,selected_activities
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

c,s = max_activities(start,end)

print(c)
print(s)

def min_platform_needed(arrival,departure):

    arrival = [time.zfill(5) for time in arrival]
    departure =[time.zfill(5)for time in departure]

    arrival.sort()
    departure.sort()

    i,j =0,0
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
            j +=1
    return max_platform

arrival = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
departure = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]

min_platform_needed = min_platform_needed(arrival,departure)

print(min_platform_needed)

def max_profit_sell(prices):

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price,price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

prices = [7, 1, 5, 3, 6, 4]

mx_profit = max_profit_sell(prices)

print(mx_profit)


def maxProfit_II(prices):

    profit = 0

    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            profit += prices[i] - prices[i-1]

    return profit

prices = [7, 1, 5, 3, 6, 4]

profit_II = maxProfit_II(prices)

print(profit_II)


def job_sequencing(jobs):

    jobs.sort(key=lambda x:x[1], reverse=True)

    max_dealine = max(job[0] for job in jobs)

    slots = [-1] * (max_dealine + 1)

    tota_profit =0

    for dealine, profit in jobs:
        for j in range(min(dealine,max_dealine),0,-1):

            if slots[j] == -1:
                slots[j]=profit
                tota_profit +=profit
                break
    return tota_profit
jobs = [(2, 100), (1, 19), (2, 27), (1, 25), (3, 15)]


tp = job_sequencing(jobs)

print(tp)


def majorityelements(nums):
    count1 = 0
    count2 = 0

    for num in nums:
        if num == 1:
            count1 += 1
        elif num == 2:
            count2 += 1

    if count2 > count1:
        return 2
    else:
        return 1


nums = [2, 2, 1, 1, 1, 2, 2]

mar = majorityelements(nums)
print(mar)

def min_costs_travel(days,costs):

    dp = {}
    travel_days = set(days)

    for day in range(1,days[-1]+1):

        if day not in travel_days:
            dp[day] = dp.get(day-1,0)

        else:
            dp[day] = min(
                dp.get(day-1,0) + costs[0],
                dp.get(day-7,0) + costs[1],
                dp.get(day-30,0) + costs[2]

            )
    return dp[days[-1]]

days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]

min_cost = min_costs_travel(days,costs)

print(min_cost)

def ways_to_climb_staries(n):

    if n <=2:
        return n
    
    dp = [1] * (n+1)
    dp[1],dp[2] =1,2

    for i in range(3, n+1):

        dp[i] = dp[i-1] + dp[i-2]

    return dp[i]

n = 5
x = ways_to_climb_staries(n)

print(x)

def rob(houses):

    if not houses:
        return 0
    
    if len(houses) ==1:
        return houses[0]
    
    dp = [1] * len(houses)

    dp[0],dp[1] = houses[0],max(houses[0],houses[1])

    for i in range(2,len(houses)):

        dp[i] = max(dp[i-1], dp[i-2] + houses[i])  

    return dp[-1]     
houses = [2, 7, 9, 3, 1]

robs = rob(houses)
print(robs)
