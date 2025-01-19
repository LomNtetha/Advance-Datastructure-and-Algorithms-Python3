import heapq
from typing import List


def max_denominations(denominations,amount):

    denominations.sort(reverse=True)

    coin_used = []
    number_coin = 0

    for coin in denominations:
        if coin <= amount:
            coin_used.append(coin)
            number_coin += 1
            amount -= coin
    return coin_used, number_coin
denominations = [25, 10, 5, 16,1]
# Example usage
amount = 41  # Target amount in cents

c, n = max_denominations(denominations, amount)

print(f"here is the coin used: {c}")
print (f"here is the number of coins {n}")


def max_activities(start,end):

    activities = list(zip(start,end))

    activities.sort(key=lambda x:x[1])

    selected_activities = [0]
    last_end_time = activities[0][1]
    count = 1

    for i in range(1, len(activities)):
        if activities[i][0] >= last_end_time:
            selected_activities.append(i)
            count+=1
            last_end_time = activities[i][1]
    return count, selected_activities
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

s,e = max_activities(start,end)
print(s)
print(e)

class Solution:
    def fractional_knapsack(self, weights: List[int], values: List[int], capacity: int) -> float:
        # Step 1: Zip values and weights together
        zipped_items = zip(values, weights)
        
        # Step 2: Calculate value-to-weight ratios and create a list of tuples
        items_with_ratios = [(v / w, w) for v, w in zipped_items]
        
        # Step 3: Sort the items by value-to-weight ratio in descending order
        items = sorted(items_with_ratios, reverse=True)
        
        total_value = 0.0  # Total value accumulated in the knapsack
        
        # Iterate through sorted items
        for value_per_weight, weight in items:
            # If the current item fits fully in the knapsack, take it
            if capacity >= weight:
                total_value += value_per_weight * weight
                capacity -= weight
            else:
                # If only a fraction of the item fits, take the fraction and stop
                total_value += value_per_weight * capacity
                break
        
        # Return the maximum value that can be taken
        return total_value
    
# Example usage:
solution = Solution()
weights = [10, 20, 30]  # Weights of items
values = [60, 100, 120]  # Values of items
capacity = 50  # Capacity of the knapsack

# Call the fractional_knapsack method
max_value = solution.fractional_knapsack(weights, values, capacity)

# Print the result
print(f"Maximum value in the knapsack: {max_value}")

def find_max_platforms(arrival, departure):

    arrival = [time.zfill(5) for time in arrival]
    departure = [time.zfill(5) for time in departure]
    arrival.sort()
    departure.sort()

    platforms_needed = 0
    max_platforms = 0
    i,j = 0,0
    n= len(arrival)

    while i < n and j < n:
        if arrival[i] < departure[j]:
            platforms_needed+= 1
            max_platforms = max(max_platforms, platforms_needed)
            i+=1

        else:
            platforms_needed -= 1
            j+=1
    return max_platforms
arrival = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
departure = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]

max_platforms = find_max_platforms(arrival, departure)

print(max_platforms)

def find_maximum_profit(jobs):
    jobs.sort(key=lambda x:x[1], reverse = True)

    max_dealine = max(job[0] for job in jobs)
    slots = [-1] * (max_dealine+1)
    total_profit = 0
    for dealine,profit in jobs:
        for j in range(min(dealine,max_dealine), 0,-1):
            if slots[j]==-1:
                slots[j] = profit
                total_profit+=profit
                break
    return total_profit
jobs = [(2, 100), (1, 19), (2, 27), (1, 25), (3, 15)]
total_profit = find_maximum_profit(jobs)
print(total_profit)


def Minimize_difference(heights,k):

    heights.sort()
    n = len(heights)

    mimum_difference = (heights[-1] -heights[0])

    for i in  range(n-1):
        new_max = max(heights[-1] -k, heights[i] +k)
        new_min = min(heights[0] +k, heights[i + 1] - k)

        mimum_difference = min(mimum_difference, (new_max - new_min))

    return mimum_difference
heights = [1, 5, 15, 10]
k = 3

min_diff = Minimize_difference(heights,k)

print(min_diff)


def dijkstra_algorithms(graph,source):

    distances = {i:float('inf') for i in graph}
    distances[source] = 0

    min_heap = [(0,source)]

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor,weight in graph[current_node]:
            dist = current_distance + weight

            if dist < distances[neighbor]:
                distances[neighbor] = dist

                heapq.heappush(min_heap, (dist,neighbor))
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

sort_dist = dijkstra_algorithms(graph, source)

print(sort_dist)



def largest_number(nums):

    nums_str = list(map(str, nums))
    
    nums_str.sort(key=lambda x:x*10, reverse=True)

    results = ''.join(nums_str)

    return results
nums = [3, 30, 34, 5, 9]

res = largest_number(nums)

print(res)

def maximum_profit(prices):

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(price, min_price)
        max_profit = max(max_profit, price-min_price)
    return max_profit
prices = [7, 1, 5, 3, 6, 4]

profit = maximum_profit(prices)

print(profit)


def maxProfit_multipletimes(prices):

    profit = 0

    for i in range(1, len(prices)):

        if prices[i] > prices[i-1]:

            profit += prices[i] - prices[i-1]
    return profit

prices = [7, 1, 5, 3, 6, 4]

pro = maxProfit_multipletimes(prices)

print(pro)

def bubble_sort(my_array):

    n = len(my_array)

    for i in range (n):
        for j in range(0, n-i-1):
            if my_array[j] > my_array[j+1]:
                my_array[i],my_array[j+1], my_array[j+1],my_array[i]
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

def bubble_sort_array_in_ascending_order(arr):
    n = len(arr)  # Get the length of the array
    # Traverse through all elements in the array
    for i in range(n):
        # Traverse the array from 0 to n-i-1
        # The last i elements are already sorted
        for j in range(0, n-i-1):
             if arr[j] > arr[j+1]:  # Swap if the element found is greater than the next element
         
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the elements

# Define the array to be sorted
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# Apply the bubble sort function
bubble_sort_array_in_ascending_order(my_array)

# Print the sorted array
print(f"{my_array}\n\n\n")




from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check if there are any duplicate numbers in the input list.
        Compare the length of the list with the length of the set (which removes duplicates).
        """
        return len(nums) != len(set(nums))

# Example input
example_input = [1, 2, 3, 4, 5, 1]

# Create an instance of Solution
sol = Solution().containsDuplicate(example_input)
print(f"Contains Duplicate: {sol}")

def min_days_costs(days,costs):
    dp = {}
    days_for_travels = set(days)

    for day in range(1, days[-1] +1):
        if day not in days_for_travels:
            dp[day] = dp.get(day -1, 0)
        else:
            dp[day] = min(
                dp.get(day - 1, 0) + costs[0],
                dp.get(day - 7, 0 ) + costs[1],
                dp.get(day - 30, 0) + costs[2]
            )
    return dp[days[-1]] 
days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
min_day = min_days_costs(days,costs)

print(min_day)


def clim_stairs(n):

    if n <=2:
        return n
    
    dp = [0]*(n+1)
    dp[1], dp[2] = 1,2

    for i in range(3, n+1):

        dp[i] = dp[i - 1] + dp[i -2]
    return dp[n]
n =5

ways = clim_stairs(n)

print(ways)


def rob(nums):

    prev = curr = 0

    for num in nums:

        prev,curr = curr, max(curr, prev + num)

    return curr


nums = [2, 7, 9, 3, 1]


number = rob(nums)

print(number)

def rob_circle(nums):

    def linear_rob(houses):

        prev, curr = 0, 0

        for money in houses:

            prev, curr = curr, max(curr, prev+money)
        return curr
        
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    
    exclude_last =  linear_rob(nums[:-1])
    exclude_first = linear_rob(nums[1:])

    return max(exclude_last, exclude_first)

nums = [1, 2, 3, 1]

numss = rob_circle(nums)

print(numss)