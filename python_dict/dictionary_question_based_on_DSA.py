"""
Question: Write a Python program to find the "Longest Subarray with Sum Zero" using a hashmap.

Comment: The algorithm uses a hashmap to store the prefix sum and checks if the sum has occurred before to find the longest
subarray with a sum of zero.
"""
def longest_subarray_with_sum_zero(arr):
    # Initialize an empty dictionary to store the prefix sum
    prefix_sum = {}
    # Initialize variables to track the maximum length and the current sum
    max_len = 0
    curr_sum = 0

    # Traverse through the array
    for i, num in enumerate(arr):
        # Add the current number to the current sum
        curr_sum += num

        # If the current sum is zero, the subarray from the beginning to the current index
        # has a sum of zero, so we update the maximum length
        if curr_sum == 0:
            max_len = i + 1

        # If the current sum has already been seen before in the prefix_sum dictionary,
        # it means the subarray between the previous occurrence and the current index has a sum of zero
        if curr_sum in prefix_sum:
            max_len = max(max_len, i - prefix_sum[curr_sum])
        else:
            # If this is the first time the current sum has been seen, store its index
            prefix_sum[curr_sum] = i

    # Return the maximum length of the subarray with a sum of zero
    return max_len

# Example usage
arr = [1, -1, 3, 2, -2, 1]
print(longest_subarray_with_sum_zero(arr))  # Output: 4

# Time Complexity: O(n) (where n is the size of the array)

# Space Complexity: O(n)
"""
2. Longest Substring Without Repeating Characters

Question: Write a Python program to find the "Longest Substring without Repeating Characters" using a sliding window technique with a hashmap.

Comment: We use a hashmap to store the index of characters and a sliding window to find the longest substring without repeating characters.


"""
def longest_substring_without_repeating(s):
    # Initialize a dictionary to store the last index of each character
    char_map = {}
    # Initialize variables to represent the start of the window and the maximum length
    start = 0
    max_len = 0

    # Traverse through the string with the 'end' pointer
    for end in range(len(s)):
        # If the character at the 'end' pointer is already in the window,
        # update the start pointer to the right of its last occurrence
        if s[end] in char_map:
            start = max(start, char_map[s[end]] + 1)

        # Update the last occurrence of the character at the 'end' pointer
        char_map[s[end]] = end

        # Update the maximum length of the window
        max_len = max(max_len, end - start + 1)

    # Return the length of the longest substring without repeating characters
    return max_len

# Example usage
s = "abcabcbb"
print(longest_substring_without_repeating(s))  # Output: 3

# Time Complexity: O(n) (where n is the length of the string)

# Space Complexity: O(min(n, m)) (where n is the length of the string, and m is the number of unique characters)
"""
3. Subarray with Given Sum
Question: Write a Python program to find the "Subarray with Given Sum" using a hashmap.

Comment: This problem can be solved by checking the prefix sums stored in a hashmap.

"""

def subarray_with_sum(arr, target_sum):
    # Initialize a dictionary to store the prefix sum and its index
    prefix_sum = {0: -1}  # Starting with prefix sum 0 at index -1
    curr_sum = 0
    # Traverse through the array
    for i, num in enumerate(arr):
        # Update the current sum by adding the current element
        curr_sum += num
        
        # If the difference between the current sum and target sum exists in the dictionary,
        # that means there exists a subarray with the required sum
        if curr_sum - target_sum in prefix_sum:
            return (prefix_sum[curr_sum - target_sum] + 1, i)
        
        # Store the current sum and its index in the dictionary
        prefix_sum[curr_sum] = i
    
    # If no such subarray exists, return None
    return None

# Example usage
arr = [1, 4, 20, 3, 10, 5]
target_sum = 33
print(subarray_with_sum(arr, target_sum))  # Output: (2, 4)

# Time Complexity: O(n) (where n is the length of the array)

# Space Complexity: O(n)
"""
4. LRU Cache
Question: Write a Python program to implement the "LRU Cache" (Least Recently Used) using a dictionary and a doubly linked list.

Comment: The LRU Cache is implemented with a hashmap for fast lookup and a doubly linked list to maintain the order of access.

"""
class Node:
    def __init__(self, key, value):
        self.key = key  # The key for the node
        self.value = value  # The value associated with the key
        self.prev = None  # Pointer to the previous node in the doubly linked list
        self.next = None  # Pointer to the next node in the doubly linked list

class LRUCache:
    def __init__(self, capacity):
        self.cache = {}  # Dictionary to store the key-value pairs
        self.capacity = capacity  # Maximum capacity of the cache
        # Dummy head and tail nodes for the doubly linked list
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        # Link the head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # Helper function to remove a node from the doubly linked list
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # Helper function to insert a node at the front of the doubly linked list
    def _insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    # Function to get the value associated with a key from the cache
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Remove the node from the current position
            self._insert(node)  # Reinsert it at the front (most recently used)
            return node.value
        return -1  # If the key is not found

    # Function to put a key-value pair into the cache
    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])  # Remove the old node
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)  # Insert the new node at the front
        # If the cache exceeds the capacity, remove the least recently used node
        if len(self.cache) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.cache[node.key]

# Example usage
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # Output: 1
lru.put(3, 3)  # Removes key 2
print(lru.get(2))  # Output: -1

# Time Complexity: O(1) for both get and put operations.

# Space Complexity: O(capacity)
"""
5. Word Ladder using BFS
Question: Write a Python program to solve the "Word Ladder" problem using a dictionary and breadth-first search (BFS).

Comment: BFS is used to explore all possible transformations of the word, and a dictionary is used to store words in the word list.

"""
from collections import deque

def word_ladder(begin_word, end_word, word_list):
    # If the end_word is not in the word_list, no valid transformation exists
    if end_word not in word_list:
        return 0
    
    # Convert the word_list to a set for fast lookups
    word_list = set(word_list)
    # Queue to store the current word and the number of transformations so far
    queue = deque([(begin_word, 1)])

    # Perform a BFS traversal
    while queue:
        word, length = queue.popleft()

        # Try all possible transformations of the current word
        for i in range(len(word)):
            for char in "abcdefghijklmnopqrstuvwxyz":
                # Form a new word by changing one character at a time
                new_word = word[:i] + char + word[i+1:]
                
                # If the new word is the end word, return the current length + 1
                if new_word == end_word:
                    return length + 1
                
                # If the new word is in the word list, add it to the queue
                if new_word in word_list:
                    word_list.remove(new_word)  # Remove to prevent re-visiting
                    queue.append((new_word, length + 1))
    
    # If no transformation sequence is found, return 0
    return 0

# Example usage
begin_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
print(word_ladder(begin_word, end_word, word_list))  # Output: 5

# Time Complexity: O(n * m) (where n is the number of words and m is the length of each word)

# Space Complexity: O(n)
"""
6. Top K Frequent Elements
Question: Write a Python program to find the "Top K Frequent Elements" in an array using a hashmap.

Comment: Use a hashmap to store the frequency of each element, then use a heap to find the top k frequent elements.


"""
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    # Create a frequency count of all elements in the list
    count = Counter(nums)
    # Use a heap to find the k largest elements based on their frequency
    return heapq.nlargest(k, count.keys(), key=count.get)

# Example usage
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(nums, k))  # Output: [1, 2]

# Time Complexity: O(n log k) (where n is the number of elements and k is the number of frequent elements)

# Space Complexity: O(n)

"""
7. Can Rearranged to Form Palindrome
Question: Write a Python program to check if a string can be rearranged to form a palindrome using a hashmap.

Comment: A string can be rearranged into a palindrome if at most one character has an odd frequency.

"""
from collections import Counter

def can_form_palindrome(s):
    # Count the frequency of each character in the string
    freq = Counter(s)
    # Count how many characters have an odd frequency
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    # A string can be rearranged to form a palindrome if at most one character has an odd frequency
    return odd_count <= 1

# Example usage
s = "civic"
print(can_form_palindrome(s))  # Output: True

# Time Complexity: O(n) (where n is the length of the string)

# Space Complexity: O(k) (where k is the number of unique characters)

"""
8. Group Anagrams
Question: Write a Python program to find all "Anagrams" in a list of strings using a hashmap.

Comment: We can use the sorted version of the string as the key in a hashmap to group anagrams together.
"""

from collections import defaultdict

def group_anagrams(strs):
    # Dictionary to group words by sorted characters
    anagrams = defaultdict(list)
    
    for word in strs:
        # Sort the word and use it as the key to group anagrams together
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    
    # Return the grouped anagrams as a list of lists
    return list(anagrams.values())

# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# Time Complexity: O(n * m log m) (where n is the number of strings and m is the length of the strings)

# Space Complexity: O(n)
"""
9. Subarray Sum Equals K
Question: Write a Python program to find the "Subarray Sum Equals K" using a hashmap.

Comment: Use a hashmap to store the prefix sums and find subarrays that sum to k.

"""

def subarray_sum(nums, k):
    # Dictionary to store the prefix sum and its frequency
    prefix_sum = {0: 1}  # Initialize with sum 0 at index -1
    current_sum = 0
    count = 0

    for num in nums:
        # Update the running sum
        current_sum += num
        
        # If current_sum - k exists in the dictionary, it means we found a subarray with sum = k
        if current_sum - k in prefix_sum:
            count += prefix_sum[current_sum - k]
        
        # Store or update the count of the current prefix sum
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

    return count

# Example usage
nums = [1, 2, 3]
k = 3
print(subarray_sum(nums, k))  # Output: 2

# Time Complexity: O(n) (where n is the size of the array)

# Space Complexity: O(n)

"""
10. Minimum Window Substring

Question: Write a Python program to find the "Minimum Window Substring" that contains all characters of a pattern using a hashmap.

Comment: This problem uses a sliding window approach and a hashmap to keep track of character frequencies.
"""


from collections import Counter

def min_window_substring(s, t):
    # Edge case: if t is empty, return an empty string
    if not s or not t:
        return ""
    
    # Frequency count of characters in t
    t_freq = Counter(t)
    # Initialize a dictionary to count characters in the current window
    window_freq = {}
    start, end = 0, 0  # Window boundaries
    min_len = float('inf')
    min_window = ""
    
    # Traverse the string to find the minimum window
    while end < len(s):
        # Add the current character to the window frequency
        window_freq[s[end]] = window_freq.get(s[end], 0) + 1
        end += 1
        
        # Check if the current window contains all characters from t
        while all(window_freq[char] >= t_freq[char] for char in t_freq):
            # Update the minimum window if the current window is smaller
            if end - start < min_len:
                min_len = end - start
                min_window = s[start:end]
            
            # Move the start pointer to reduce the window size
            window_freq[s[start]] -= 1
            start += 1
    
    return min_window if min_window else ""

# Example usage
s = "ADOBECODEBANC"
t = "ABC"
print(min_window_substring(s, t))  # Output: "BANC"

# Time Complexity: O(n) (where n is the length of the string)

# Space Complexity: O(m) (where m is the size of the pattern)
