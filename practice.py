import heapq


def maximum_activities(start,end):
    activities = list(zip(start,end))

    activities.sort(key=lambda x:x[1])

    last_end_time = activities[0][1]
    print(last_end_time)
    selected_activities = [activities[0]]
    print(selected_activities)
    count = 1

    for i in range(1, len(activities)):
        if activities[i][0] >= last_end_time:
            count += 1
            selected_activities.append(activities[i])
            last_end_time = activities[i][1]

    return count, selected_activities
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

c,s = maximum_activities(start, end)

print(c)
print(s)


def kanapsack_fractions(weights,values,capacity):

    items = zip(values,weights)

    items_ratios = [(v/w,w )for v,w in items]

    sort_items = sorted(items_ratios, reverse=True)

    total_value = 0.0

    for item_weight, weight in sort_items:

        if capacity >= weight:
            total_value += item_weight * weight
            capacity -= weight

        else:
            total_value += item_weight * capacity
            break

    return total_value
    
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

t = kanapsack_fractions(weights,values,capacity)

print(t)



def maxi_platforms_needed(arrival, departure):

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

platformwww = maxi_platforms_needed(arrival, departure)

print(platformwww)

def job_sequence(jobs):

    jobs.sort(key=lambda x:x[1], reverse = True)

    max_dealine = jobs[-1][0]
    slots =  [-1] * (max_dealine + 1)
    total_profit = 0

    for dealine, profit in jobs:
        for j in range(min(dealine, max_dealine), 0, -1):
            if  slots[j] == -1:
                slots[j] = profit
                total_profit += profit
                break

    return total_profit

   
jobs = [(2, 100), (1, 19), (2, 27), (1, 25), (3, 15)]
tol_profit = job_sequence(jobs)
print(tol_profit)

def dijkstra_algorithms(graph,source):

    distances = {i: float('inf') for i in graph}

    distances[source] = 0

    min_heap = [(0, source)]



    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)
        if current_distance > distances[current_node]:

            continue

        for neighbor, weight in graph[current_node]:
            dist = current_distance + weight

            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(min_heap,(dist, neighbor))

    return [distances[i] for i in range(len(graph))]



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

dista = dijkstra_algorithms(graph,source)

print (dista)


def minimize_height_difference(heights, k):

    heights.sort()
    n = len(heights)

    initial_difference = heights[-1] - heights[0]

    min_difference = initial_difference
    
    for i in range(n - 1):
        new_max = max(heights[-1] - k, heights[i] + k)
        new_min = min(heights[0] + k, heights[i+1] - k)

        min_difference = min(min_difference,new_max - new_min)

    return min_difference
    

heights = [1, 5, 15, 10]
k = 3

mindiff = minimize_height_difference(heights, k)

print(mindiff)

def possible_large_number(nums):

    num_str = list(map(str,nums))

    num_str.sort(key=lambda x:x*10, reverse=True)

    print(num_str)

    results = ''.join(num_str)

    return results




nums = [3, 30, 34, 5, 9]

strnumber = possible_large_number(nums)

print (strnumber)

def maxprofit(prices):

    min_profit = float('inf')
    max_profit = 0
    

    for price in prices:
        min_profit = min(min_profit,price)
        max_profit = max(max_profit, price - min_profit)
    return max_profit

prices = [7, 1, 5, 3, 6, 4]

mm = maxprofit(prices)
print(mm)

def double_profit(prices):

    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit +=  prices[i] - prices[i -1]
    return profit
prices = [7, 1, 5, 3, 6, 4]

proft = double_profit(prices)
print(f"double profit: {proft}")


# Back to dynamic programming

def minimum_travel_day_cost(days,costs):

    dp = {}
    travel_days = set(days)

    for day in range(1, days[-1] +1):
        if day not in travel_days:
            dp[day] = dp.get(day - 1, 0)
        else:
            dp[day] = min(
                dp.get(day - 1, 0) + costs[0],
                dp.get(day - 7, 0) + costs[1],
                dp.get(day - 30, 0) + costs[2]
                )
    return dp[days[-1]]

days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]

min_travel_day = minimum_travel_day_cost(days,costs)

print(f"The minimum travel day is: {min_travel_day}")


def ways_to_climp_stairs(n):

    if n <= 2:
        return n
    dp = [0] * (n+1)
    dp[1],dp[2] = 1,2

    for i in range(3, n+1):
        dp[i] = dp[i -1] + dp[i -2]
    return dp[n]
n = 5

numbers_to_climp = ways_to_climp_stairs(n)
print(f"Numbers to climp the stairs are: { numbers_to_climp}")

def rob(houses):
    prev = curr = 0

    for house in houses:
        prev,curr = curr, max(curr, prev + house)
    return curr
houses = [2, 7, 9, 3, 1]

quick_robbers = rob(houses)

print(f"Asd quick robbers we get: ${quick_robbers}")

def rob_house_incircle(nums):
    def linear_rob(houses):
        prev,curr = 0,0

        for money in houses:
            prev,curr = curr,max(curr, prev + money)
        return curr
    
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    
    exclude_last = linear_rob(nums[:-1])
    exclude_first = linear_rob(nums[1:])

    return max(exclude_last, exclude_first)

nums = [1, 2, 3, 1]

robs = rob_house_incircle(nums)

print(f"I rob quick in a circle: {robs}")

def dp_denominations(coins, amount):

    dp = [float('inf')] * (amount+1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    results = dp[amount] if dp[amount] != float('inf') else -1
    return results

coins = [1, 2, 5]
amount = 11

number_coin = dp_denominations(coins, amount)
print(f"Total number of coin adding up to 11: {number_coin}")

from collections import defaultdict

def group_anagrams(strs):

    anagramss= defaultdict(list)

    for s in strs:

        sorted_strs = ''.join(sorted(s))

        anagramss[sorted_strs].append(s)
    return list(anagramss.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

ana = group_anagrams(strs)
print(ana)


def the_longest_strike(nums):

    num_set = set(nums)
    longest_strike = 0

    for num in num_set:

        if num - 1 not in num_set:
            current_num = num
            current_strike = 1
        
        while current_num + 1 in num_set:
            current_strike += 1
            current_num += 1

            longest_strike = max(longest_strike, current_strike)

    return longest_strike


nums = [100, 4, 200, 1, 3, 2]

longeststrke = the_longest_strike(nums)

print(longeststrke)


def Isormphorbic(s,t):

    mapping_s_t = {}
    mapping_t_s = {}

    for c1,c2 in zip(s,t):
        if c1 not in mapping_s_t and c2 not in mapping_t_s:
            mapping_s_t[c1] = c2
            mapping_t_s[c2] = c1

        elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
            return False
    return True
s = "egg"
t = "add"

yes_no = Isormphorbic(s,t)

print(yes_no)

def word_pattern(pattern,s):

    words = s.split()

    if len(pattern) != len(words):
        return False
    
    mapping_cha_word = {}
    mapping_word_cha = {}

    for cha,word in zip(pattern,s):

        if cha not in mapping_cha_word and  word not in mapping_word_cha:
            mapping_cha_word[cha] = word
            mapping_word_cha[word] = cha

        elif mapping_cha_word.get(cha) != word or  mapping_word_cha != cha:
            return False
    return True

pattern = "abba"
s = "dog cat cat dog"