"""
Problem 1: Task Scheduling
Problem Statement: You are given a list of tasks with their respective deadlines and execution times. Schedule the tasks in such a way 
that the maximum lateness is minimized. Use a min-heap to prioritize tasks with the earliest deadlines.

Example Input:

tasks = [
    {"name": "Task1", "deadline": 5, "execution_time": 2},
    {"name": "Task2", "deadline": 3, "execution_time": 1},
    {"name": "Task3", "deadline": 8, "execution_time": 3}
]
"""

import heapq

def schedule_tasks(tasks):
    """
    Schedules tasks to minimize maximum lateness using a min-heap.
    :param tasks: List of tasks with deadlines and execution times.
    :return: List of scheduled tasks.
    """
    # Sort tasks by deadline (earliest deadline first)
    tasks.sort(key=lambda x: x["deadline"])
    
    # Min-heap to store the execution times of scheduled tasks
    heap = []
    current_time = 0
    
    for task in tasks:
        execution_time = task["execution_time"]
        deadline = task["deadline"]
        
        # Push the execution time into the heap
        heapq.heappush(heap, execution_time)
        current_time += execution_time
        
        # If the current time exceeds the deadline, remove the task with the longest execution time
        if current_time > deadline:
            longest_task = heapq.heappop(heap)
            current_time -= longest_task
    
    # The heap now contains the optimal schedule
    return [task for task in tasks if task["execution_time"] in heap]

# Example usage
tasks = [
    {"name": "Task1", "deadline": 5, "execution_time": 2},
    {"name": "Task2", "deadline": 3, "execution_time": 1},
    {"name": "Task3", "deadline": 8, "execution_time": 3}
]
print(schedule_tasks(tasks))

# Time Complexity: O(N log N), where N is the number of tasks.
# Space Complexity: O(N), for the heap.

"""
Problem 2: Merging K Sorted Logs
Scenario:
A system collects logs from multiple servers. Each server's logs are sorted by timestamp. The goal is to merge all logs into a single sorted log file.

Example Input:
logs = [
    [(1, "Log A1"), (4, "Log A2"), (5, "Log A3")],
    [(2, "Log B1"), (3, "Log B2"), (6, "Log B3")],
    [(0, "Log C1"), (7, "Log C2")]
]
Each list represents logs from a different server, where each log entry is (timestamp, log_message).


"""
import heapq

def merge_logs(logs):
    """
    Merges k sorted log lists using a min heap.
    :param logs: List of sorted logs from different servers.
    :return: Merged sorted logs.
    """
    min_heap = []
    merged_logs = []

    # Push the first element of each log with index reference
    for i, log_list in enumerate(logs):
        if log_list:
            heapq.heappush(min_heap, (log_list[0][0], i, 0, log_list[0][1]))

    while min_heap:
        timestamp, list_idx, elem_idx, log_msg = heapq.heappop(min_heap)
        merged_logs.append((timestamp, log_msg))

        # Push next log from the same list
        if elem_idx + 1 < len(logs[list_idx]):
            heapq.heappush(min_heap, (logs[list_idx][elem_idx + 1][0], list_idx, elem_idx + 1, logs[list_idx][elem_idx + 1][1]))

    return merged_logs

# Example usage
logs = [
    [(1, "Log A1"), (4, "Log A2"), (5, "Log A3")],
    [(2, "Log B1"), (3, "Log B2"), (6, "Log B3")],
    [(0, "Log C1"), (7, "Log C2")]
]

print(merge_logs(logs))

"""
Problem 3: Find the Kth Largest Element
Statement: Given an array of integers, find the kth largest element.

Example Input:
nums = [3, 2, 1, 5, 6, 4]
k = 2
"""
import heapq

def find_kth_largest(nums, k):
    """
    Finds the kth largest element using a min-heap.
    Time Complexity: O(n log k).
    Space Complexity: O(k) for the heap.
    """
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # Remove the smallest element
    return min_heap[0]

# Example Usage
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k))  # Output: 5

"""
Problem 3: Finding Top K Frequent Words
Scenario:
A social media analytics platform wants to identify the top K most frequent words from user posts.

Example Input:
words = ["apple", "banana", "apple", "orange", "banana", "apple", "grape"]
k = 2
Find the top 2 most frequent words.
"""
from collections import Counter
import heapq

def top_k_frequent(words, k):
    """
    Returns the top k most frequent words.
    :param words: List of words.
    :param k: Number of top frequent words to return.
    :return: List of top k frequent words.
    """
    freq_map = Counter(words)
    min_heap = []

    # Push (frequency, word) into a min heap
    for word, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, word))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return sorted([heapq.heappop(min_heap)[1] for _ in range(k)], reverse=True)

# Example usage
words = ["apple", "banana", "apple", "orange", "banana", "apple", "grape"]
k = 2
print(top_k_frequent(words, k))


"""
Problem 5: Minimum Cost to Connect Ropes
Statement: Given n ropes of different lengths, connect them into one rope with minimum cost. The cost of connecting two ropes is equal to 
the sum of their lengths.

Example Input:
"""

ropes = [4, 3, 2, 6]

import heapq

def min_cost_to_connect_ropes(ropes):
    """
    Calculates the minimum cost to connect all ropes using a min-heap.
    Time Complexity: O(n log n).
    Space Complexity: O(n) for the heap.
    """
    heapq.heapify(ropes)  # Convert list into a min-heap
    total_cost = 0
    while len(ropes) > 1:
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)
        cost = first + second
        total_cost += cost
        heapq.heappush(ropes, cost)
    return total_cost

# Example Usage
ropes = [4, 3, 2, 6]
print(min_cost_to_connect_ropes(ropes))  # Output: 29
"""
Problem 6: Sliding Window Maximum
Statement: Given an array and a window size k, find the maximum element in each sliding window.

Example Input:
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
"""
import heapq

def sliding_window_max(nums, k):
    """
    Finds the maximum in each sliding window using a max-heap.
    Time Complexity: O(n log n).
    Space Complexity: O(n) for the heap.
    """
    result = []
    max_heap = []
    for i, num in enumerate(nums):
        heapq.heappush(max_heap, (-num, i))  # Use negative for max-heap
        while max_heap[0][1] <= i - k:
            heapq.heappop(max_heap)  # Remove elements outside the window
        if i >= k - 1:
            result.append(-max_heap[0][0])
    return result

# Example Usage
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_max(nums, k))  # Output: [3, 3, 5, 5, 6, 7]

"""
Problem 7: K Closest Points to Origin
Statement: Given a list of points on a plane, find the k closest points to the origin.
Given a list of points on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2)
is calculated using the Euclidean distance formula:

Example Input:
points = [(1, 3), (-2, 2), (5, 8), (0, 1)]
k = 2
 Output: 
 
[(-2, 2), (0, 1)]
"""
def k_closest_points(points, k):
    """
    Finds the k closest points to the origin using a max-heap.
    Time Complexity: O(n log k).
    Space Complexity: O(k) for the heap.
    """
    max_heap = []
    for x, y in points:
        distance = -(x**2 + y**2)  # Use negative for max-heap
        heapq.heappush(max_heap, (distance, x, y))
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return [(x, y) for distance, x, y in max_heap]

# Example Usage
points = [(1, 3), (-2, 2), (5, 8), (0, 1)]
k = 2
print(k_closest_points(points, k))  # Output: [(-2, 2), (0, 1)]

def k_closest_points(points, k):
    # Calculate squared distances and store them with the points
    points_with_distances = [(x**2 + y**2, (x, y)) for x, y in points]
    
    # Sort the points based on the squared distance
    points_with_distances.sort(key=lambda x: x[0])
    
    # Extract the first k points
    closest_points = [point for (_, point) in points_with_distances[:k]]
    
    return closest_points

# Example usage:
points = [(1, 3), (-2, 2), (5, 8), (0, 1)]
k = 2
print(k_closest_points(points, k))  # Output: [(-2, 2), (0, 1)]

"""
Problem 8: Median of a Data Stream
Statement:
Design a data structure that can efficiently find the median of a stream of integers. The median is the middle value in 
an ordered list of numbers. If the list has an odd number of elements, the median is the middle element. If the list has 
an even number of elements, the median is the average of the two middle elements.

The data structure should support two operations:

addNum(int num): Adds an integer num to the data structure.

findMedian(): Returns the median of all the numbers added so far.

Example Input:
stream = [5, 15, 1, 3]

Example Output:
# After adding 5:
Median = 5

# After adding 15:
Median = (5 + 15) / 2 = 10

# After adding 1:
Median = 5

# After adding 3:
Median = (3 + 5) / 2 = 4
"""
import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # Stores the smaller half
        self.min_heap = []  # Stores the larger half

    def add_num(self, num):
        """
        Adds a number to the data structure.
        Time Complexity: O(log n).
        """
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self):
        """
        Finds the median of the data stream.
        Time Complexity: O(1).
        """
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2

# Example Usage
mf = MedianFinder()
stream = [5, 15, 1, 3]
for num in stream:
    mf.add_num(num)
print(mf.find_median())  # Output: 4.0


"""
Problem 10: Kth Smallest Element in a Sorted Matrix
Statement: Given a sorted matrix, find the kth smallest element.

Example Input:
matrix = [
  [1, 5, 9],
  [10, 11, 13],
  [12, 13, 15]
]
k = 8
"""
import heapq

def kth_smallest(matrix, k):
    """
    Finds the kth smallest element in a sorted matrix using a min-heap.
    Time Complexity: O(n log n).
    Space Complexity: O(n) for the heap.
    """
    min_heap = []
    for row in matrix:
        for num in row:
            heapq.heappush(min_heap, num)
    for _ in range(k - 1):
        heapq.heappop(min_heap)
    return heapq.heappop(min_heap)

# Example Usage
matrix = [
  [1, 5, 9],
  [10, 11, 13],
  [12, 13, 15]
]
k = 8
print(kth_smallest(matrix, k))  # Output: 13