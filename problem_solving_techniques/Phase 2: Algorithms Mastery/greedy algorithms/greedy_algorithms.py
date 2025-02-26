"""
1. Problem:
Suppose we have coin denominations of 25, 10, 5, and 1 (as in U.S. currency) and need to make 41 cents. Our goal is to use as few coins as possible
to reach this amount.

Complexity:
Time Complexity: O(n), where 
n is the number of coin denominations (constant in this case as it is a fixed list of 4 denominations).
Space Complexity: O(k), where 
k is the number of coins used (to store the list coins_used).
"""

class Solution:
    def minimumCoins(self, amount):
        """
        Function to find the minimum number of coins required to make the given amount.
        Parameters:
        - amount (int): The target amount in cents.
        
        Returns:
        - int: Minimum number of coins required.
        - list: Coins used to form the amount.
        """
        # Variables to store the number of coins and the list of coins used
        coin_count = 0
        coins_used = []

        # Iterate through each denomination
        for coin in denominations:
            # Determine how many coins of this denomination can be used
            while amount >= coin:
                coins_used.append(coin)  # Append the coin
                coin_count += 1          # Increment the coin count
                amount -= coin           # Reduce the remaining amount


        return coin_count, coins_used

# Coin denominations in descending order
denominations = [25, 16,10, 5, 1]
# Example usage
solution = Solution()
amount = 41  # Target amount in cents
min_coins, coins_used = solution.minimumCoins(amount)
print(f"Minimum coins required: {min_coins}")
print(f"Coins used: {coins_used}")


"""
2. Activity Selection Problem
Problem:
Given n activities with their start and end times, select the maximum number of activities that can be performed by a single person, 
assuming that a person can only work on one activity at a time.

Example:
Input: start = [1, 3, 0, 5, 8, 5], end = [2, 4, 6, 7, 9, 9]
Output: 4
Explanation: The maximum set of non-overlapping activities are [0, 1], [3, 4], and [4, 5] (total 4 activities).

"""
from typing import Dict, List, Tuple


class Solution:
    def max_activities(self, start: List[int], end: List[int]) -> int:
        # Zip start and end times together
        activities = list(zip(start, end))
        
        # Sort the activities based on their end times (second element of each tuple)
        activities.sort(key=lambda x: x[1])
        
        # The first activity is always selected
        last_end_time = activities[0][1]
        count = 1  # We've selected the first activity
        selected_activities = [0]  # To store indices of selected activities
        
        # Iterate over the remaining activities
        for i in range(1, len(activities)):
            # If the current activity starts after the last selected activity ends, select it
            if activities[i][0] >= last_end_time:
                count += 1
                selected_activities.append(i)  # Track the index of the selected activity
                # Update last_end_time to the end time of the current activity
                last_end_time = activities[i][1]
        
        # Return the maximum number of activities that can be performed and the selected activities' indices
        return count, selected_activities


# Example usage
solution = Solution()
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
max_activities, selected_activities = solution.max_activities(start, end)

print(f"Maximum number of activities: {max_activities}")
print(f"Indices of selected activities: {selected_activities}")

"""
Statement: You are given a list of transactions with start and end times. Schedule the maximum number of transactions without overlapping.

Example Input:
transactions = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9)]
"""
def max_transactions(transactions):
    # Sort transactions based on their end time
    transactions.sort(key=lambda x: x[1])

    selected = []
    last_end = float('-inf')

    for start, end in transactions:
        if start >= last_end:  # If the transaction does not overlap
            selected.append((start, end))
            last_end = end  # Update the last selected transaction's end time

    return selected

# Example usage
transactions = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9)]
result = max_transactions(transactions)

print("Maximum Non-Overlapping Transactions:", result)


"""
Time Complexity: O(n log n)
We sort the activities based on their end times.
Space Complexity: O(n)
We store the sorted list of activities.
"""

"""
3. Fractional Knapsack Problem
Problem:
Given n items with their weights and values, select fractions of items to maximize the total value in a knapsack of capacity W.

Example:
Input: weights = [10, 20, 30], values = [60, 100, 120], capacity = 50
Output: 240
Explanation: Take the full items with weight 20 (value 100) and weight 10 (value 60), and 2/3 of the item with weight 30 (value 80).

"""

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


"""
An investor has $50,000 to allocate across three investment options. Each option has a cost per unit (investment) and an expected return per unit.
The goal is to maximize the total return while staying within the budget.

Inputs:

Investment options (costs and returns):
Option 1: Cost = $10,000, Return = $15,000
Option 2: Cost = $20,000, Return = $25,000
Option 3: Cost = $15,000, Return = $18,000
Budget: $50,000
"""
class Solution:
    def fractional_allocation(self, costs: List[int], returns: List[int], budget: int) -> float:
        # Step 1: Zip costs and returns together
        zipped_items = zip(costs, returns)
        
        # Step 2: Calculate return-to-cost ratios and create a list of tuples
        investments = [(r / c, c, r) for c, r in zipped_items]
        
        # Step 3: Sort investments by ratio in descending order
        investments.sort(reverse=True, key=lambda x: x[0])
        
        total_return = 0.0  # Total return accumulated
        
        # Step 4: Allocate budget
        for ratio, cost in investments:
            if budget >= cost:
                # Take the full investment
                total_return += ratio * cost
                budget -= cost
            else:
                # Take a fractional part of the investment
                total_return += ratio * budget
                break
        
        return total_return

# Example usage
solution = Solution()
costs = [10000, 20000, 15000]
returns = [15000, 25000, 18000]
budget = 50000

max_return = solution.fractional_allocation(costs, returns, budget)
print(f"Maximum return from the investment: ${max_return:.2f}")

"""
Statement: Allocate a budget to projects such that the total cost does not exceed the budget and the maximum number of projects are funded.

Example Input:
projects = [10, 20, 30, 40]  # Cost of each project
budget = 50  
"""
def max_funded_projects(projects, budget):
    projects.sort()  # Sort projects by cost
    funded = []
    total_cost = 0

    for cost in projects:
        if total_cost + cost <= budget:
            funded.append(cost)
            total_cost += cost
        else:
            break  # Stop when budget is exceeded

    return funded, len(funded)

projects = [10, 20, 30, 40]
budget = 50
print(max_funded_projects(projects, budget))  # Output: ([10, 20], 2)


"""
Time Complexity: O(n log n)
We sort the items based on their value-to-weight ratio.
Space Complexity: O(n)
We store the sorted list of items.
"""

"""
4. Minimum Number of Platforms Required for a Railway Station
Problem:
Given the arrival and departure times of trains at a railway station, find the minimum number of platforms required to accommodate
all trains without delay.

Example:
Input: arrival = [9:00, 9:40, 9:50, 11:00, 15:00, 18:00], departure = [9:10, 12:00, 11:20, 11:30, 19:00, 20:00]
Output: 3
Explanation: At peak time (around 11:00), there are 3 trains at the station.

"""
class Solution:
    def findMinPlatforms(self, arrival, departure):

        # Format arrival and departure times to ensure proper comparison
        arrival = [time.zfill(5) for time in arrival]
        departure = [time.zfill(5) for time in departure]
        # Sort arrival and departure times
        arrival.sort()
        departure.sort()
        
        # Initialize pointers and platform counters
        #i: Tracks the next arrival.
        #j: Tracks the next departure.
        i, j = 0, 0
        platforms_needed = 0
        max_platforms = 0
        n = len(arrival)
        
        # Traverse both arrays
        while i < n and j < n:
            # If the next train is arriving
            if arrival[i] < departure[j]:
                platforms_needed += 1
                max_platforms = max(max_platforms, platforms_needed)
                i += 1
            else:  # If the next train is departing
                platforms_needed -= 1
                j += 1
        return max_platforms

# Example usage
arrival = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
departure = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]

solution = Solution()
print(solution.findMinPlatforms(arrival, departure))  # Output: 3


"""
Time Complexity: O(n log n)
We sort the arrival and departure times.
Space Complexity: O(1)
We use only a few extra variables.
"""

"""
5. Job Sequencing Problem
Problem:
Given n jobs with their deadlines and profits, find the sequence of jobs that maximizes the total profit. Each job takes 1 unit of time,
and a job must be completed by its deadline.

Example:
Input: jobs = [(2, 100), (1, 19), (2, 27), (1, 25), (3, 15)]
Output: 142
Explanation: Schedule jobs (2, 100), (2, 27), and (1, 25) to maximize profit.
"""
class Solution:
    def job_sequencing(self, jobs: List[Tuple[int, int]]) -> int:
        # Sort jobs based on profit in descending order
        jobs.sort(key=lambda x: x[1], reverse=True)
        
        # Find the maximum deadline
        max_deadline = max(job[0] for job in jobs)
        
        # Initialize a list to keep track of the time slots (one slot for each deadline)
        slots = [-1] * (max_deadline + 1)
        total_profit = 0  # Variable to store the total profit
        
        # Iterate through the sorted jobs
        for deadline, profit in jobs:
            # Check if there is a free slot for this job (starting from the job's deadline)
            for j in range(min(deadline, max_deadline), 0, -1):
                if slots[j] == -1:  # If the slot is free
                    slots[j] = profit  # Assign the job to this slot
                    total_profit += profit  # Add the profit of this job
                    break  # Move to the next job once the current one is scheduled
        
        # Return the total profit
        return total_profit
# Example usage
jobs = [(2, 100), (1, 19), (2, 27), (1, 25), (3, 15)]
solution = Solution()
print(solution.job_sequencing(jobs))  # Output: 142
"""
    
Time Complexity: O(n log n)
We sort the jobs by profit and then iterate over the jobs and slots.
Space Complexity: O(d)
We use a list of size equal to the maximum deadline d.
"""

"""
6. Dijkstra’s Shortest Path Algorithm
Problem:
Given a weighted graph, find the shortest path from a given source node to all other nodes using Dijkstra’s algorithm.

Example:
Input:
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
Source Node: 0
Output: Distances: [0, 4, 12, 19, 21, 11, 9, 8, 14]
Explanation: The shortest path from node 0 to all other nodes is given by the distance array.

"""
import heapq

class Solution:
    def dijkstra(self, graph: Dict[int, List[Tuple[int, int]]], source: int) -> List[int]:
        # Initialize distances from source to all nodes as infinity
        distances = {i: float('inf') for i in graph}
        # Set the distance of the source to itself as 0
        distances[source] = 0
        
        # Min-heap to keep track of the shortest distance discovered so far
        min_heap = [(0, source)]  # (distance, node)
        
        # Iterate while the heap is not empty
        while min_heap:
            current_distance, current_node = heapq.heappop(min_heap)
            
            # If we have already found a shorter path before, skip this one
            if current_distance > distances[current_node]:
                continue
            
            # Iterate over neighbors of the current node
            for neighbor, weight in graph[current_node]:
                # Calculate the new distance to the neighbor
                dist = current_distance + weight
                
                # If a shorter distance is found, update and push it to the heap
                if dist < distances[neighbor]:
                    distances[neighbor] = dist
                    heapq.heappush(min_heap, (dist, neighbor))
        
        # Return the distances from the source to all other nodes
        return [distances[i] for i in range(len(graph))]
# Example usage
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
solution = Solution()
distances = solution.dijkstra(graph, source)

# Output distances
print("Distances:", [distances[i] for i in range(len(graph))])

"""      
Time Complexity: O(E log V)
Where E is the number of edges and V is the number of vertices.
Space Complexity: O(V)
We use space to store distances and the heap.
"""


"""
7. Huffman Encoding
Problem:
Given a set of characters and their frequencies, your task is to build a Huffman Tree and determine the optimal binary code
for each character, such that the total encoding length is minimized.

Example:
Input:
characters = ['a', 'b', 'c', 'd', 'e', 'f']
frequencies = [5, 9, 12, 13, 16, 45]
Output:
Huffman Codes:
a: 1100  
b: 1101  
c: 100  
d: 101  
e: 111  
f: 0
Explanation: A Huffman tree minimizes the total number of bits needed to represent the characters based on their frequency.

"""
import heapq

class Node:
    def __init__(self, freq, char=None):
        self.freq = freq  # Frequency of the character
        self.char = char  # Character itself (None for internal nodes)
        self.left = None  # Left child
        self.right = None  # Right child

    # Comparator for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

class Solution:
    def huffman_encoding(self, characters: List[str], frequencies: List[int]) -> Dict[str, str]:
        # Build a priority queue (min-heap) where each element is a node with frequency
        heap = [Node(frequencies[i], characters[i]) for i in range(len(characters))]
        heapq.heapify(heap)
        
        # Combine nodes until only one remains (the root of the Huffman Tree)
        while len(heap) > 1:
            left = heapq.heappop(heap)  # Extract the node with the smallest frequency
            right = heapq.heappop(heap)  # Extract the second smallest
            
            # Create a new internal node with combined frequency of left and right
            merged = Node(left.freq + right.freq)
            merged.left = left  # Left child is the smaller frequency node
            merged.right = right  # Right child is the second smallest node
            heapq.heappush(heap, merged)  # Push the new node back to the heap
        
        # The remaining node is the root of the Huffman tree
        root = heapq.heappop(heap)
        
        # Recursively build the Huffman code
        def build_code(node, current_code, code_map):
            if node is None:
                return
            # If it's a leaf node (contains a character), add the code to the map
            if node.char:
                code_map[node.char] = current_code
            build_code(node.left, current_code + '0', code_map)  # Left = 0
            build_code(node.right, current_code + '1', code_map)  # Right = 1
        
        code_map = {}
        build_code(root, '', code_map)  # Start building the code from the root
        return code_map
"""
Time Complexity: O(n log n)
Building the heap and tree takes O(n log n), where n is the number of characters.
Space Complexity: O(n)
We store the nodes and Huffman codes.
"""


"""
8. Greedy Algorithm for Egyptian Fraction
Problem:
Given a fraction num/den, find its Egyptian Fraction representation. An Egyptian Fraction is a sum of distinct unit fractions where each fraction
has a numerator of 1, i.e., 1/x.

Example:
Input: num = 6, den = 14
Output: [1/3, 1/11, 1/231]
Explanation: The fraction 6/14 can be represented as 1/3 + 1/11 + 1/231.
"""
class Solution:
    def egyptian_fraction(self, num: int, den: int) -> List[str]:
        result = []  # List to store the result fractions
        
        # Continue until the numerator becomes 0
        while num != 0:
            # Find the ceiling of den/num to get the next unit fraction
            x = (den + num - 1) // num
            
            # Append the unit fraction to the result
            result.append(f"1/{x}")
            
            # Update num and den for the next fraction
            num = num * x - den
            den = den * x
        
        return result
# Example usage
solution = Solution()
num = 6
den = 14
print(solution.egyptian_fraction(num, den))  # Output: [3, 11, 231]
"""
Time Complexity: O(n), where n is the number of unit fractions generated.
Space Complexity: O(n), where n is the number of unit fractions stored in the result.
"""

"""
9. Greedy Algorithm to Minimize the Maximum Difference Between Heights
Problem:
Given heights of towers and an integer k, you are allowed to either increase or decrease the height of each tower by k (only once).
Your task is to minimize the difference between the highest and the lowest towers after the modification.

Example:
Input: heights = [1, 5, 15, 10], k = 3
Output: 8
Explanation: We can increase 1 to 4 and decrease 15 to 12, resulting in the heights [4, 5, 10, 12] with a difference of 12 - 4 = 8.

"""
class Solution:
    def minimize_difference(self, heights: List[int], k: int) -> int:
        # Step 1: Sort the array to process heights in order
        heights.sort()
        
        # Step 2: Calculate the initial difference between max and min heights
        n = len(heights)
        initial_difference = heights[-1] - heights[0]
        
        # Step 3: Iterate through the array to find the minimized difference
        min_difference = initial_difference
        for i in range(n - 1):
            # Adjust heights[i] and heights[i+1] for potential new min and max
            new_max = max(heights[-1] - k, heights[i] + k)
            new_min = min(heights[0] + k, heights[i + 1] - k)
            
            # Update the minimum difference
            min_difference = min(min_difference, new_max - new_min)
        
        return min_difference


# Example usage:
solution = Solution()
heights = [1, 5, 15, 10]
k = 3
result = solution.minimize_difference(heights, k)
print(f"Minimum difference: {result}")

    
"""Time Complexity: O(n log n)
We sort the array first and then iterate through it once.
Space Complexity: O(1)
We use only a few extra variables.
"""

"""
10. Largest Number
Problem:
Given a list of non-negative integers, arrange them such that they form the largest possible number. The result should be a string.

Example:
Input: nums = [3, 30, 34, 5, 9]
Output: "9534330"
Explanation: By arranging the numbers as "9534330", we form the largest possible number.
"""
from functools import cmp_to_key

from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Rearrange numbers to form the largest number.
        
        Parameters:
        nums (List[int]): List of non-negative integers.

        Returns:
        str: Largest possible number as a string.
        """
        # Convert all integers to strings
        nums_str = list(map(str, nums))
        
        # Custom sort based on the order of concatenation
        nums_str.sort(key=lambda x: x*10, reverse=True)
        
        # Join sorted strings into the final number
        result = ''.join(nums_str)
        
        # Handle edge case where the result is multiple zeros (e.g., [0, 0])
        return '0' if result[0] == '0' else result


# Example usage
solution = Solution()
nums = [3, 30, 34, 5, 9]
print(solution.largestNumber(nums))  # Output: "9534330"


# The above is the most correct way where the below is the most simplest way
def convert_large_number(nums):

    nums_string = "".join(str(num) for num in nums)

    sorted_nums_string = "".join(sorted(nums_string, reverse=True))
    
    return sorted_nums_string

nums = [3, 30, 34, 5, 9]

large = convert_large_number(nums)

print(large)

"""
Time Complexity: O(n log n)
We sort the numbers based on the custom comparator.
Space Complexity: O(n)
We store the numbers as strings.
"""

"""
11. Best Time to Buy and Sell Stock (Single Transaction)
Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the 𝑖 𝑡ℎ  day.
You want to maximize your profit by choosing a single day to buy one stock and a different day to sell.
Return the maximum profit you can achieve. If no profit is possible, return 0.

Example:
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.

Input: prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: In this case, no transactions are done, and the maximum profit is 0.
"""

"""
Type: Greedy
Time Complexity: 
O(n)
Space Complexity: 
O(1)
"""
class Solution:
    def maxProfit(self, prices):
        """
        Find the maximum profit from a single stock transaction.
        
        Args:
        prices (List[int]): Stock prices
        
        Returns:
        int: Maximum profit
        """
        min_price = float('inf')  # Minimum price seen so far
        max_profit = 0  # Maximum profit found so far

        for price in prices:
            min_price = min(min_price, price)  # Update minimum price
            max_profit = max(max_profit, price - min_price)  # Update maximum profit
        
        return max_profit

# Test
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5


"""
12. Best Time to Buy and Sell Stock II (Multiple Transactions)
Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the i th day.
You can perform as many transactions as you like (buy one and sell one share of the stock multiple times).
Return the maximum profit you can achieve.

Example:
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 7
Explanation: Buy on day 2 (price = 1), sell on day 3 (price = 5), profit = 4. Then buy on day 4 (price = 3), sell on day 5 (price = 6), profit = 3.

Input: prices = [1, 2, 3, 4, 5]
Output: 4
Explanation: Buy on day 1 (price = 1), sell on day 5 (price = 5).
"""
"""
Type: Greedy
Time Complexity: 
O(n)
Space Complexity: 
O(1)
"""

class Solution:
    def maxProfit(self, prices):
        """
        Find the maximum profit from multiple stock transactions.
        
        Args:
        prices (List[int]): Stock prices
        
        Returns:
        int: Maximum profit
        """
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:  # Sell every profitable transaction
                profit += prices[i] - prices[i-1]
        
        return profit

# Test
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 7

"""
Technique: Greedy Algorithm (Load Balancing - Manual Min Selection)

Statement: Assign tasks to workers such that no worker is overloaded. Each task has a certain workload, and each worker has a capacity.

Example Input:
tasks = [2, 3, 4]  # Workload of each task
workers = [5, 5]    # Capacity of each worker
"""

def assign_tasks(tasks, workers):
    tasks.sort(reverse=True)  # Sort tasks in descending order
    worker_loads = [0] * len(workers)  # Track each worker's assigned load

    for task in tasks:
        # Find the worker with the minimum current load who can take the task
        min_worker = -1
        min_load = float('inf')
        
        for i in range(len(workers)):
            if worker_loads[i] + task <= workers[i] and worker_loads[i] < min_load:
                min_worker = i
                min_load = worker_loads[i]

        if min_worker == -1:  # No worker can take this task
            return "Task assignment not possible"

        worker_loads[min_worker] += task  # Assign task to the selected worker

    return worker_loads

tasks = [2, 3, 4]
workers = [5, 5]
print(assign_tasks(tasks, workers))  # Output: [5, 4] or [4, 5] (valid distributions)

"""
Technique: Greedy Algorithm (Interval Scheduling with Room Assignment)
Statement: Schedule meetings in rooms such that no two meetings overlap in the same room.

Example Input:
meetings = [(1, 4), (3, 5), (6, 8)]  # (start, end) times
rooms = 2                              # Number of room
"""
def schedule_meetings(meetings, rooms):
    meetings.sort()  # Sort by start time
    room_end_times = [0] * rooms  # Track when each room is free

    for start, end in meetings:
        assigned = False
        
        for i in range(rooms):  # Try to place the meeting in an available room
            if room_end_times[i] <= start:  # Room is free
                room_end_times[i] = end  # Assign the room
                assigned = True
                break

        if not assigned:  # If no room is free
            return "Not enough rooms available"

    return "Meetings scheduled successfully"

meetings = [(1, 4), (3, 5), (6, 8)]
rooms = 2
print(schedule_meetings(meetings, rooms))  # Output: "Meetings scheduled successfully"

"""
Statement: Plan a travel itinerary such that the total cost does not exceed the budget and all destinations are visited.

Example Input:

destinations = [("Paris", 500), ("London", 400), ("Rome", 300)]  # (destination, cost)
budget = 1000
"""

def plan_itinerary(destinations, budget):
    destinations.sort(key=lambda x: x[1])  # Sort by cost (ascending)
    itinerary = []
    total_cost = 0

    for city, cost in destinations:
        if total_cost + cost <= budget:  # Check if we can afford this destination
            itinerary.append(city)
            total_cost += cost
        else:
            break  # Stop if we exceed the budget

    return itinerary, total_cost  # Return planned itinerary and total cost

# Example Input
destinations = [("Paris", 500), ("London", 400), ("Rome", 300)]
budget = 1000

# Output
itinerary, total_spent = plan_itinerary(destinations, budget)
print("Planned Itinerary:", itinerary)  # Example Output: ['Rome', 'London']
print("Total Cost:", total_spent)  # Example Output: 700


