"""
2. Activity Selection Problem
Problem:
Given n activities with their start and end times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on one activity at a time.

Example:
Input: start = [1, 3, 0, 5, 8, 5], end = [2, 4, 6, 7, 9, 9]
Output: 4
Explanation: The maximum set of non-overlapping activities are [0, 1], [3, 4], and [4, 5] (total 4 activities).

"""
from typing import Dict, List, Tuple


class Solution:
    def max_activities(self, start: List[int], end: List[int]) -> int:
        # Sort activities by their finish times
        activities = sorted(zip(start, end), key=lambda x: x[1])
        
        # The first activity is always selected
        last_end_time = activities[0][1]
        count = 1  # We've selected the first activity
        
        # Iterate over the remaining activities
        for i in range(1, len(activities)):
            # If the current activity starts after the last selected activity ends, select it
            if activities[i][0] >= last_end_time:
                count += 1
                # Update last_end_time to the end time of the current activity
                last_end_time = activities[i][1]
        
        # Return the maximum number of activities that can be performed
        return count
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
        # Calculate value-to-weight ratio and sort items in descending order
        items = sorted([(v / w, w) for v, w in zip(values, weights)], reverse=True)
        
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
"""
Time Complexity: O(n log n)
We sort the items based on their value-to-weight ratio.
Space Complexity: O(n)
We store the sorted list of items.
"""

"""
4. Minimum Number of Platforms Required for a Railway Station
Problem:
Given the arrival and departure times of trains at a railway station, find the minimum number of platforms required to accommodate all trains without delay.

Example:
Input: arrival = [9:00, 9:40, 9:50, 11:00, 15:00, 18:00], departure = [9:10, 12:00, 11:20, 11:30, 19:00, 20:00]
Output: 3
Explanation: At peak time (around 11:00), there are 3 trains at the station.

"""
class Solution:
    def min_platforms(self, arrival: List[int], departure: List[int]) -> int:
        # Sort arrival and departure times
        arrival.sort()
        departure.sort()
        
        platforms = 1  # Minimum platforms needed
        result = 1  # Final result (maximum platforms required)
        i = 1  # Pointer for arrival
        j = 0  # Pointer for departure
        
        # Traverse the arrival and departure lists
        while i < len(arrival) and j < len(departure):
            # If next train is arriving before the current one departs, increase platform count
            if arrival[i] <= departure[j]:
                platforms += 1
                i += 1
            else:
                # If a train departs, reduce platform count
                platforms -= 1
                j += 1
            
            # Update the result if the current number of platforms is the maximum so far
            result = max(result, platforms)
        
        # Return the minimum number of platforms required
        return result
    
# Example usage
solution = Solution()
arrival = [900, 940, 950, 1100, 1500, 1800]  # Arrival times in 24-hour format
departure = [910, 1200, 1120, 1130, 1900, 2000]  # Departure times in 24-hour format

# Calculate and print the result
print("Minimum platforms required:", solution.min_platforms(arrival, departure))


"""
Time Complexity: O(n log n)
We sort the arrival and departure times.
Space Complexity: O(1)
We use only a few extra variables.
"""

"""
5. Job Sequencing Problem
Problem:
Given n jobs with their deadlines and profits, find the sequence of jobs that maximizes the total profit. Each job takes 1 unit of time, and a job must be completed by its deadline.

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
                distance = current_distance + weight
                
                # If a shorter distance is found, update and push it to the heap
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))
        
        # Return the distances from the source to all other nodes
        return [distances[i] for i in range(len(graph))]
"""      
Time Complexity: O(E log V)
Where E is the number of edges and V is the number of vertices.
Space Complexity: O(V)
We use space to store distances and the heap.
"""


"""
7. Huffman Encoding
Problem:
Given a set of characters and their frequencies, your task is to build a Huffman Tree and determine the optimal binary code for each character, such that the total encoding length is minimized.

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
Given a fraction num/den, find its Egyptian Fraction representation. An Egyptian Fraction is a sum of distinct unit fractions where each fraction has a numerator of 1, i.e., 1/x.

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
"""
Time Complexity: O(n), where n is the number of unit fractions generated.
Space Complexity: O(n), where n is the number of unit fractions stored in the result.
"""

"""
9. Greedy Algorithm to Minimize the Maximum Difference Between Heights
Problem:
Given heights of towers and an integer k, you are allowed to either increase or decrease the height of each tower by k (only once). Your task is to minimize the difference between the highest and the lowest towers after the modification.

Example:
Input: heights = [1, 5, 15, 10], k = 3
Output: 8
Explanation: We can increase 1 to 4 and decrease 15 to 12, resulting in the heights [4, 5, 10, 12] with a difference of 12 - 4 = 8.

"""
class Solution:
    def minimize_max_difference(self, heights: List[int], k: int) -> int:
        n = len(heights)
        if n == 1:
            return 0  # If there's only one tower, no modification is needed
        
        # Sort the heights to consider smallest and largest heights
        heights.sort()
        
        # Initialize the maximum difference before any changes
        max_diff = heights[-1] - heights[0]
        
        # Iterate through the sorted array and adjust the heights
        for i in range(1, n):
            min_height = min(heights[0] + k, heights[i] - k)
            max_height = max(heights[-1] - k, heights[i - 1] + k)
            max_diff = min(max_diff, max_height - min_height)
        
        return max_diff
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

class Solution:
    def largest_number(self, nums: List[int]) -> str:
        # Custom comparator to compare which combination forms a larger number
        def compare(x, y):
            # Combine x and y in two possible orders and compare them
            if x + y > y + x:
                return -1  # If x + y is greater, x should come first
            else:
                return 1  # Otherwise, y should come first
        
        # Convert the integers to strings to facilitate comparison
        nums_str = list(map(str, nums))
        
        # Sort the numbers based on the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # Edge case: If the largest number is 0, return "0"
        if nums_str[0] == '0':
            return '0'
        
        # Join the sorted numbers to form the largest number
        return ''.join(nums_str)
"""
Time Complexity: O(n log n)
We sort the numbers based on the custom comparator.
Space Complexity: O(n)
We store the numbers as strings.
"""

"""
Problem Setup:
Suppose we have coin denominations of 25, 10, 5, and 1 (as in U.S. currency) and need to make 41 cents. Our goal is to use as few coins as possible to reach this amount.

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
            if amount >= coin:
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