"""
Problem Statement: Given an integer array nums, and multiple queries, each query asks for the sum of elements between indices i and j inclusive.

Example:

Input:

nums = [1, 3, 5]
queries = [(0, 2), (1, 2), (0, 1)]
Output:

[9, 8, 4]
Explanation:

Sum from index 0 to 2 is 1 + 3 + 5 = 9
Sum from index 1 to 2 is 3 + 5 = 8
Sum from index 0 to 1 is 1 + 3 = 4
Solution Using Prefix Sums:

"""

from collections import deque
from typing import List, Tuple


class Solution:
    def __init__(self, nums: List[int]):
        # Initialize and compute prefix sums
        self.prefix_sum = self.compute_prefix_sums(nums)
    
    def compute_prefix_sums(self, nums: List[int]) -> List[int]:
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        return prefix_sum

    def range_sum(self, i: int, j: int) -> int:
        if i == 0:
            return self.prefix_sum[j]
        return self.prefix_sum[j] - self.prefix_sum[i - 1]

# Example Usage
nums = [1, 3, 5]
queries = [(0, 2), (1, 2), (0, 1)]
solution = Solution(nums)

# Process each query
results = [solution.range_sum(i, j) for i, j in queries]
print(results)  # Output: [9, 8, 4]

"""
Subarray Sum Equals K
Problem Statement: Given an integer array nums and an integer k, return the total number of continuous subarrays whose sum equals k.

Example:

Input:
nums = [1, 1, 1]
k = 2
Output:

2
Explanation: The two subarrays are [1, 1] which sum to 2.

Solution Using Prefix Sums:"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = {0: 1}  # Initialize with prefix sum 0 having a count of 1
        current_prefix_sum = 0
        count_subarrays = 0
        
        for num in nums:
            current_prefix_sum += num
            
            # Check if there exists a prefix sum that equals current_prefix_sum - k
            if (current_prefix_sum - k) in prefix_sum_count:
                count_subarrays += prefix_sum_count[current_prefix_sum - k]
            
            # Update the hash map with the current prefix sum
            if current_prefix_sum in prefix_sum_count:
                prefix_sum_count[current_prefix_sum] += 1
            else:
                prefix_sum_count[current_prefix_sum] = 1
        
        return count_subarrays

# Example Usage
nums = [1, 1, 1]
k = 2
solution = Solution()
print(solution.subarraySum(nums, k))  # Output: 2

"""
Maximum Sum of a Subarray of Size K
Problem Statement: Given an integer array nums and an integer k, find the maximum sum of any contiguous subarray of size k.

Example:

Input:


nums = [2, 1, 5, 1, 3, 2]
k = 3
Output:

9
Explanation: The subarrays of size 3 are [2, 1, 5], [1, 5, 1], [5, 1, 3], and [1, 3, 2]. The maximum sum is 9 (from [5, 1, 3]).

"""

class Solution:
    def maxSumSubarray(self, nums: List[int], k: int) -> int:
        # Compute the sum of the first 'k' elements
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # Slide the window across the array
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        
        return max_sum

# Example Usage
nums = [2, 1, 5, 1, 3, 2]
k = 3
solution = Solution()
print(solution.maxSumSubarray(nums, k))  # Output: 9

"""
Prefix Sum Array for Range Minimum Query
Problem Statement: Given an integer array nums, compute the minimum value for each subarray of length k.

Example:

Input:

python
Copy code
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
Output:

python
Copy code
[-1, -3, -3, -3, 3, 3]
Explanation: The minimums of all subarrays of size 3 are [-1, -3, -3, -3, 3, 3].



"""

class Solution:
    def minSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        min_values = []
        dq = deque()  # To store indices of the elements
        
        for i in range(len(nums)):
            # Remove indices that are out of the bounds of the current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove elements from the back of the deque while the current element is smaller
            while dq and nums[dq[-1]] > nums[i]:
                dq.pop()
            
            # Add the current element index to the deque
            dq.append(i)
            
            # The minimum of the window is at the front of the deque
            if i >= k - 1:
                min_values.append(nums[dq[0]])
        
        return min_values

# Example Usage
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
solution = Solution()
print(solution.minSlidingWindow(nums, k))  # Output: [-1, -3, -3, -3, 3, 3]

"""
Find the Minimum in Rotated Sorted Array
Problem Statement: Suppose an array of length n sorted in ascending order is rotated between 1 and n times. Find the minimum element in this rotated sorted array.

Example:

Input:

nums = [3, 4, 5, 1, 2]
Output:

1
Explanation: The array was rotated 3 times. The minimum element is 1.

"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                # Minimum is in the right half
                left = mid + 1
            else:
                # Minimum is in the left half including mid
                right = mid
        
        # At the end of the loop, left == right, which is the minimum element
        return nums[left]

# Example Usage
nums = [3, 4, 5, 1, 2]
solution = Solution()
print(solution.findMin(nums))  # Output: 1