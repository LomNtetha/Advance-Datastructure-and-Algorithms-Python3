"""
1. Implement Min Heap
Problem Statement:
Implement a min heap class that supports the following operations:

insert: Inserts a value into the heap.
extract_min: Removes and returns the smallest element from the heap.
peek: Returns the smallest element without removing it.
size: Returns the size of the heap.
Solution:

"""
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return min_val

    def peek(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

# Example
min_heap = MinHeap()
min_heap.insert(3)
min_heap.insert(2)
min_heap.insert(1)
print(min_heap.extract_min())  # Output: 1
print(min_heap.peek())         # Output: 2

"""
2. Implement Max Heap
Problem Statement:
Implement a max heap class that supports the same operations as the min heap class (insert, extract_max, peek, size).

Solution:

"""
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return max_val

    def peek(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

# Example
max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(2)
max_heap.insert(1)
print(max_heap.extract_max())  # Output: 3
print(max_heap.peek())         # Output: 2
"""

3. Implement Priority Queue
Problem Statement:
Implement a priority queue class using a heap, which supports enqueue and dequeue operations.

Solution:
"""
import heapq

class PriorityQueue:
    def __init__(self):
        self.pq = []
        self.counter = 0

    def enqueue(self, val, priority):
        heapq.heappush(self.pq, (priority, self.counter, val))
        self.counter += 1

    def dequeue(self):
        if self.pq:
            return heapq.heappop(self.pq)[2]
        return None

    def peek(self):
        return self.pq[0][2] if self.pq else None

# Example
pq = PriorityQueue()
pq.enqueue("task1", 1)
pq.enqueue("task2", 3)
pq.enqueue("task3", 2)
print(pq.dequeue())  # Output: "task1"
"""
4. Find Kth Largest Element Using a Min Heap
Problem Statement:
Find the kth largest element in an array using a min heap.

Solution:
"""
import heapq

class Solution:
    def find_kth_largest(self, nums, k):
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]

# Example
sol = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(sol.find_kth_largest(nums, k))  # Output: 5

"""
5. Find Kth Smallest Element Using a Max Heap
Problem Statement:
Find the kth smallest element in an array using a max heap.

Solution:
"""

import heapq

class Solution:
    def find_kth_smallest(self, nums, k):
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return -max_heap[0]

# Example
sol = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(sol.find_kth_smallest(nums, k))  # Output: 2

"""
6. Kth Largest Element in an Array (Using Sorting)
Problem Statement:
Find the kth largest element in an array using sorting.
"""

class Solution:
    def find_kth_largest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k - 1]

# Example
sol = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(sol.find_kth_largest(nums, k))  # Output: 5

"""
7. Check if a Binary Heap is a Max Heap
Problem Statement:
Check if a given binary heap is a max heap.
"""

class Solution:
    def is_max_heap(self, arr):
        n = len(arr)
        for i in range(n // 2):
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            if left_child < n and arr[i] < arr[left_child]:
                return False
            if right_child < n and arr[i] < arr[right_child]:
                return False
        return True

# Example
sol = Solution()
heap = [9, 6, 8, 4, 2, 7]
print(sol.is_max_heap(heap))  # Output: True

"""
8. Merge K Sorted Lists Using Min Heap
Problem Statement:
Given k sorted linked lists, merge them into one sorted linked list.
"""

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        min_heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i, l))

        dummy = ListNode()
        current = dummy

        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))

        return dummy.next

# Example
lists = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
sol = Solution()
merged = sol.mergeKLists(lists)
while merged:
    print(merged.val, end=" -> ")
    merged = merged.next

""""
9. Kth Largest Element in a Stream
Problem Statement:
Design a data structure to find the kth largest element in a stream of integers.


"""
import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val):
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]

# Example
kth_largest = KthLargest(3, [4, 5, 8, 2])
print(kth_largest.add(3))  # Output: 4
print(kth_largest.add(5))  # Output: 5

"""
10. Top K Frequent Elements
Problem Statement:
Given a non-empty array of integers, return the k most frequent elements.

"""

import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        min_heap = []
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [num for freq, num in min_heap]

# Example
sol = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(sol.topKFrequent(nums, k))  # Output: [1, 2]

"""
Using a priority queue is an efficient way to implement Dijkstra's algorithm. The priority queue helps keep track of the next node to process (the one with the smallest distance) in 
O(logV) time for each insertion and extraction, making the algorithm faster compared to a simple array or list for large graphs.


"""

import heapq
from typing import Dict, List, Tuple

class Solution:
    def dijkstra(self, graph: Dict[int, List[Tuple[int, int]]], source: int) -> List[int]:
        # Initialize distances as infinite for all nodes except the source
        num_nodes = len(graph)
        distances = [float('inf')] * num_nodes
        distances[source] = 0
        
        # Priority queue: stores (distance, node)
        priority_queue = [(0, source)]  # (distance to node, node index)
        
        while priority_queue:
            # Extract the node with the smallest distance
            current_distance, current_node = heapq.heappop(priority_queue)
            
            # If the current distance is greater than the stored distance, skip it (outdated entry)
            if current_distance > distances[current_node]:
                continue
            
            # Explore neighbors of the current node
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                
                # If a shorter path to the neighbor is found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances

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
source_node = 0

solution = Solution()
distances = solution.dijkstra(graph, source_node)
print(f"Shortest distances from node {source_node}: {distances}")

