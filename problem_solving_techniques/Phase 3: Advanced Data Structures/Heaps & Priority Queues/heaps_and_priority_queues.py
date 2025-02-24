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
    """
    A class to implement a Min-Heap data structure.
    The smallest element is always at the root.
    """
    
    def __init__(self):
        # Initialize an empty list to store heap elements.
        self.heap = []

    def insert(self, val):
        """
        Inserts a new value into the heap.
        Args:
            val (int): The value to be inserted.
        """
        # Add the new value to the end of the heap list.
        self.heap.append(val)
        # Restore the heap property by moving the new value up.
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        """
        Removes and returns the smallest element from the heap.
        Returns:
            int: The smallest value in the heap, or None if the heap is empty.
        """
        if len(self.heap) == 0:
            # If the heap is empty, return None.
            return None
        # The smallest value is at the root (index 0).
        min_val = self.heap[0]
        # Move the last element to the root to maintain structure.
        self.heap[0] = self.heap[-1]
        # Remove the last element (previously moved to the root).
        self.heap.pop()
        # Restore the heap property by moving the root value down.
        self._heapify_down(0)
        return min_val

    def peek(self):
        """
        Returns the smallest element in the heap without removing it.
        Returns:
            int: The smallest value in the heap, or None if the heap is empty.
        """
        return self.heap[0] if self.heap else None

    def size(self):
        """
        Returns the number of elements in the heap.
        Returns:
            int: The size of the heap.
        """
        return len(self.heap)

    def _heapify_up(self, index):
        """
        Restores the heap property by moving the element at the given index up.
        Args:
            index (int): The index of the element to heapify up.
        """
        while index > 0:
            # Calculate the parent index for the current element.
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                # Swap the current element with its parent if it's smaller.
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                # Update the index to continue heapifying up.
                index = parent_index
            else:
                # If the heap property is satisfied, stop heapifying.
                break

    def _heapify_down(self, index):
        """
        Restores the heap property by moving the element at the given index down.
        Args:
            index (int): The index of the element to heapify down.
        """
        while True:
            # Calculate the indices of the left and right children.
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            # Assume the current index has the smallest value.
            smallest = index

            # Check if the left child exists and is smaller than the current smallest.
            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index
            # Check if the right child exists and is smaller than the current smallest.
            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index
            # If the smallest value is not the current index, swap and continue heapifying.
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                # If the heap property is satisfied, stop heapifying.
                break

# Example usage of the MinHeap class
min_heap = MinHeap()
min_heap.insert(3)  # Insert the value 3 into the heap.
min_heap.insert(2)  # Insert the value 2 into the heap.
min_heap.insert(1)  # Insert the value 1 into the heap.
print(min_heap.extract_min())  # Output: 1 (smallest element removed from the heap)
print(min_heap.peek())         # Output: 2 (smallest element now at the root)


"""
2. Implement Max Heap
Problem Statement:
Implement a max heap class that supports the same operations as the min heap class (insert, extract_max, peek, size).

Solution:

"""
class MaxHeap:
    """
    A class to implement a Max-Heap data structure.
    The largest element is always at the root.
    """
    
    def __init__(self):
        # Initialize an empty list to store heap elements.
        self.heap = []

    def insert(self, val):
        """
        Inserts a new value into the heap.
        Args:
            val (int): The value to be inserted.
        """
        # Add the new value to the end of the heap list.
        self.heap.append(val)
        # Restore the heap property by moving the new value up.
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        """
        Removes and returns the largest element from the heap.
        Returns:
            int: The largest value in the heap, or None if the heap is empty.
        """
        if len(self.heap) == 0:
            # If the heap is empty, return None.
            return None
        # The largest value is at the root (index 0).
        max_val = self.heap[0]
        # Move the last element to the root to maintain structure.
        self.heap[0] = self.heap[-1]
        # Remove the last element (previously moved to the root).
        self.heap.pop()
        # Restore the heap property by moving the root value down.
        self._heapify_down(0)
        return max_val

    def peek(self):
        """
        Returns the largest element in the heap without removing it.
        Returns:
            int: The largest value in the heap, or None if the heap is empty.
        """
        return self.heap[0] if self.heap else None

    def size(self):
        """
        Returns the number of elements in the heap.
        Returns:
            int: The size of the heap.
        """
        return len(self.heap)

    def _heapify_up(self, index):
        """
        Restores the heap property by moving the element at the given index up.
        Args:
            index (int): The index of the element to heapify up.
        """
        while index > 0:
            # Calculate the parent index for the current element.
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                # Swap the current element with its parent if it's larger.
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                # Update the index to continue heapifying up.
                index = parent_index
            else:
                # If the heap property is satisfied, stop heapifying.
                break

    def _heapify_down(self, index):
        """
        Restores the heap property by moving the element at the given index down.
        Args:
            index (int): The index of the element to heapify down.
        """
        while True:
            # Calculate the indices of the left and right children.
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            # Assume the current index has the largest value.
            largest = index

            # Check if the left child exists and is larger than the current largest.
            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
                largest = left_child_index
            # Check if the right child exists and is larger than the current largest.
            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
                largest = right_child_index
            # If the largest value is not the current index, swap and continue heapifying.
            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                # If the heap property is satisfied, stop heapifying.
                break

# Example usage of the MaxHeap class
max_heap = MaxHeap()
max_heap.insert(3)  # Insert the value 3 into the heap.
max_heap.insert(2)  # Insert the value 2 into the heap.
max_heap.insert(1)  # Insert the value 1 into the heap.
print(max_heap.extract_max())  # Output: 3 (largest element removed from the heap)
print(max_heap.peek())         # Output: 2 (largest element now at the root)


class MaxHeap:
    """
    A class to implement a Max-Heap data structure.
    The largest element is always at the root.
    """

    def __init__(self):
        # Initialize an empty list to store heap elements.
        self.heap = []

    def insert(self, val):
        """
        Inserts a new value into the heap.
        
        Question: 
        What happens when we insert a value into the MaxHeap?

        Example:
        Input: Insert 5 into the MaxHeap.
        Before: []
        After: [5]

        Input: Insert 3 into the MaxHeap.
        Before: [5]
        After: [5, 3]

        Input: Insert 7 into the MaxHeap.
        Before: [5, 3]
        After: [7, 3, 5]
        """
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        """
        Removes and returns the largest element from the heap.
        
        Question:
        What is the result of extracting the maximum value from the MaxHeap?

        Example:
        Input: Heap = [7, 3, 5]
        Operation: Extract Max
        Output: 7
        After: [5, 3]

        Input: Heap = [5, 3]
        Operation: Extract Max
        Output: 5
        After: [3]
        """
        if len(self.heap) == 0:
            return None
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return max_val

    def peek(self):
        """
        Returns the largest element in the heap without removing it.
        
        Question:
        How can we check the maximum value in the MaxHeap without removing it?

        Example:
        Input: Heap = [7, 3, 5]
        Operation: Peek
        Output: 7
        """
        return self.heap[0] if self.heap else None

    def size(self):
        """
        Returns the number of elements in the heap.
        
        Question:
        How many elements are currently in the MaxHeap?

        Example:
        Input: Heap = [7, 3, 5]
        Operation: Size
        Output: 3
        """
        return len(self.heap)

    def _heapify_up(self, index):
        """
        Restores the heap property by moving the element at the given index up.
        
        Question:
        What happens during the "heapify up" process?

        Example:
        Input: Heap = [5, 3], Index = 2, Inserted Value = 7
        Before: [5, 3, 7]
        After: [7, 3, 5] (7 swapped with 5)
        """
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        """
        Restores the heap property by moving the element at the given index down.
        
        Question:
        What happens during the "heapify down" process?

        Example:
        Input: Heap = [3, 5], Root Value = 3
        Before: [3, 5]
        After: [5, 3] (5 swapped with 3)
        """
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
                largest = left_child_index
            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
                largest = right_child_index
            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

# Example usage of the MaxHeap class
max_heap = MaxHeap()

# Insert elements
max_heap.insert(3)  # Insert the value 3 into the heap.
max_heap.insert(2)  # Insert the value 2 into the heap.
max_heap.insert(1)  # Insert the value 1 into the heap.
max_heap.insert(7)  # Insert the value 7 into the heap.

# Extract the maximum element
print(max_heap.extract_max())  # Output: 7 (largest element removed from the heap)

# Peek the maximum element
print(max_heap.peek())         # Output: 3 (largest element now at the root)


"""

3. Implement Priority Queue
Problem Statement:
Implement a priority queue class using a heap, which supports enqueue and dequeue operations.

Solution:
"""
import heapq

class PriorityQueue:
    """
    A class to represent a priority queue using a heap.
    Elements are dequeued based on their priority, with lower numbers having higher priority.
    """

    def __init__(self):
        """
        Initialize an empty priority queue.
        The priority queue uses a list (pq) to store elements and a counter to break ties.
        """
        self.pq = []  # The list to hold the elements of the priority queue
        self.counter = 0  # Counter to ensure stable sorting for elements with the same priority

    def enqueue(self, val, priority):
        """
        Add a new element to the priority queue.

        Parameters:
        val: The value to be added to the queue.
        priority: The priority of the value (lower numbers indicate higher priority).
        """
        # Push a tuple containing the priority, counter, and value onto the heap.
        # The counter ensures that elements with the same priority are dequeued in the order they were added.
        heapq.heappush(self.pq, (priority, self.counter, val))
        self.counter += 1  # Increment the counter for the next enqueue operation

    def dequeue(self):
        """
        Remove and return the element with the highest priority (lowest priority number).

        Returns:
        The value of the dequeued element, or None if the queue is empty.
        """
        if self.pq:  # Check if the priority queue is not empty
            return heapq.heappop(self.pq)[2]  # Remove and return the value (third element of the tuple)
        return None  # Return None if the queue is empty

    def peek(self):
        """
        Return the element with the highest priority without removing it.

        Returns:
        The value of the element with the highest priority, or None if the queue is empty.
        """
        return self.pq[0][2] if self.pq else None  # Access the value of the top element without popping it

# Example usage
pq = PriorityQueue()
pq.enqueue("task1", 1)  # Add "task1" with priority 1
pq.enqueue("task2", 3)  # Add "task2" with priority 3
pq.enqueue("task3", 2)  # Add "task3" with priority 2

# Dequeue and print the element with the highest priority (lowest priority number)
print(pq.dequeue())  # Output: "task1"

# Note: The elements are dequeued based on priority, so even though "task3" was added last,
# it will be dequeued before "task2" because it has a lower priority number.

"""
4. Find Kth Largest Element Using a Min Heap
Problem Statement:
Find the kth largest element in an array using a min heap.

Solution:
"""
import heapq

class Solution:
    """
    A class to solve the problem of finding the k-th largest element in an array.
    """

    def find_kth_largest(self, nums, k):
        """
        Find the k-th largest element in the given list `nums`.

        Parameters:
        nums (list[int]): The list of integers.
        k (int): The k-th position (1-based) of the largest element to find.

        Returns:
        int: The k-th largest element in the list.
        """
        min_heap = []  # Initialize an empty min heap (used to store the top `k` largest elements)

        # Iterate over each number in the input list
        for num in nums:
            # Add the current number to the min heap
            heapq.heappush(min_heap, num)

            # If the heap size exceeds `k`, remove the smallest element from the heap
            # This ensures the heap only contains the top `k` largest elements
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # The root of the min heap (index 0) is the k-th largest element
        return min_heap[0]

# Example usage
sol = Solution()

# Input list and the desired k-th largest element
nums = [3, 2, 1, 5, 6, 4]  # List of integers
k = 2                       # We want the 2nd largest element

# Output the result
print(sol.find_kth_largest(nums, k))  # Output: 5


"""
5. Find Kth Smallest Element Using a Max Heap
Problem Statement:
Find the kth smallest element in an array using a max heap.

Solution:
"""

import heapq

class Solution:
    """
    A class to solve the problem of finding the k-th smallest element in an array.
    """

    def find_kth_smallest(self, nums, k):
        """
        Find the k-th smallest element in the given list `nums`.

        Parameters:
        nums (list[int]): The list of integers.
        k (int): The k-th position (1-based) of the smallest element to find.

        Returns:
        int: The k-th smallest element in the list.
        """
        max_heap = []  # Initialize an empty max heap (implemented using negative values with heapq)

        # Iterate over each number in the input list
        for num in nums:
            # Add the negative of the current number to the max heap
            # This simulates a max heap using Python's default min-heap implementation
            heapq.heappush(max_heap, -num)

            # If the size of the heap exceeds `k`, remove the largest element (smallest negative value)
            # This ensures the heap only contains the top `k` smallest elements
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # The root of the max heap (index 0) is the negative of the k-th smallest element
        return -max_heap[0]

# Example usage
sol = Solution()

# Input list and the desired k-th smallest element
nums = [3, 2, 1, 5, 6, 4]  # List of integers
k = 2                       # We want the 2nd smallest element

# Output the result
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
    """
    A class representing a node in a singly linked list.
    
    Attributes:
    val (int): The value of the node.
    next (ListNode): A reference to the next node in the list.
    """
    def __init__(self, val=0, next=None):
        self.val = val  # Initialize the node's value
        self.next = next  # Initialize the next pointer to None by default


class Solution:
    """
    A class that provides a method to merge k sorted linked lists into one sorted linked list.
    """

    def mergeKLists(self, lists):
        """
        Merge k sorted linked lists into one sorted linked list.

        Parameters:
        lists (list[ListNode]): A list of ListNode objects, each representing the head of a sorted linked list.

        Returns:
        ListNode: The head of the merged sorted linked list.
        """
        min_heap = []  # Initialize an empty min-heap (priority queue)

        # Iterate over each of the k linked lists
        for i, l in enumerate(lists):
            if l:  # If the linked list is not empty
                # Push a tuple with (node's value, index of the list, and the node itself) into the heap
                # The index is used to distinguish nodes with the same value from different lists
                heapq.heappush(min_heap, (l.val, i, l))

        # Create a dummy node to simplify edge cases like empty lists
        dummy = ListNode()
        current = dummy  # A pointer to the last node in the merged list

        # While the heap is not empty, continue extracting the smallest element
        while min_heap:
            val, idx, node = heapq.heappop(min_heap)  # Pop the smallest node
            current.next = node  # Attach the current smallest node to the merged list
            current = current.next  # Move the pointer to the newly added node

            # If the popped node has a next node, push it into the heap to process next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))

        # Return the merged list, starting from the node after the dummy node
        return dummy.next

# Example usage:
# Create 3 sorted linked lists
lists = [
    ListNode(1, ListNode(4, ListNode(5))),  # List 1: 1 -> 4 -> 5
    ListNode(1, ListNode(3, ListNode(4))),  # List 2: 1 -> 3 -> 4
    ListNode(2, ListNode(6))                # List 3: 2 -> 6
]

# Initialize the Solution class and merge the lists
sol = Solution()
merged = sol.mergeKLists(lists)

# Print the merged sorted linked list
while merged:
    print(merged.val, end=" -> " if merged.next else "")  # Print the node value with an arrow if there's a next node
    merged = merged.next  # Move to the next node in the merged list


""""
9. Kth Largest Element in a Stream
Problem Statement:
Design a data structure to find the kth largest element in a stream of integers.


"""
import heapq

class KthLargest:
    """
    A class to maintain the k-th largest element in a stream of numbers.
    It supports adding new numbers and retrieving the k-th largest element at any time.
    """

    def __init__(self, k, nums):
        """
        Initialize the KthLargest object with a given k and an initial list of numbers.
        
        Parameters:
        k (int): The value of k, indicating that we are tracking the k-th largest element.
        nums (list[int]): A list of integers to initialize the KthLargest object.
        
        We use a min-heap to keep track of the k largest elements seen so far.
        """
        self.k = k  # Store the value of k
        self.min_heap = nums  # Initialize the heap with the given list of numbers
        heapq.heapify(self.min_heap)  # Convert the list into a valid heap structure
        
        # Ensure that the heap contains only k elements
        # If the heap size exceeds k, pop the smallest element
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val):
        """
        Add a new value to the stream and return the k-th largest element.
        
        Parameters:
        val (int): The new value to be added to the stream.
        
        Returns:
        int: The k-th largest element in the stream after adding the new value.
        
        We add the new value to the heap and if the heap exceeds size k, 
        we remove the smallest element.
        """
        heapq.heappush(self.min_heap, val)  # Push the new value into the heap
        
        # If the heap exceeds size k, remove the smallest element (the root of the min-heap)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        # The root of the min-heap is the k-th largest element
        return self.min_heap[0]

# Example usage:

# Initialize the KthLargest object with k = 3 and an initial list of numbers [4, 5, 8, 2]
kth_largest = KthLargest(3, [4, 5, 8, 2])

# Add a new number (3) and print the k-th largest element after the addition
# After adding 3, the 3rd largest element is 4
print(kth_largest.add(3))  # Output: 4

# Add another new number (5) and print the k-th largest element
# After adding 5, the 3rd largest element is 5
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
        """
        This method returns the top k most frequent elements in the list nums.
        
        Parameters:
        nums (list[int]): The input list of integers.
        k (int): The number of most frequent elements to return.
        
        Returns:
        list[int]: A list of the k most frequent elements in nums.
        """
        
        # Step 1: Count the frequency of each element in the nums list
        count = Counter(nums)  # Counter creates a dictionary where the keys are the elements, 
                                # and the values are their frequencies.
        
        # Step 2: Initialize a min-heap
        min_heap = []  # A min-heap will store elements as (frequency, element) tuples
        
        # Step 3: Iterate over the frequency dictionary
        for num, freq in count.items():
            # Push the (frequency, element) pair into the min-heap
            heapq.heappush(min_heap, (freq, num))  # heapq by default is a min-heap, which pops the smallest item
            
            # Step 4: Ensure the heap contains only k elements
            # If the heap size exceeds k, remove the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)  # Removes the element with the smallest frequency
        
        # Step 5: Extract the elements from the heap
        # We return only the elements, not their frequencies
        return [num for freq, num in min_heap]

# Example usage:

# Input list of numbers and the value of k (top k frequent elements)
nums = [1,1,1,2,2,3]
k = 2

# Initialize the Solution class and call the topKFrequent method
sol = Solution()
result = sol.topKFrequent(nums, k)

# Print the result, which will be the top 2 most frequent elements
print(result)  # Output: [1, 2]


"""
Using a priority queue is an efficient way to implement Dijkstra's algorithm. The priority queue helps keep track of the next 
node to process (the one with the smallest distance) in 
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

