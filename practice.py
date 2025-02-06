import heapq
from typing import List, Tuple


def make_denominations(denominations,amount):

    denominations.sort(reverse = True)
    list_coin = []
    num_coins = 0

    for coin in denominations:

        if coin <= amount:
            num_coins +=1
            list_coin.append(coin)
            amount -=coin
           

    return list_coin, num_coins

denominations = [25, 16,10, 5, 1]
amount = 41  # Target amount in cents

list_oin, nums_coin = make_denominations(denominations, amount)
print(list_oin)
print(nums_coin)

def maximum_activities(start,end):

    activities = list(zip(start,end))
    activities.sort(key=lambda x:x[1])

    last_end_time = activities[0][1]
    count = 1
    select_activities = [0]

    for i in range(1, len(activities)):

        if activities[i][0] >= last_end_time:
            count+=1

            select_activities.append(i)

            last_end_time = activities[i][1]

    return count, select_activities

start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

count, selected_activities = maximum_activities(start,end)
print(f"number of ctivities {count}")
print(f"selected activiies {selected_activities}")


def fractional_knapsack(weights,values,capacity):

    items = zip(values,weights)

    items_with_ratio = [(v/w,w) for v,w in items]

    items_with_ratio.sort(reverse=True)
    total_value = 0.0

    for value_per_weight,weight in items_with_ratio:
        if capacity >= weight:
            total_value += value_per_weight * weight
            capacity -= weight

        else:
            total_value += value_per_weight * capacity
            break
    return total_value

weights = [10, 20, 30]  # Weights of items
values = [60, 100, 120]  # Values of items
capacity = 50  # Capacity of the knapsack

total_value = fractional_knapsack(weights,values,capacity)

print(total_value)


def dijstra_algorithms(graph, source):

    distances = {i: float('inf') for i in graph}
    distances[source] = 0

    min_heap = [(0,source)]

    while min_heap:
        current_distnce, current_node = heapq.heappop(min_heap)

        if current_distnce > distances[current_node]:
            break

        for neighbor,weight in graph[current_node]:
            dist = current_distnce + weight
            
            if dist < distances[neighbor]:
                distances[neighbor] = dist

                heapq.heappush(min_heap,(dist, neighbor))

    return distances

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

dist = dijstra_algorithms(graph,source)

print(dist)

def job_sequencing(jobs):

    jobs.sort(key=lambda x:x[1], reverse=True)

    max_dealine = max(job[0] for job in jobs)

    total_profit = 0
    slots = [-1] * (max_dealine+1)

    for dealine,profit in jobs:
        for j in range(min(dealine,max_dealine),0, -1):
            if slots[j] == -1:
                slots[j] = profit
                total_profit += profit

                break

    return total_profit


        

jobs = [(2, 100), (1, 19), (2, 27), (1, 25), (3, 15)]

total_pro = job_sequencing(jobs)

print(f"Total profit of job squence {total_pro}")

def reduce_difference(heights,k):
    heights.sort()

    n = len(heights)
    intial_difference = heights[-1] - heights[0]

    min_difference = intial_difference

    for i in range(n - 1):
        new_max = max(heights[-1] -k, heights[i]+k)
        new_min = min(heights[0] + k, heights[i+1]-k)

        min_difference = min(min_difference, (new_max - new_min))

    return min_difference

heights = [1, 5, 15, 10]
k = 3

diff = reduce_difference(heights,k)
print("minimum diffirence",diff)



def max_platforms_needed(arrival,departure):

    arrival = [time.zfill(5) for time in arrival]
    departure = [time.zfill(5) for time in departure]

    arrival.sort()
    departure.sort()

    i,j = 0,0
    platform_needed = 0
    max_platforms = 0
    n = len(arrival)

    while i < n and j < n:
         if arrival[i] < departure[j]:
             platform_needed += 1
             max_platforms = max(max_platforms, platform_needed)
             i += 1
         else:
             platform_needed -= 1
             j += 1
    return max_platforms


arrival = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
departure = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]

max = max_platforms_needed(arrival,departure)

print(max)

def largest_number(nums):

    nums_str = list(map(str,nums))
    nums_str.sort(key=lambda x:x*10, reverse=True)

    results = ''.join(nums_str)

    return results
nums = [3, 30, 34, 5, 9]

res = largest_number(nums)

print(res)

