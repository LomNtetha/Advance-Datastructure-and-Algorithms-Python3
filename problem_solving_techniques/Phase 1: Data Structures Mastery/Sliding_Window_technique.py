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

"""
time complexity is: 𝑂(𝑛)
This means the algorithm runs in linear time relative to the number of elements in the input 
Space Complexity: 𝑂(1)
This indicates that the algorithm uses a fixed amount of space.
"""

from typing import List, Optional, Set
from collections import deque
from collections import defaultdict

class Solution:
    def maxSumSubarray(self, nums: List[int], k: int) -> int:
        # Step 1: Initialize variables
        max_sum = 0  # This will store the maximum sum found
        current_sum = 0  # This will store the current window sum
        
        # Step 2: Sum the first 'k' elements
        for i in range(k):
            current_sum += nums[i]  # Calculate the sum of the first 'k' elements
        max_sum = current_sum  # Initialize max_sum with the current_sum
        
        # Step 3: Slide the window across the array
        for i in range(k, len(nums)):
            # Update current_sum by adding the next element and removing the element going out of the window
            current_sum += nums[i] - nums[i - k]
            # Update max_sum if the new current_sum is greater
            max_sum = max(max_sum, current_sum)
        
        return max_sum  # Return the maximum sum found

# Example Usage
nums = [2, 1, 5, 1, 3, 2]
k = 3
solution = Solution()
print(solution.maxSumSubarray(nums, k))  # Output: 9

"""
Subarray with Sum Equal to Target
Example Question: Given an array of positive integers, find the subarray that sums up to a given target.

Input:

nums = [1, 2, 3, 4, 5]
target = 9
Approach:

Use two pointers to form a sliding window. Start both pointers at the beginning and move the right pointer to grow the sum until it equals or exceeds the target.
If the sum exceeds the target, move the left pointer to reduce the sum.
Time Complexity: O(n) – Each element is visited once.

"""

class Solution:
    def subarraySum(self, nums: List[int], target: int) -> Optional[List[int]]:
        # Initialize the left pointer for the sliding window and the current sum
        left = 0
        current_sum = 0
        
        # Iterate over each element with the right pointer to adjust the window size
        for right in range(len(nums)):
            # Expand the window by adding the current number at right pointer to current_sum
            current_sum += nums[right]
            
            # If current_sum exceeds target, shrink the window from the left side
            while current_sum > target and left <= right:
                # Subtract nums[left] from current_sum and move the left pointer to the right
                current_sum -= nums[left]
                left += 1
            
            # Check if current_sum is equal to the target
            if current_sum == target:
                # If we find the sum, return the subarray from left to right (inclusive)
                return nums[left:right + 1]
        
        # If no subarray is found that adds up to the target, return None
        return None

# Example Usage
nums = [1, 2, 3, 4, 5]
target = 9
solution = Solution()
print(solution.subarraySum(nums, target))  # Output: [2, 3, 4]



"""
Example Question: Given a string s, find the length of the longest substring without repeating characters.

Input:

s = "abcabcbb"
Output: 3 (The longest substring is "abc").
Approach:

Use a sliding window with two pointers (start and end) to maintain the current substring. Use a hash set to track the characters in the window. If a repeating character is found, move the start pointer to shrink the window until there are no repeating characters.

"""

"""
Time Complexity: 𝑂(𝑛)

Space Complexity:O(1) with constant character set sizes.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # Hash set to store characters in the current substring
        left = 0  # Left pointer for the sliding window
        max_length = 0  # Variable to track the maximum length
        
        for right in range(len(s)):  # Right pointer for the sliding window
            # If the character is already in the set, move the left pointer
            while s[right] in char_set:
                char_set.remove(s[left])  # Remove the leftmost character
                left += 1  # Move left pointer to the right
            
            char_set.add(s[right])  # Add the current character to the set
            max_length = max(max_length, right - left + 1)  # Update max length
        
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

"""
Time Complexity: O(n)
The algorithm processes each element in the array at most twice (once when expanding the right pointer and once when contracting the left pointer).

Space Complexity: O(1)
Only a fixed number of variables are used (not dependent on the input size), so the space complexity is constant.

"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)  # Get the length of the input array
        left = 0  # Initialize the left pointer for the sliding window
        current_sum = 0  # Initialize the sum of the current window
        min_len = float('inf')  # Initialize min_len to infinity to find the minimum
        
        # Iterate through the array using the right pointer
        for right in range(n):
            current_sum += nums[right]  # Expand the window by adding the current element
            
            # While the current sum is greater than or equal to the target, we can shrink the window
            while current_sum >= target:
                # Update the minimum length of the valid subarray found
                min_len = min(min_len, right - left + 1)  # right - left + 1 gives the length of the window
                current_sum -= nums[left]  # Remove the leftmost element from the sum
                left += 1  # Move the left pointer to the right to shrink the window
        
        # Check if we found any valid subarray; if not, return 0
        return min_len if min_len != float('inf') else 0

# Example Usage
nums = [2, 3, 1, 2, 4, 3]  # Input array
target = 7  # Target sum
solution = Solution()  # Create an instance of the Solution class
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
"""
Time Complexity:
O(n): Each element is added and removed from the deque at most once.
Space Complexity:
O(k): The deque will store at most k indices, where k is the size of the sliding window.

"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:  # Handle edge case where nums is empty
            return []
        
        n = len(nums)  # Length of the input array
        result = []  # This will store the maximums for each window
        dq = deque()  # Deque to store indices of potential maximums
        
        for i in range(n):
            # Remove indices that are out of the bounds of the current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()  # Remove the leftmost index (oldest element)

            # Remove indices of elements that are less than the current element
            # because they will never be the maximum when current element is in the window
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()  # Remove indices from the back

            dq.append(i)  # Add the current index to the deque

            # Start adding results to output after the first k elements
            if i >= k - 1:
                result.append(nums[dq[0]])  # The maximum is at the front of the deque
        
        return result

# Example Usage
nums = [1, 3, -1, -3, 5, 3, 6, 7]  # Input array
k = 3  # Size of the sliding window
solution = Solution()  # Create an instance of the Solution class
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
"""


"""
from collections import defaultdict
from typing import List

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or not s:  # Edge case: if k is 0 or string is empty
            return 0
        
        char_count = defaultdict(int)  # Dictionary to store the count of characters in the current window
        left = 0  # Left pointer of the sliding window
        max_length = 0  # Variable to keep track of the maximum length found

        # Iterate through the string with the right pointer
        for right in range(len(s)):
            char_count[s[right]] += 1  # Include the current character in the window
            
            # While we have more than k distinct characters, shrink the window from the left
            while len(char_count) > k:
                char_count[s[left]] -= 1  # Decrease the count of the leftmost character
                if char_count[s[left]] == 0:
                    del char_count[s[left]]  # Remove it from the dictionary if its count drops to 0
                left += 1  # Move the left pointer to the right
            
            # Update the maximum length found
            max_length = max(max_length, right - left + 1)  # Update max length of the valid window

        return max_length  # Return the maximum length found

# Example Usage
s = "eceba"  # Input string
k = 2  # Maximum number of distinct characters
solution = Solution()  # Create an instance of the Solution class
print(solution.lengthOfLongestSubstringKDistinct(s, k))  # Output: 3


"""
Prefix Sum Array for Range Minimum Query
Problem Statement: Given an integer array nums, compute the minimum value for each subarray of length k.

Example:

Input:
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
Output:
[-1, -3, -3, -3, 3, 3]
Explanation: The minimums of all subarrays of size 3 are [-1, -3, -3, -3, 3, 3].



"""


class Solution:
    def minSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        result = []  # To store the minimums of each sliding window
        deq = deque()  # Deque to store indices of elements in the current window
        
        for i in range(len(nums)):
            # Remove indices that are out of the current window
            if deq and deq[0] < i - k + 1:
                deq.popleft()
            
            # Remove elements from the deque that are greater than the current element
            # because they will not be needed (they can't be the minimum if the current
            # element is smaller)
            while deq and nums[deq[-1]] > nums[i]:
                deq.pop()
            
            # Add the current element's index to the deque
            deq.append(i)
            
            # Once we reach the first full window, we can start recording results
            if i >= k - 1:
                result.append(nums[deq[0]])  # The minimum for the current window
        
        return result

# Example Usage
nums = [1, 3, -1, -3, 5, 3, 6, 7]  # Input array
k = 3  # Size of the sliding window
solution = Solution()  # Create an instance of the Solution class
print(solution.minSlidingWindow(nums, k))  # Output: [-1, -3, -3, -3, 3, 3]