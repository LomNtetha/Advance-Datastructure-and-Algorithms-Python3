"""
Given an array arr = [2, 4, 1, 6, 3], find the sum of elements between index i = 1 and j = 3.


Consider arr = [2, 4, 1, 6, 3] and the prefix sum array prefix_sum = [2, 6, 7, 13, 16].

If you want to find the sum of elements from index 1 to 3 (i.e., [4, 1, 6]):

Using regular summing, it would be: 4 + 1 + 6 = 11
Using prefix sums, the sum from index 1 to 3 is: prefix_sum[3] - prefix_sum[0] = 13 - 2 = 11
"""

class Solution:
    def subarray_sum(arr: List[int], i: int, j: int) -> int:
        # Compute the prefix sum array on-the-fly
        prefix_sum = [0] * len(arr)
        
        prefix_sum[0] = arr[0]  # The first element is the same in prefix sum

        # Calculate the prefix sum for the entire array
        for k in range(1, len(arr)):
            prefix_sum[k] = prefix_sum[k - 1] + arr[k]

        # Determine the sum of the subarray from index i to j
        if i == 0:
            # If i is 0, return the prefix sum up to index j
            return prefix_sum[j]
        else:
            # Otherwise, return the difference of prefix sums
            # This gives us the sum of elements from index i to j
            return prefix_sum[j] - prefix_sum[i - 1]

# Example usage
arr = [2, 4, 1, 6, 3]
i, j = 1, 3
result = Solution.subarray_sum(arr, i, j)
print(f"The sum of the subarray from index {i} to {j} is: {result}")

"""
Question: Subarray Sum Query with Prefix Sums
You are given an array of integers, arr, and a list of queries. Each query specifies a pair of indices (i, j), representing the start 
and end indices of a subarray. For each query, return the sum of the elements within the subarray starting at index i and ending at index j (inclusive).

Input:

An integer array arr of length n.
A list of queries queries, where each query is a tuple (i, j) indicating the range of indices to calculate the subarray sum.
Output: Return the sum of elements within the subarray for each query.

Constraints:

1 <= len(arr) <= 10^5
1 <= arr[i] <= 10^4
0 <= i <= j < len(arr)
Example:

Input:
arr = [3, 5, 2, 8, 6]
queries = [(1, 3), (0, 4), (2, 4)]

Output:
Sum from index 1 to 3: 15
Sum from index 0 to 4: 24
Sum from index 2 to 4: 16

"""

from typing import List

class Solution:
    @staticmethod
    def subarray_sum(arr: List[int], i: int, j: int) -> int:
        # Initialize and compute the prefix sum array
        prefix_sum = [0] * len(arr)
        prefix_sum[0] = arr[0]
        
        # Compute prefix sums
        for k in range(1, len(arr)):
            prefix_sum[k] = prefix_sum[k - 1] + arr[k]
        
        # Return the sum of the subarray from index i to j
        if i == 0:
            return prefix_sum[j]
        else:
            return prefix_sum[j] - prefix_sum[i - 1]

# Example usage
arr = [3, 5, 2, 8, 6]
queries = [(1, 3), (0, 4), (2, 4)]

for i, j in queries:
    result = Solution.subarray_sum(arr, i, j)
    print(f"Sum from index {i} to {j}: {result}")



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

from typing import List, Tuple

class Solution:
    @staticmethod
    def query_sums(nums: List[int], queries: List[Tuple[int, int]]) -> List[int]:
        # Compute the prefix sum array on-the-fly
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]  # Initialize the first element

        # Calculate the prefix sum for the entire array
        for k in range(1, len(nums)):
            prefix_sum[k] = prefix_sum[k - 1] + nums[k]

        result = []
        # For each query, calculate the sum of the subarray
        for i, j in queries:
            if i == 0:
                # If i is 0, return the prefix sum up to index j
                result.append(prefix_sum[j])
            else:
                # Otherwise, return the difference of prefix sums
                result.append(prefix_sum[j] - prefix_sum[i - 1])

        return result

# Example usage
nums = [1, 3, 5]
queries = [(0, 2), (1, 2), (0, 1)]
result = Solution.query_sums(nums, queries)
print(result)  # Output: [9, 8, 4]

"""
Subarray Sum Equals K
Problem Statement: Given an integer array nums and an integer k, return the total number of continuous subarrays whose sum equals k.

Example:

Input:
nums = [1, 1, 1]
k = 2
Output: 2
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
Find the Minimum in Rotated Sorted Array
Problem Statement: Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
Find the minimum element in this rotated sorted array.

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


"""Problem Statement
Given an array of integers and a target integer  k, determine if there exists a contiguous subarray whose sum equals k.

Input:

An array of integers arr (e.g., [1, 3, -2, 5, -1])
An integer 
k (e.g., 5)
Output:

A boolean value: True if there exists a subarray with sum equal to k, False otherwise.
Example
Input: arr = [1, 3, -2, 5, -1], k = 5
Output: True (the subarray [3, -2, 5] has a sum of 5)

"""
"""
The time complexity is O(n): The solution iterates through the array once, performing constant-time operations (sum and set checks) for each element.

Space Complexity:
O(n): In the worst case, the prefix sums stored in the set could include all elements of the array

"""
class Solution:
    def subarray_with_sum_k(self, arr: List[int], k: int) -> bool:
        # Initialize the prefix sum and a set to store prefix sums
        prefix_sum = 0
        prefix_set = set()
        prefix_set.add(0)  # Adding 0 to handle edge cases
        
        # Iterate through the array
        for num in arr:
            prefix_sum += num  # Update the prefix sum
            
            # Check if the difference between prefix_sum and k has been seen before
            if (prefix_sum - k) in prefix_set:
                return True
            
            # Add the current prefix sum to the set
            prefix_set.add(prefix_sum)
        
        return False  # No subarray found

# Example usage
arr = [1, 3, -2, 5, -1]
k = 5
sol = Solution()
print(f"Is there a subarray with sum {k}? {sol.subarray_with_sum_k(arr, k)}")


"""
Given an array of integers and a target integer k, find the minimum length of a contiguous subarray whose sum is at least k.

Input:

An array of integers arr (e.g., [2, 3, 1, 2, 4, 3])
An integer 
k (e.g., 7)
Output:

An integer representing the minimum length of the subarray, or 0 if no such subarray exists.
Example
Input: arr = [2, 3, 1, 2, 4, 3], k = 7
Output: 2 (the subarray [4, 3] has a sum of 7)

"""
"""
Time Complexity:
O(n): The solution iterates through the array with a right pointer and potentially moves the left pointer through the array as well. 
Each pointer traverses the array at most once.
Space Complexity:
O(1): The algorithm only uses a fixed amount of additional space (for variables like prefix_sum, min_len, and left), regardless of the input size.


"""
class Solution:
    def min_subarray_len(self, arr: List[int], k: int) -> int:
        n = len(arr)  # Length of the input array
        prefix_sum = 0  # Initialize prefix sum
        min_len = n + 1  # Set min_len to a value larger than any possible length
        left = 0  # Left pointer for the sliding window
        
        # Iterate through the array with the right pointer
        for right in range(n):
            prefix_sum += arr[right]  # Update prefix sum
            
            # Shrink the window from the left until the sum is less than k
            while prefix_sum >= k:
                min_len = min(min_len, right - left + 1)  # Update minimum length
                prefix_sum -= arr[left]  # Remove the leftmost element from sum
                left += 1  # Move the left pointer to the right
        
        return min_len if min_len <= n else 0  # Return the result

# Example usage
arr = [2, 3, 1, 2, 4, 3]
k = 7
sol = Solution()
print(f"The length of the smallest subarray with sum ≥ {k}: {sol.min_subarray_len(arr, k)}")

"""
Given an array of integers, find the maximum sum of any contiguous subarray.

Input:

An array of integers arr (e.g., [-2, 1, -3, 4, -1, 2, 1, -5, 4])
Output:

An integer representing the maximum sum of a contiguous subarray.
Example
Input: arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6 (the subarray [4, -1, 2, 1] has a sum of 6)

"""

"""
Time Complexity:
O(n): The solution iterates through the array once, updating the maximum sum in constant time for each element.
Space Complexity:
O(1): The algorithm uses a constant amount of space for variables like max_sum and current_sum, irrespective of the input size.

"""

class Solution:
    def max_subarray_sum(self, arr: List[int]) -> int:
        max_sum = float('-inf')  # Initialize to the smallest possible value
        current_sum = 0  # Current subarray sum
        
        # Iterate through the array
        for num in arr:
            # Update the current sum; either start fresh with the current number or add it to the existing sum
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)  # Update the max sum if the current is greater
        
        return max_sum  # Return the maximum sum found

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sol = Solution()
print(f"The maximum sum of a subarray is: {sol.max_subarray_sum(arr)}")

"""
Given an array of integers and an integer k, find how many contiguous subarrays have a sum that is divisible by k.

Input:

An array of integers arr (e.g., [4, 5, 0, -2, -3, 1])
An integer 
k (e.g., 5)
Output:

An integer representing the count of subarrays whose sum is divisible by 
k.
Example
Input: arr = [4, 5, 0, -2, -3, 1], k = 5
Output: 7 (the subarrays [[4, 1], [5], [0], [-2, -3], [1], [4, 5, 0, -2, -3], [5, 0, -2, -3, 1]])

"""

"""
Time Complexity:
O(n): The solution iterates through the array once, with constant-time operations for each element to update the prefix sum and check the hash map.
Space Complexity:
O(n): In the worst case, the hash map can store a count for every possible modulo result, which can be up to 
k entries (at most k different modulo results).
"""
class Solution:
    def subarray_div_by_k(self, arr: List[int], k: int) -> int:
        prefix_sum = 0  # Initialize the prefix sum
        mod_map = {0: 1}  # Dictionary to count occurrences of mod results
        count = 0  # Count of subarrays divisible by k
        
        # Iterate through the array
        for num in arr:
            prefix_sum += num  # Update prefix sum
            mod = prefix_sum % k  # Get the mod of the prefix sum
            
            # Adjust for negative mod values
            if mod < 0:
                mod += k
            
            # If this mod has been seen before, it means there are subarrays that sum to a multiple of k
            if mod in mod_map:
                count += mod_map[mod]  # Increase count by the number of times this mod has occurred
            
            # Update the mod count in the map
            mod_map[mod] = mod_map.get(mod, 0) + 1
        
        return count  # Return the total count of subarrays

# Example usage
arr = [4, 5, 0, -2, -3, 1]
k = 5
sol = Solution()
print(f"The number of subarrays divisible by {k} is: {sol.subarray_div_by_k(arr, k)}")
