"""
1. Implement a Stack with Push, Pop, and Peek Operations
Problem Statement:
Implement a stack with push, pop, and peek operations. Implement these operations for a basic stack data structure.

Example:

Input:
push(1) → push(2) → peek() → pop() → pop()
Output:
peek() = 2, pop() = 2, pop() = 1

"""
class Stack:
    def __init__(self):
        # Initialize an empty list to represent the stack
        self.stack = []

    def push(self, val):
        # Add an element to the top of the stack
        self.stack.append(val)

    def pop(self):
        # Remove and return the top element of the stack
        # Check if the stack is not empty before attempting to pop
        if not self.is_empty():
            return self.stack.pop()
        # Return None if the stack is empty
        return None

    def peek(self):
        # Return the top element of the stack without removing it
        # Check if the stack is not empty before accessing the top element
        if not self.is_empty():
            return self.stack[-1]
        # Return None if the stack is empty
        return None

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

# Example usage:
stack = Stack()          # Create an instance of the Stack class
stack.push(1)            # Push the value 1 onto the stack
stack.push(2)            # Push the value 2 onto the stack
print(stack.peek())      # Output: 2 (the top element of the stack)
print(stack.pop())       # Output: 2 (removes and returns the top element)
print(stack.pop())       # Output: 1 (removes and returns the next top element)

# """
# Time Complexity:
# push: O(1)
# pop: O(1)
# peek: O(1)
# Space Complexity: O(n), where n is the number of elements in the stack.
# """

"""
2. Implement a Queue with Enqueue and Dequeue Operations
Problem Statement:
Implement a queue with enqueue and dequeue operations. Implement the queue data structure and make use of FIFO (First In First Out) principle.

Example:

Input:
enqueue(1) → enqueue(2) → dequeue() → dequeue()
Output:
dequeue() = 1, dequeue() = 2
"""
class Queue:
    def __init__(self):
        # Initialize an empty list to represent the queue
        self.queue = []

    def enqueue(self, val):
        # Add an element to the end of the queue
        self.queue.append(val)

    def dequeue(self):
        # Remove and return the element at the front of the queue
        # Check if the queue is not empty before attempting to dequeue
        if not self.is_empty():
            return self.queue.pop(0)
        # Return None if the queue is empty
        return None

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

# Example usage:
queue = Queue()          # Create an instance of the Queue class
queue.enqueue(1)         # Enqueue the value 1 into the queue
queue.enqueue(2)         # Enqueue the value 2 into the queue
print(queue.dequeue())   # Output: 1 (removes and returns the front element)
print(queue.dequeue())   # Output: 2 (removes and returns the next front element)

# """
# Time Complexity:
# enqueue: O(1)
# dequeue: O(n) (since we shift all elements in the list)

# Space Complexity:O(n), where n is the number of elements in the queue.
# """

"""
3. Implement a Stack Using Two Queues
Problem Statement:
Implement a stack using two queues. Your solution should be efficient for both push and pop operations.

Example:

Input:
push(1) → push(2) → pop() → push(3) → pop()
Output:
pop() = 2, pop() = 3
"""
class StackUsingQueues:
    def __init__(self):
        # Initialize two empty queues
        # queue1 will be the primary queue where elements are pushed
        # queue2 will be used as a temporary queue during the pop operation
        self.queue1 = []
        self.queue2 = []
    
    def push(self, val):
        # Add an element to the end of queue1
        self.queue1.append(val)
    
    def pop(self):
        # If queue1 is empty, there are no elements to pop, so return None
        if len(self.queue1) == 0:
            return None
        
        # Transfer all elements except the last one from queue1 to queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        
        # The last element remaining in queue1 is the one to be popped
        popped_val = self.queue1.pop()
        
        # Swap the roles of queue1 and queue2
        # queue2 now becomes the main queue (queue1), and queue1 becomes empty
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        # Return the popped value
        return popped_val

# Example usage:
stack = StackUsingQueues()  # Create an instance of the StackUsingQueues class
stack.push(1)               # Push the value 1 onto the stack
stack.push(2)               # Push the value 2 onto the stack
print(stack.pop())          # Output: 2 (removes and returns the last pushed element)
stack.push(3)               # Push the value 3 onto the stack
print(stack.pop())          # Output: 3 (removes and returns the last pushed element)


# Time Complexity:
# push: O(1)
# pop: O(n)
# Space Complexity: O(n), where n is the number of elements in the stack.


"""
4. Check Balanced Parentheses Using Stack
Problem Statement:
Given a string containing just the characters '(', ')', {, }, [, and ], determine if the input string is valid.
An input string is valid if the brackets are closed in the correct order.

Example:

Input:
"{[()]}"

Output:
True

Input:
"{[(])}"

Output:
False
"""

class Solution:
    def is_valid(self, expression):
        """Checks if an expression has balanced parentheses."""
        
        # Stack to keep track of opening parentheses
        stack = []
        
        # Dictionary to match closing parentheses with corresponding opening parentheses
        pairs = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the expression
        for char in expression:
            # If the character is an opening parenthesis, push it onto the stack
            if char in pairs.values():
                stack.append(char)
            
            # If the character is a closing parenthesis
            elif char in pairs:
                # If the stack is empty or the top of the stack doesn't match the expected opening parenthesis, return False
                if not stack or stack.pop() != pairs[char]:
                    return False
        
        # Return True if the stack is empty (all opening parentheses had a matching closing parenthesis)
        return not stack

# Create an instance of Solution
sol = Solution()  
print(sol.is_valid("{[()]}"))  # Output: True (all brackets are matched correctly)
print(sol.is_valid("{[(])}"))  # Output: False (mismatched brackets)


# Time Complexity:O(n), where n is the length of the string.
# Space Complexity:O(n), due to the stack storage.


"""
5. Reverse a Stack
Problem Statement:
Write a function that reverses a stack using recursion.

Example:

Input:
Stack: 1 -> 2 -> 3 -> 4
Output:
Reversed Stack: 4 -> 3 -> 2 -> 1
"""
class Stack:
    def __init__(self):
        # Initialize an empty list to represent the stack
        self.stack = []
    
    def push(self, val):
        # Push an element onto the stack (add it to the end of the list)
        self.stack.append(val)
    
    def pop(self):
        # Pop an element from the stack (remove the last element of the list)
        # If the stack is empty, return None
        return self.stack.pop() if self.stack else None
    
    def peek(self):
        # Peek at the top element of the stack (view the last element without removing it)
        # If the stack is empty, return None
        return self.stack[-1] if self.stack else None
    
    def is_empty(self):
        # Check if the stack is empty by checking if the length is 0
        return len(self.stack) == 0

def reverse_stack(stack):
    # Recursively reverse the stack by popping elements and re-inserting them at the bottom
    if not stack.is_empty():
        # Pop the top element
        temp = stack.pop()
        # Recursively reverse the rest of the stack
        reverse_stack(stack)
        # Insert the popped element at the bottom of the stack
        insert_at_bottom(stack, temp)

def insert_at_bottom(stack, item):
    # Recursively insert the given item at the bottom of the stack
    if stack.is_empty():
        # If the stack is empty, push the item
        stack.push(item)
    else:
        # Otherwise, pop the top element, recursively insert the item at the bottom,
        # and then push the popped element back onto the stack
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.push(temp)

# Example usage:
stack = Stack()  # Create a new stack instance
stack.push(1)    # Push 1 onto the stack
stack.push(2)    # Push 2 onto the stack
stack.push(3)    # Push 3 onto the stack
stack.push(4)    # Push 4 onto the stack

reverse_stack(stack)  # Reverse the stack using recursion

# Output the reversed stack by popping elements
while not stack.is_empty():
    print(stack.pop(), end=" -> ")  # Print each element followed by "->"

# Output: 4 -> 3 -> 2 -> 1

# Time Complexity: O(n), where n is the number of elements in the stack.

# Space Complexity: O(n), due to recursion stack.


"""
6. Implement Min Stack
Problem Statement:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Example:

Input:
push(1) → push(2) → getMin() → pop() → getMin()
Output:
getMin() = 1, pop() = 2, getMin() = 1
"""
class MinStack:
    def __init__(self):
        # Initialize two stacks:
        # 1. 'stack' holds the main stack elements.
        # 2. 'min_stack' holds the minimum elements at each level of the stack.
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        # Push the value onto the main stack
        self.stack.append(val)
        
        # If 'min_stack' is empty or the current value is smaller than or equal to the top of the 'min_stack',
        # push the current value onto 'min_stack' as well.
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        # If the main stack is not empty, pop the top element from it
        if self.stack:
            val = self.stack.pop()
            
            # If the popped value is equal to the top value in the 'min_stack',
            # pop it from the 'min_stack' as well (it was the minimum value at that level).
            if val == self.min_stack[-1]:
                self.min_stack.pop()
                
            return val
        return None
    
    def top(self):
        # Return the top element of the main stack without removing it.
        # If the stack is empty, return None.
        return self.stack[-1] if self.stack else None
    
    def getMin(self):
        # Return the minimum element from the 'min_stack', which is always the top element.
        # If 'min_stack' is empty, return None.
        return self.min_stack[-1] if self.min_stack else None

# Example usage:
min_stack = MinStack()   # Create a new instance of MinStack
min_stack.push(1)        # Push 1 onto the stack
min_stack.push(2)        # Push 2 onto the stack
print(min_stack.getMin())  # Output: 1, as 1 is the minimum value
min_stack.pop()          # Pop the top element (2)
print(min_stack.getMin())  # Output: 1, as 1 is still the minimum value


# Time Complexity: O(1) for push, pop, top, and getMin.

# Space Complexity: O(n), where n is the number of elements in the stack.


"""
7. Sliding Window Maximum (Deque/Queue)
Problem Statement:
Given an array of integers, find the maximum value in each sliding window of size k.

Example:

Input:
Array: [1,3,-1,-3,5,3,6,7], k = 3
Output:
[3,3,5,5,6,7]
"""

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        # If the input list is empty, return an empty list
        if not nums:
            return []
        
        # Deque to store the indices of elements in the current sliding window
        deque_index = deque()
        # List to store the result (maximum values in each sliding window)
        result = []
        
        # Iterate through each element in the input list
        for i in range(len(nums)):
            # Remove elements outside the window
            # The condition checks if the index at the front of deque is out of the current window
            if deque_index and deque_index[0] < i - k + 1:
                deque_index.popleft()  # Remove the index from deque (out of the window)
            
            # Remove smaller elements in the window
            # Keep the largest elements in the deque for maximum sliding window
            while deque_index and nums[deque_index[-1]] < nums[i]:
                deque_index.pop()  # Remove smaller elements from the back of the deque
            
            # Add the current element's index to the deque
            deque_index.append(i)
            
            # Once the window is fully formed, i.e., i >= k - 1, add the maximum element to the result
            if i >= k - 1:
                # The front of the deque holds the index of the maximum element in the window
                result.append(nums[deque_index[0]])
        
        return result  # Return the list of maximum values for each sliding window

# Example usage:
sol = Solution()
# Test case: Sliding window of size 3
print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Output: [3, 3, 5, 5, 6, 7]

"""
Time Complexity:

O(n), where n is the number of elements in the array.
Space Complexity:

O(k), where k is the size of the sliding window.
"""


"""
8. Implement Queue Using Stacks
Problem Statement:
Implement a queue using two stacks. Your solution should support enqueue and dequeue operations efficiently.

Example:

Input:
enqueue(1) → enqueue(2) → dequeue() → enqueue(3) → dequeue()
Output:
dequeue() = 1, dequeue() = 2
"""
class QueueUsingStacks:
    def __init__(self):
        # Initialize two stacks: stack1 for enqueue operations and stack2 for dequeue operations
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, val):
        # Add the value to stack1 (enqueue operation)
        self.stack1.append(val)
    
    def dequeue(self):
        # If stack2 is empty, transfer elements from stack1 to stack2
        # This ensures the first element in stack1 is on top of stack2 for the dequeue operation
        if not self.stack2:
            while self.stack1:
                # Pop all elements from stack1 and push them onto stack2
                self.stack2.append(self.stack1.pop())
        
        # If stack2 is not empty, pop the top element from stack2 and return it
        if self.stack2:
            return self.stack2.pop()
        
        # If both stacks are empty, return None (queue is empty)
        return None

# Example usage:
queue = QueueUsingStacks()
queue.enqueue(1)  # Add 1 to the queue
queue.enqueue(2)  # Add 2 to the queue
print(queue.dequeue())  # Output: 1 (first element in the queue is dequeued)
queue.enqueue(3)  # Add 3 to the queue
print(queue.dequeue())  # Output: 2 (second element in the queue is dequeued)

# Time Complexity:
# enqueue: O(1)
# dequeue: O(n), in the worst case.

# Space Complexity: O(n), where n is the number of elements in the queue.


"""
9. Monotonic Stack for Next Greater Element
Problem Statement:
Given an array, find the next greater element for each element in the array. For the element, output the next greater
element in the array (if no greater element exists, output -1).

Example:

Input:
[4, 5, 2, 10]
Output:
[5, 10, 10, -1]
"""

class Solution:
    def nextGreaterElements(self, nums):
        # Initialize an empty stack to store indices of the nums array
        stack = []
        
        # Initialize result array with -1, assuming no next greater element by default
        result = [-1] * len(nums)
        
        # Iterate twice through the nums array to simulate the circular nature
        # We need to go through the array once for each element and check if a greater element exists
        for i in range(2 * len(nums)):  # Iterate twice for circular array
            # While stack is not empty and the current element is greater than the element at the index
            # stored at the top of the stack, update the result for that index
            while stack and nums[stack[-1]] < nums[i % len(nums)]:
                result[stack.pop()] = nums[i % len(nums)]
            
            # Append the current index (modulo the length of nums to ensure circular behavior)
            stack.append(i % len(nums))
        
        return result

# Example usage:
sol = Solution()
print(sol.nextGreaterElements([4, 5, 2, 10]))  # Output: [5, 10, 10, -1]

# Time Complexity: O(n), where n is the number of elements in the array.

# Space Complexity: O(n), where n is the number of elements in the array.


"""
10. Sliding Window Minimum (Deque/Queue)
Problem Statement:
Given an array of integers, find the minimum value in each sliding window of size k.

Example:

Input:
Array: [1,3,-1,-3,5,3,6,7], k = 3
Output:
[-1,-3,-3,-3,3,3]
"""
from collections import deque

class Solution:
    def minSlidingWindow(self, nums, k):
        # If the input array is empty, return an empty list
        if not nums:
            return []
        
        # Initialize a deque to store the indices of the elements in the sliding window
        deque_index = deque()
        
        # Initialize an empty list to store the result
        result = []
        
        # Loop through the elements in the array
        for i in range(len(nums)):
            # Remove elements that are outside the current window (i.e., i - k + 1)
            # These are no longer part of the window, so we remove them from the deque
            if deque_index and deque_index[0] < i - k + 1:
                deque_index.popleft()
            
            # Remove elements from the deque that are larger than the current element
            # because they are not needed to compute the minimum for the current window
            while deque_index and nums[deque_index[-1]] > nums[i]:
                deque_index.pop()
            
            # Add the current element index to the deque
            deque_index.append(i)
            
            # Once we have processed at least k elements (i >= k - 1),
            # add the minimum element of the current window to the result
            if i >= k - 1:
                result.append(nums[deque_index[0]])  # The front of the deque holds the index of the minimum element
        
        # Return the list of minimum values for each window
        return result

# Example usage:
sol = Solution()
print(sol.minSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # Output: [-1, -3, -3, -3, 3, 3]


# Time Complexity: O(n), where n is the number of elements in the array.

# Space Complexity: O(k), where k is the size of the sliding window.

"""
11. LRU Cache Implementation
Problem Statement:
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations:

get(key) - Retrieve the value of the key if the key exists, otherwise return -1.
put(key, value) - Insert the value if the key is not already present. When the cache reaches its capacity, the least recently
used item is evicted.
Example:

Input:
put(1, 1) → put(2, 2) → get(1) → put(3, 3) → get(2) → put(4, 4) → get(1) → get(3) → get(4)
Output:
1, -1, 3, 4
"""
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        # Initialize the cache as an ordered dictionary to maintain the access order
        self.cache = OrderedDict()
        # Set the maximum capacity of the cache
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        # If the key is present in the cache
        if key in self.cache:
            # Move the accessed item to the end of the OrderedDict (most recently used)
            self.cache.move_to_end(key)
            # Return the value associated with the key
            return self.cache[key]
        # If the key is not present, return -1
        return -1
    
    def put(self, key: int, value: int):
        # If the key is already in the cache, move it to the end (update usage)
        if key in self.cache:
            self.cache.move_to_end(key)
        # Add or update the key with its associated value
        self.cache[key] = value
        # If the cache exceeds its capacity, remove the oldest (least recently used) item
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Removes the first (least recently used) item

# Example usage:
cache = LRUCache(2)
cache.put(1, 1)   # Cache: {1=1}
cache.put(2, 2)   # Cache: {1=1, 2=2}
print(cache.get(1))  # Output: 1  (Access key 1, move it to end)
cache.put(3, 3)      # Cache: {2=2, 3=3} (Evicts key 2)
print(cache.get(2))  # Output: -1  (Key 2 evicted)
cache.put(4, 4)      # Cache: {3=3, 4=4} (Evicts key 1)
print(cache.get(1))  # Output: -1  (Key 1 evicted)
print(cache.get(3))  # Output: 3  (Access key 3)
print(cache.get(4))  # Output: 4  (Access key 4)


# Time Complexity:
# get: O(1)
# put: O(1)

# Space Complexity:O(capacity), where capacity is the maximum size of the cache.

"""
12. Kth Smallest Element in a BST
Problem Statement:
Given the root of a binary search tree (BST) and an integer k, return the kth smallest value (1-indexed) of all the values of the
nodes in the tree.

Example:

Input:
root = [3,1,4,null,2], k = 1
Output:
1
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Initialize a tree node with a value, left child, and right child
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Helper function to perform an inorder traversal of the tree
        def inorder(node):
            if not node:  # Base case: if the node is None, return an empty list
                return []
            # Recursively get the values of the left subtree, the current node, and the right subtree
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        # Perform an inorder traversal of the tree and return the k-th smallest element
        # Inorder traversal of a binary search tree returns the elements in ascending order
        return inorder(root)[k-1]

# Example usage:
root = TreeNode(3)                # Create the root node with value 3
root.left = TreeNode(1)            # Create the left child with value 1
root.right = TreeNode(4)           # Create the right child with value 4
root.left.right = TreeNode(2)      # Create the right child of the left node with value 2
sol = Solution()                   # Create an instance of the Solution class
print(sol.kthSmallest(root, 1))    # Output: 1, as 1 is the 1st smallest element in the BST


# Time Complexity:

# O(n), where n is the number of nodes in the tree.
# Space Complexity:

# O(n), due to the space needed for the inorder traversal.


"""
13. Merge Intervals
Problem Statement:
Given a collection of intervals, merge all overlapping intervals.

Example:

Input:
[[1,3], [2,6], [8,10], [15,18]]
Output:
[[1, 6], [8, 10], [15, 18]]
"""
class Solution:
    def merge(self, intervals):
        # Sort the intervals by the starting point of each interval
        intervals.sort(key=lambda x: x[0])
        
        merged = []  # This will hold the merged intervals
        
        # Iterate over each interval in the sorted list
        for interval in intervals:
            # If merged is empty or there is no overlap with the last merged interval
            if not merged or merged[-1][1] < interval[0]:
                # Add the current interval to merged as there is no overlap
                merged.append(interval)
            else:
                # There is overlap, so we merge the intervals by updating the end of the last merged interval
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        # Return the list of merged intervals
        return merged

# Example usage:
sol = Solution()
# Merging the intervals [[1,3], [2,6], [8,10], [15,18]]
# After sorting: [[1,3], [2,6], [8,10], [15,18]]
# The merged result is [[1, 6], [8, 10], [15, 18]]
print(sol.merge([[1,3], [2,6], [8,10], [15,18]]))  # Output: [[1, 6], [8, 10], [15, 18]]


# Time Complexity: O(n log n), where n is the number of intervals (due to sorting).

# Space Complexity: O(n), where n is the number of intervals.


"""
14. Spiral Matrix
Problem Statement:
Given an m x n matrix, return all elements of the matrix in spiral order.

Example:

Input:
matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output:
[1, 2, 3, 6, 9, 8, 7, 4, 5]
"""
class Solution:
    def spiralOrder(self, matrix):
        # Initialize an empty list to store the result
        res = []
        
        # Continue looping as long as there are rows in the matrix
        while matrix:
            # Add the first row to the result (moving from left to right)
            res += matrix.pop(0)
            
            # If the matrix still has rows and the first column is non-empty
            if matrix and matrix[0]:
                # Add the last element of each row (moving from top to bottom)
                for row in matrix:
                    res.append(row.pop())
            
            # If the matrix is not empty, add the last row (moving from right to left)
            if matrix:
                res += matrix.pop()[::-1]
            
            # If the matrix still has rows and the first column is non-empty
            if matrix and matrix[0]:
                # Add the first element of each row (moving from bottom to top)
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        
        # Return the result after completing the spiral traversal
        return res

# Example usage:
sol = Solution()
# For the matrix [[1,2,3], [4,5,6], [7,8,9]], the output is [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the matrix.

# Space Complexity: O(m * n), to store the result.


"""
15. Find Peak Element
Problem Statement:
A peak element is an element that is strictly greater than its neighbors. Given an array, find a peak element and return its index.
If the array contains multiple peaks, return any of them.

Example:

Input:
[1,2,3,1]
Output:
2 (because 3 is a peak)
"""

class Solution:
    def findPeakElement(self, nums):
        # Initialize two pointers: left and right, representing the range of indices
        left, right = 0, len(nums) - 1
        
        # Perform binary search
        while left < right:
            # Find the middle index
            mid = left + (right - left) // 2
            
            # If the middle element is greater than the next element, then the peak must be on the left side
            if nums[mid] > nums[mid + 1]:
                right = mid  # Move the right pointer to mid
            else:
                left = mid + 1  # Move the left pointer to mid + 1
        
        # When left equals right, we've found the peak element, return the index
        return left

# Example usage:
sol = Solution()
# For the array [1, 2, 3, 1], the peak element is 3 (at index 2)
print(sol.findPeakElement([1, 2, 3, 1]))  # Output: 2


# Time Complexity: O(log n), where n is the length of the array.
# Space Complexity: O(1)

"""
16. Word Ladder II
Problem Statement:
Given two words (start and end) and a dictionary of words, return all shortest transformation sequences from start to end, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the dictionary.
Example:

Input:
beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output:
[ ["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"] ]
"""
from collections import defaultdict, deque
[]
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        # Convert wordList to a set for faster lookup
        wordList = set(wordList)
        
        # If the endWord is not in the wordList, return an empty list as it's impossible to reach the endWord
        if endWord not in wordList:
            return []
        
        # Initialize a dictionary to hold the current level of words
        # Each key will be a word, and the value will be a list of paths leading to that word
        level = {beginWord: [[beginWord]]}
        
        # Start a BFS-like process to explore all word transformations
        while level:
            # Create a new level to store transformations for the next step
            new_level = defaultdict(list)
            
            # Iterate through each word in the current level
            for word in level:
                # If we found the endWord, return all the paths leading to it
                if word == endWord:
                    return level[word]
                
                # For each word, try transforming it to another word by changing one letter at a time
                for i in range(len(word)):
                    # Try replacing each letter with all possible letters from 'a' to 'z'
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        # Generate a new word by replacing the current letter with the new one
                        new_word = word[:i] + char + word[i+1:]
                        
                        # If the new word is in the wordList, it's a valid transformation
                        if new_word in wordList:
                            # Add the new word to the new level, and add all sequences leading to the current word
                            new_level[new_word] += [seq + [new_word] for seq in level[word]]
            
            # Remove the new words from wordList to prevent revisiting them in the next level
            wordList -= set(new_level.keys())
            
            # Move to the next level
            level = new_level
        
        # If no path is found, return an empty list
        return []

# Example usage:
sol = Solution()
# Example input: start from "hit", end at "cog", and the wordList includes ["hot", "dot", "dog", "lot", "log", "cog"]
print(sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))

# Time Complexity: O(n * L * 26), where n is the number of words in the word list and L is the length of each word.

# Space Complexity: O(n * L), where n is the number of words and L is the length of each word.


"""
17. Maximal Rectangle
Problem Statement:
Given a 2D binary matrix filled with 0's and 1's, find the maximal rectangle containing only 1's and return its area.

Example:

Input:
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output:
6
"""
class Solution:
    def maximalRectangle(self, matrix):
        # If the matrix is empty, return 0 as there's no rectangle to find
        if not matrix:
            return 0
        
        # Get the number of columns in the matrix
        n = len(matrix[0])
        
        # Initialize an array to store the heights of the histogram
        # heights[i] represents the number of consecutive '1's in the matrix at column i
        heights = [0] * n
        
        # Variable to keep track of the maximum area found
        max_area = 0
        
        # Iterate through each row in the matrix
        for row in matrix:
            # Update the heights array for the current row
            for i in range(n):
                # If the cell is '1', increment the corresponding height
                # If the cell is '0', reset the corresponding height to 0
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            # Calculate the largest rectangle area for the current heights
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        # Return the maximum area found
        return max_area
    
    def largestRectangleArea(self, heights):
        # Stack to hold the indices of the heights array
        # We initialize the stack with -1 to handle edge cases where the stack might be empty
        stack = [-1]
        
        # Variable to keep track of the maximum rectangle area
        max_area = 0
        
        # Iterate through the heights array, including an extra 0 at the end
        # The extra 0 helps to empty the stack at the end of the loop
        for i, h in enumerate(heights + [0]):
            # While the current height is less than the height at the top of the stack
            # Pop from the stack and calculate the area of the rectangle formed
            # by the popped height as the shortest height in that rectangle
            while heights[stack[-1]] > h:
                h = heights[stack.pop()]
                # Calculate the area for the rectangle using the popped height
                max_area = max(max_area, h * (i - stack[-1] - 1))
            
            # Push the current index to the stack
            stack.append(i)
        
        # Return the maximum area found
        return max_area

# Example usage:
sol = Solution()
# Example input matrix where '1' represents filled cells and '0' represents empty cells
# Expected output: 6
print(sol.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))

# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the matrix.

# Space Complexity: O(n), where n is the number of columns in the matrix.

"""
18. Coin Change Problem
Problem Statement:
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
You need to return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by 
any combination of the coins, return -1.

Example:

Input:
coins = [1, 2, 5], amount = 11
Output:
3 (because 11 = 5 + 5 + 1)
"""

class Solution:
    def coinChange(self, coins, amount):
        # Initialize the dp array with a large number (infinity).
        # dp[i] will represent the minimum number of coins needed to make amount i.
        dp = [float('inf')] * (amount + 1)
        
        # Base case: it takes 0 coins to make amount 0.
        dp[0] = 0
        
        # Iterate through each coin denomination
        for coin in coins:
            # For each coin, try to update the dp array for all amounts from 'coin' to 'amount'
            for i in range(coin, amount + 1):
                # Update dp[i] to the minimum number of coins needed by considering using this coin.
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If dp[amount] is still infinity, it means it's not possible to make the amount with the given coins.
        # Otherwise, return the minimum number of coins needed.
        return dp[amount] if dp[amount] != float('inf') else -1

# Example usage:
sol = Solution()
# Example input: coins = [1, 2, 5], amount = 11
# Expected output: 3 (since 11 can be made using 5 + 5 + 1)
print(sol.coinChange([1, 2, 5], 11))  # Output: 3


# Time Complexity: O(amount * n), where n is the number of coins.

# Space Complexity: O(amount), where amount is the target amount.
