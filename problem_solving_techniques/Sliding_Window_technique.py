"""
Maximum Sum Subarray of Size K
Example Question: You are given an array of integers nums and an integer k. Find the maximum sum of a subarray of size k.

Input:

nums = [2, 1, 5, 1, 3, 2]
k = 3
Output:

9 (The subarray [5, 1, 3] has the largest sum: 5 + 1 + 3 = 9).
Approach:

Use a sliding window of size k. First, sum the first k elements, then slide the window one element at a time by adding the new element coming into the window and subtracting the element that is moving out of the window.
"""

from typing import List, Set
from collections import deque
from collections import defaultdict

class Solution:
    def maxSumSubarray(self, nums: List[int], k: int) -> int:
        # Step 1: Initialize variables
        max_sum = 0
        current_sum = 0
        
        # Step 2: Sum the first 'k' elements
        for i in range(k):
            current_sum += nums[i]
        max_sum = current_sum
        
        # Step 3: Slide the window across the array
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]  # Add new element and remove the old one
            max_sum = max(max_sum, current_sum)
        
        return max_sum

# Example Usage
nums = [2, 1, 5, 1, 3, 2]
k = 3
solution = Solution()
print(solution.maxSumSubarray(nums, k))  # Output: 9



"""
Example Question: Given a string s, find the length of the longest substring without repeating characters.

Input:

s = "abcabcbb"
Output: 3 (The longest substring is "abc").
Approach:

Use a sliding window with two pointers (start and end) to maintain the current substring. Use a hash set to track the characters in the window. If a repeating character is found, move the start pointer to shrink the window until there are no repeating characters.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        char_set: Set[str] = set()
        
        for end in range(len(s)):
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            char_set.add(s[end])
            max_length = max(max_length, end - start + 1)
        
        return max_length

# Example Usage
s = "abcabcbb"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))  # Output: 3

"""
Minimum Size Subarray Sum
Example Question: Given an array of positive integers nums and a positive integer target, find the minimal length of a contiguous subarray of which the sum is greater than or equal to target. If there is no such subarray, return 0.

Input:

nums = [2,3,1,2,4,3]
target = 7
Output: 2 (The subarray [4, 3] has the smallest length with sum 7).
Approach:

Use a sliding window to track the current sum of elements. Start with both pointers at the beginning of the array. Expand the window by moving the end pointer until the sum is greater than or equal to target. Then, shrink the window by moving the start pointer to find the smallest possible window that satisfies the condition.

"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        current_sum = 0
        min_length = float('inf')
        
        for end in range(len(nums)):
            current_sum += nums[end]
            
            while current_sum >= target:
                min_length = min(min_length, end - start + 1)
                current_sum -= nums[start]
                start += 1
        
        return min_length if min_length != float('inf') else 0

# Example Usage
nums = [2, 3, 1, 2, 4, 3]
target = 7
solution = Solution()
print(solution.minSubArrayLen(target, nums))  # Output: 2

"""
Sliding Window Maximum
Example Question: You are given an array nums and an integer k. You need to find the maximum value in each sliding window of size k.

Input:

nums = [1,3,-1,-3,5,3,6,7]
k = 3
Output:

[3, 3, 5, 5, 6, 7] (The maximum values for each window are [1,3,-1], [3,-1,-3], etc.)
Approach:

Use a deque (double-ended queue) to store the indices of elements in the current window in decreasing order of their values. The front of the deque contains the index of the largest element in the window. For each new element, remove elements from the back of the deque that are smaller than the current element since they cannot be the maximum.

"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Deque to store indices of array elements
        dq = deque()
        max_values = []
        
        for i in range(len(nums)):
            # Remove indices that are out of the current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove elements from the back of the deque that are less than the current element
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # Add the current element index to the deque
            dq.append(i)
            
            # The front of the deque is the largest element in the current window
            if i >= k - 1:
                max_values.append(nums[dq[0]])
        
        return max_values

# Example Usage
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
solution = Solution()
print(solution.maxSlidingWindow(nums, k))  # Output: [3, 3, 5, 5, 6, 7]


"""
 Longest Substring with At Most K Distinct Characters
Example Question: Given a string s and an integer k, find the length of the longest substring that contains at most k distinct characters.

Input:

s = "eceba"
k = 2
Output:

3 (The longest substring with at most 2 distinct characters is "ece").
Approach:

Use a sliding window with two pointers to track the current substring. Use a dictionary to count the occurrences of characters in the window. When the number of distinct characters exceeds k, move the start pointer to reduce the size of the window.

"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        start = 0
        max_length = 0
        char_count = defaultdict(int)
        
        for end in range(len(s)):
            char_count[s[end]] += 1
            
            while len(char_count) > k:
                char_count[s[start]] -= 1
                if char_count[s[start]] == 0:
                    del char_count[s[start]]
                start += 1
            
            max_length = max(max_length, end - start + 1)
        
        return max_length

# Example Usage
s = "eceba"
k = 2
solution = Solution()
print(solution.lengthOfLongestSubstringKDistinct(s, k))  # Output: 3