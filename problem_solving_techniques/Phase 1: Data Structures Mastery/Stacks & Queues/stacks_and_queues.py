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
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def is_empty(self):
        return len(self.stack) == 0

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())  # Output: 2
print(stack.pop())   # Output: 2
print(stack.pop())   # Output: 1
"""
Time Complexity:

push: O(1)
pop: O(1)
peek: O(1)
Space Complexity:

O(n), where n is the number of elements in the stack.
"""
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
        self.queue = []
    
    def enqueue(self, val):
        self.queue.append(val)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None
    
    def is_empty(self):
        return len(self.queue) == 0

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
"""
Time Complexity:

enqueue: O(1)
dequeue: O(n) (since we shift all elements in the list)
Space Complexity:

O(n), where n is the number of elements in the queue.
"""

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
        self.queue1 = []
        self.queue2 = []
    
    def push(self, val):
        self.queue1.append(val)
    
    def pop(self):
        if len(self.queue1) == 0:
            return None
        
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        
        popped_val = self.queue1.pop()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return popped_val

# Example usage:
stack = StackUsingQueues()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
stack.push(3)
print(stack.pop())  # Output: 3
"""
Time Complexity:

push: O(1)
pop: O(n)
Space Complexity:

O(n), where n is the number of elements in the stack.
"""

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
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack

# Example usage:
sol = Solution()
print(sol.isValid("{[()]}"))  # Output: True
print(sol.isValid("{[(])}"))  # Output: False
"""
Time Complexity:

O(n), where n is the length of the string.
Space Complexity:

O(n), due to the stack storage.
"""

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
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        return self.stack.pop() if self.stack else None
    
    def peek(self):
        return self.stack[-1] if self.stack else None
    
    def is_empty(self):
        return len(self.stack) == 0

def reverse_stack(stack):
    if not stack.is_empty():
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)

def insert_at_bottom(stack, item):
    if stack.is_empty():
        stack.push(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.push(temp)

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
reverse_stack(stack)

# Output reversed stack
while not stack.is_empty():
    print(stack.pop(), end=" -> ")
# Output: 4 -> 3 -> 2 -> 1
"""
Time Complexity:

O(n), where n is the number of elements in the stack.
Space Complexity:

O(n), due to recursion stack.
"""

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
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
            return val
        return None
    
    def top(self):
        return self.stack[-1] if self.stack else None
    
    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None

# Example usage:
min_stack = MinStack()
min_stack.push(1)
min_stack.push(2)
print(min_stack.getMin())  # Output: 1
min_stack.pop()
print(min_stack.getMin())  # Output: 1
"""
Time Complexity:

O(1) for push, pop, top, and getMin.
Space Complexity:

O(n), where n is the number of elements in the stack.
"""

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
        if not nums:
            return []
        
        deque_index = deque()
        result = []
        
        for i in range(len(nums)):
            # Remove elements outside the window
            if deque_index and deque_index[0] < i - k + 1:
                deque_index.popleft()
            
            # Remove smaller elements in the window
            while deque_index and nums[deque_index[-1]] < nums[i]:
                deque_index.pop()
            
            deque_index.append(i)
            
            if i >= k - 1:
                result.append(nums[deque_index[0]])
        
        return result

# Example usage:
sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # Output: [3, 3, 5, 5, 6, 7]
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
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, val):
        self.stack1.append(val)
    
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        return None

# Example usage:
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Output: 1
queue.enqueue(3)
print(queue.dequeue())  # Output: 2

"""
Time Complexity:

enqueue: O(1)
dequeue: O(n), in the worst case.
Space Complexity:

O(n), where n is the number of elements in the queue.
"""

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
        stack = []
        result = [-1] * len(nums)
        
        for i in range(2 * len(nums)):  # Iterate twice for circular array
            while stack and nums[stack[-1]] < nums[i % len(nums)]:
                result[stack.pop()] = nums[i % len(nums)]
            stack.append(i % len(nums))
        
        return result

# Example usage:
sol = Solution()
print(sol.nextGreaterElements([4, 5, 2, 10]))  # Output: [5, 10, 10, -1]
"""
Time Complexity:

O(n), where n is the number of elements in the array.
Space Complexity:

O(n), where n is the number of elements in the array.
"""


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
        if not nums:
            return []
        
        deque_index = deque()
        result = []
        
        for i in range(len(nums)):
            # Remove elements outside the window
            if deque_index and deque_index[0] < i - k + 1:
                deque_index.popleft()
            
            # Remove larger elements in the window
            while deque_index and nums[deque_index[-1]] > nums[i]:
                deque_index.pop()
            
            deque_index.append(i)
            
            if i >= k - 1:
                result.append(nums[deque_index[0]])
        
        return result

# Example usage:
sol = Solution()
print(sol.minSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # Output: [-1, -3, -3, -3, 3, 3]
"""
Time Complexity:

O(n), where n is the number of elements in the array.
Space Complexity:

O(k), where k is the size of the sliding window.
Let me know if you need more questions or further explanations on any of the problems.
"""


"""
11. LRU Cache Implementation
Problem Statement:
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations:

get(key) - Retrieve the value of the key if the key exists, otherwise return -1.
put(key, value) - Insert the value if the key is not already present. When the cache reaches its capacity, the least recently used item is evicted.
Example:

Input:
put(1, 1) → put(2, 2) → get(1) → put(3, 3) → get(2) → put(4, 4) → get(1) → get(3) → get(4)
Output:
1, -1, 3, 4
"""

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)  # Move the accessed item to the end
            return self.cache[key]
        return -1
    
    def put(self, key: int, value: int):
        if key in self.cache:
            self.cache.move_to_end(key)  # Move the updated item to the end
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove the first (least recently used) item

# Example usage:
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Output: 1
cache.put(3, 3)  # Evicts key 2
print(cache.get(2))  # Output: -1
cache.put(4, 4)  # Evicts key 1
print(cache.get(1))  # Output: -1
print(cache.get(3))  # Output: 3
print(cache.get(4))  # Output: 4
"""
Time Complexity:

get: O(1)
put: O(1)
Space Complexity:

O(capacity), where capacity is the maximum size of the cache.
"""
"""
12. Kth Smallest Element in a BST
Problem Statement:
Given the root of a binary search tree (BST) and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example:

Input:
root = [3,1,4,null,2], k = 1
Output:
1
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        return inorder(root)[k-1]

# Example usage:
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
sol = Solution()
print(sol.kthSmallest(root, 1))  # Output: 1
"""
Time Complexity:

O(n), where n is the number of nodes in the tree.
Space Complexity:

O(n), due to the space needed for the inorder traversal.
"""

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
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

# Example usage:
sol = Solution()
print(sol.merge([[1,3], [2,6], [8,10], [15,18]]))  # Output: [[1, 6], [8, 10], [15, 18]]
"""
Time Complexity:

O(n log n), where n is the number of intervals (due to sorting).
Space Complexity:

O(n), where n is the number of intervals.
"""

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
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res

# Example usage:
sol = Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
"""
Time Complexity:

O(m * n), where m is the number of rows and n is the number of columns in the matrix.
Space Complexity:

O(m * n), to store the result.
"""

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
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left

# Example usage:
sol = Solution()
print(sol.findPeakElement([1,2,3,1]))  # Output: 2
"""
Time Complexity:

O(log n), where n is the length of the array.
Space Complexity:

O(1)
"""

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

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        
        level = {beginWord: [[beginWord]]}
        while level:
            new_level = defaultdict(list)
            for word in level:
                if word == endWord:
                    return level[word]
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + char + word[i+1:]
                        if new_word in wordList:
                            new_level[new_word] += [seq + [new_word] for seq in level[word]]
            wordList -= set(new_level.keys())
            level = new_level
        return []

# Example usage:
sol = Solution()
print(sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
"""
Time Complexity:

O(n * L * 26), where n is the number of words in the word list and L is the length of each word.
Space Complexity:

O(n * L), where n is the number of words and L is the length of each word.
"""

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
        if not matrix:
            return 0
        n = len(matrix[0])
        heights = [0] * n
        max_area = 0
        
        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area
    
    def largestRectangleArea(self, heights):
        stack = [-1]
        max_area = 0
        for i, h in enumerate(heights + [0]):
            while heights[stack[-1]] > h:
                h = heights[stack.pop()]
                max_area = max(max_area, h * (i - stack[-1] - 1))
            stack.append(i)
        return max_area

# Example usage:
sol = Solution()
print(sol.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))  # Output: 6
"""
Time Complexity:

O(m * n), where m is the number of rows and n is the number of columns in the matrix.
Space Complexity:

O(n), where n is the number of columns in the matrix.
"""

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
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

# Example usage:
sol = Solution()
print(sol.coinChange([1, 2, 5], 11))  # Output: 3
"""
Time Complexity:

O(amount * n), where n is the number of coins.
Space Complexity:

O(amount), where amount is the target amount.
"""