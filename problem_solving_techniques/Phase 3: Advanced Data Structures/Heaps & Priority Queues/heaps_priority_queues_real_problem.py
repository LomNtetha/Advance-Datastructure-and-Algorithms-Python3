"""
Problem 1: Task Scheduling with Priority
Statement: You are given a list of tasks with their priorities. Schedule the tasks in order of priority (highest priority first).

Example Input:
tasks = [("Task A", 3), ("Task B", 1), ("Task C", 2)]
"""
import heapq

def schedule_tasks(tasks):
    """
    Schedules tasks based on priority using a max-heap.
    Time Complexity: O(n log n) for heap construction, O(n log n) for extraction.
    Space Complexity: O(n) for the heap.
    """
    # Use a max-heap by negating priorities
    max_heap = [(-priority, task) for task, priority in tasks]
    heapq.heapify(max_heap)  # Convert list into a heap, O(n) time

    scheduled_tasks = []
    while max_heap:
        priority, task = heapq.heappop(max_heap)  # Extract the highest priority task
        scheduled_tasks.append(task)
    
    return scheduled_tasks

# Example Usage
tasks = [("Task A", 3), ("Task B", 1), ("Task C", 2)]
print(schedule_tasks(tasks))  # Output: ['Task A', 'Task C', 'Task B']

"""
Problem 2: Merge K Sorted Lists
Statement: Given k sorted lists, merge them into a single sorted list.

Example Input:
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]

"""
import heapq

def merge_k_sorted_lists(lists):
    """
    Merges k sorted lists into one sorted list using a min-heap.
    Time Complexity: O(n log k), where n is the total number of elements.
    Space Complexity: O(k) for the heap.
    """
    min_heap = []
    merged_list = []

    # Push the first element of each list into the heap
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))  # (value, list index, element index)

    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(val)
        if element_idx + 1 < len(lists[list_idx]):
            heapq.heappush(min_heap, (lists[list_idx][element_idx + 1], list_idx, element_idx + 1))

    return merged_list

# Example Usage
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
print(merge_k_sorted_lists(lists))  # Output: [1, 1, 2, 3, 4, 4, 5, 6]
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
Problem 4: Top K Frequent Elements
Statement: Given an array of integers, return the k most frequent elements.

Example Input:
nums = [1, 1, 1, 2, 2, 3]
k = 2
"""
import heapq
from collections import Counter

def top_k_frequent(nums, k):
    """
    Finds the k most frequent elements using a min-heap.
    Time Complexity: O(n log k).
    Space Complexity: O(n) for the frequency map and heap.
    """
    freq_map = Counter(nums)
    min_heap = []
    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return [num for freq, num in min_heap]

# Example Usage
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(nums, k))  # Output: [2, 1]

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

Example Input:
points = [(1, 3), (-2, 2), (5, 8), (0, 1)]
k = 2
Solution:
import heapq
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

"""
Problem 8: Median of a Data Stream
Statement: Design a data structure to find the median of a stream of integers.

Example Input:
stream = [5, 15, 1, 3]
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
Problem 9: Maximum Number of Events
Statement: Given a list of events with start and end times, find the maximum number of events you can attend.

Example Input:
events = [(1, 4), (4, 6), (2, 5)]

"""
import heapq

def max_events(events):
    """
    Finds the maximum number of events you can attend using a min-heap.
    Time Complexity: O(n log n).
    Space Complexity: O(n) for the heap.
    """
    events.sort()
    min_heap = []
    count = 0
    day = 1
    i = 0
    while i < len(events) or min_heap:
        while i < len(events) and events[i][0] == day:
            heapq.heappush(min_heap, events[i][1])
            i += 1
        while min_heap and min_heap[0] < day:
            heapq.heappop(min_heap)
        if min_heap:
            heapq.heappop(min_heap)
            count += 1
        day += 1
    return count

# Example Usage
events = [(1, 4), (4, 6), (2, 5)]
print(max_events(events))  # Output: 2
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