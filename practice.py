import heapq
from typing import List, Tuple


def denominations_coin(denominations, amount):

    denominations.sort(reverse= True)

    coin_used = []
    coin_count = 0

    for coin in denominations:
     
     if coin <= amount:

        coin_used.append(coin)
        coin_count += 1
        amount-= coin

    return coin_count, coin_used    


denominations = [25, 16,10, 5, 1]

amount = 41

total_denominations, used_coin = denominations_coin(denominations, amount)

print(total_denominations)

print(used_coin)


def max_activities(start, end):
   
   activities = list(zip(start,end))

   activities.sort(key=lambda x:x[1])

   last_end = activities[0][1]
   count = 1
   select_activities = [0]

   for i in range(1, len(activities)):
      if activities[i][0] >= last_end:
         count += 1
         select_activities.append(i)
         last_end = activities[i][1]
   return count, select_activities

start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]


num_activities, select_activity = max_activities(start,end)

print(f"Number of activities {num_activities}")

print(f"selected activities {select_activity}")


def fractiona_kanapsack(weights,values, capacity):
   
   items = zip(values,weights)
   

   ratio_items = [(v/w,w) for v, w in items]

   items= sorted(ratio_items,key=lambda x:x[1])

   total_value = 0.0

   for value_per_item, weight in ratio_items:
      if capacity >= weight:
         total_value += value_per_item * weight
         capacity-= weight

      else:
         total_value += value_per_item * capacity
         break
   return total_value




weights = [10, 20, 30]  # Weights of items
values = [60, 100, 120]  # Values of items
capacity = 50

max_value = fractiona_kanapsack(weights,values,capacity)
print(max_value)


def max_platform_need_train(arrival,departure):
   
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
         max_platform = max(max_platform, platform_needed)
         i += 1
      else:
         platform_needed -= 1
         j += 1
   return max_platform
         
   
arrival = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
departure = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]

maxplatform = max_platform_need_train(arrival, departure)

print(maxplatform)

def job_sequencing(jobs):

   jobs.sort(key =lambda x:x[1], reverse = True )

   max_dealine = max(job[0] for job in jobs) 

   slots = [-1] *(max_dealine+1)

   total_profit = 0

   for dealine,profit in jobs:

      for j in range (min(dealine,max_dealine),0, -1):
         if slots[j] == -1:
            slots[j] = profit
            total_profit += profit
            break
   return total_profit

jobs = [(2, 100), (1, 19), (2, 27), (1, 25), (3, 15)]

profit_dealine = job_sequencing(jobs)

print(profit_dealine)

def dijkstra_algorithms(graph,source):

   distances = {i: float('inf') for i in graph}

   distances[source] = 0

   min_heap = [(0,source)]


   while min_heap:
      current_distance, current_node = heapq.heappop(min_heap)
      if current_distance > distances[current_node]:
         continue
      for neighbor, weight in graph[current_node]:
         dist = current_distance + weight

         if dist < distances[neighbor]:
            distances[neighbor] = dist

            heapq.heappush(min_heap, (dist,neighbor))

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

short_dist = dijkstra_algorithms(graph,source)

print(short_dist)

def large_numbers(nums):
   num_str = list(map(str,nums))

   num_str.sort(key=lambda x:x*10, reverse = True)

   result = ''.join(num_str)

   return result

nums = [3, 30, 34, 5, 9]

large = large_numbers(nums)

print(large)



def minimize_difference(heights,k):

   heights.sort()

   n = len(heights)

   initial_min = heights[-1] - heights[0]

   min_diff = initial_min

   for i in range(n-1):

      new_min = min(heights[0] + k, heights[i + 1] - k)
      new_max = max(heights[-1] -k, heights[i] +k)


      min_diff = min(min_diff, (new_max - new_min))

   return min_diff



heights = [1, 5, 15, 10]
k = 3

diff_minimum = minimize_difference(heights, k)

print(diff_minimum)


def single_profit(prices):

   min_price = float('inf')

   max_profit = 0

   for price in prices:
      min_price = min(min_price, price)
      max_profit = max(max_profit, (price - min_price))
   return max_profit


prices = [7, 1, 5, 3, 6, 4]

best_profit = single_profit(prices)
print(best_profit)

def double_profit(prices):

   profit = 0

   for i in range(1,len(prices)):

      if prices[i] > prices[i - 1]:
         profit += prices[i] - prices[i-1]

   return profit

prices = [7, 1, 5, 3, 6, 4]

double_pp = double_profit(prices)

print(double_pp)

def min_cost_travel_day(days,costs):

   dp = {}
   travel_days = set(days)

   for day in range(1,days[-1] + 1):

      if day not in travel_days:
         dp[day] = dp.get(day -1, 0)

      else:
          dp[day] = min(
             dp.get(day -1, 0) + costs[0],
             dp.get(day -7, 0) + costs[1],
             dp.get(day -30, 0) + costs[2]
            )
   return dp[days[-1]]
         
days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]

min_cost_day = min_cost_travel_day(days,costs)

print(min_cost_day)


def ways_to_climp_stairs(n):

   if n <= 2:
      return n
   
   dp = [0] * (n +1)
   dp[1],dp[2] = 1,2

   for i in range(3, n + 1):
      dp[i] = dp[i - 1] + dp[i - 2]

   return dp[n]
n = 5

nums = ways_to_climp_stairs(n)

print(nums)

def rob_houses(nums):

   prev = curr = 0

   for num in nums:

      prev,curr = curr,max(curr, prev +num)

   return curr

nums = [2, 7, 9, 3, 1]

robs = rob_houses(nums)
print(robs)


def rob_houses_in_circle(numss):

   def rob_linear(houses):
      prev, curr = 0,0

      for money in houses:

         prev,curr = curr, max(curr,prev + money)

      return curr
   
   if len(nums) == 1:
            return nums[0]
   if len(nums) == 2:
      return max(nums[0], nums[1])
   

   exclude_last = rob_linear(numss[:-1])
   exclude_first = rob_linear(numss[1:])

   return max(exclude_last,exclude_first)



numss = [1, 2, 3, 1]

excudeddd = rob_houses_in_circle(numss)

print(excudeddd)

def dp_denominations(coins,amount):
   dp = [float('inf')] * (amount +1)
   dp[0] = 0

   for coin in coins:
      for i in range(coin, amount +1):
         dp[i] = min(dp[i], dp[i - coin] + 1)

   results = dp[amount] if dp[amount] != float('inf') else -1

   return results

coins = [1, 2, 5]

amount = 11

dp_results = dp_denominations(coins,amount)
print(dp_results)


def longest_increasing_subsquence(nums):

   dp = [1] * len(nums)

   for i in range(len(nums)):
      for j in range(i):
         if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j ]+ 1)

   return max(dp)

nums = [10, 9, 2, 5, 3, 7, 101, 18]

res = longest_increasing_subsquence(nums)

print(res)


from typing import List

def calpoints(ops):
   stack = []

   for op in ops:
      if op == "C":
         stack.pop()
      elif op == "D":
         stack.append(2 * stack[-1])
      elif op == "+":
         stack.append(stack[-1] + stack[-2])

      else:
         stack.append(int(op))
   return sum(stack)



ops = ["5", "2", "C", "D", "+"]
ops1 = ["5", "-2", "4", "C", "D", "9", "+", "+"]

ops_sum1 = calpoints(ops)
ops_sum2 = calpoints(ops1)

print (ops_sum1)
print (ops_sum2)

def is_valid(expression):
  stack = []
  pairs = {')':'(', '}':'{',']':'['}

  for char in expression:

      if char in pairs.values():
         stack.append(char)
         
      elif char in pairs:
         if not stack or stack.pop() != pairs[char]:
            return False
        
  return not stack


expression1 = ("{[()]}")
expression2 = ("{[(])}")
epx1 = is_valid(expression1)
exp2 = is_valid(expression2)

print(epx1)
print(exp2)

def dfs(graph,start):

   visited = set()
   result = []


   def dfs_helper(node):

      if node not in visited:
         visited.add(node)
         result.append(node)


         for neighbor in graph.get(node, []):
            dfs_helper(neighbor)
   dfs_helper(start)
   return result

graph = {
    0: [1, 2],  # Node 0 is connected to nodes 1 and 2
    1: [2],     # Node 1 is connected to node 2
    2: [3],     # Node 2 is connected to node 3
    3: [3]      # Node 3 has a self-loop (connected to itself)
}

start = 0

dfs_result = dfs(graph,start)

print(dfs_result)


from collections import deque
def bfs(graph, start):

   visited = set()
   queue = deque([start])
   result = []

   while queue:
      node = queue.popleft()

      if node not in visited:
         visited.add(node)
         result.append(node)


         for neighbor in graph.get(node, []):
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

print(bfs_result)

