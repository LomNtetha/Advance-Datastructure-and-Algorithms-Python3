
"""
1.  A cab service offers three types of passes. 1D, 7D, 30D. A T days pass can be used for a continuous

duration only. Consider the days of the year being labeled sequentially from 1 to 365. Travelling is

required only on some selected days of the year(input). Given the cost of different passes and the

days on which travel is required, Calculate the minimum amount using which we can travel on all these days.

Input: days = [1,4,6,7,8,20], costs = [2,7,15]

Output: 11(2 + 7 + 2)
"""

"""
Complexity Analysis
Time Complexity
The algorithm iterates from day 1 to the last travel day (days[-1]), which could be up to 365 (if the last day is day 365).
Each day, the calculation of dp[day] only involves a fixed number of operations (finding the minimum of three values).
Total Time Complexity: 
O(D), where  𝐷
is the last travel day (maximum 365).

Space Complexity
The dp dictionary stores costs for each day from 1 to days[-1]. In the worst case, if travel days span the entire year, dp could have up to 365 entries.
Total Space Complexity: 
O(D), where 
𝐷 is the last travel day.
"""


class Solution:
    def min_cost_for_travel(self, days: List[int], costs: List[int]) -> int:
        dp = {}  # Dictionary to store minimum cost up to each travel day
        travel_days = set(days)  # Convert days list to set for faster lookup
        
        # Iterate from day 1 up to the last day of travel
        for day in range(1, days[-1] + 1):
            if day not in travel_days:
                # If not traveling on this day, inherit previous day's cost
                dp[day] = dp.get(day - 1, 0)
            else:
                # Calculate the minimum cost to travel on this day
                dp[day] = min(
                    dp.get(day - 1, 0) + costs[0],  # Cost with 1-day pass
                    dp.get(day - 7, 0) + costs[1],  # Cost with 7-day pass
                    dp.get(day - 30, 0) + costs[2]  # Cost with 30-day pass
                )
        
        # The cost on the last travel day represents the minimum cost to cover all required days
        return dp[days[-1]]

# Example usage
days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
solution = Solution()
print("Minimum cost to cover all travel days:", solution.min_cost_for_travel(days, costs))


"""
2. Climbing Stairs
Question: Given n stairs, each time you can either climb 1 or 2 steps. Find the number of ways to reach the top of the staircase.
Example:
Input: n = 5
Output: 8
Constraints: 1 <= n <= 45

"""
class Solution:
    def climb_stairs(self, n: int) -> int:
        # Base cases: if there are 0 or 1 stairs, there's only one way to climb
        if n <= 2:
            return n
        
        # Initialize a list to store the number of ways to climb stairs
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2  # One way to climb 1 stair, two ways to climb 2 stairs
        
        # Fill the DP table
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]  # Total ways to climb to step i
            
        return dp[n]  # Return the number of ways to reach the top

# Example usage
sol = Solution()
print(sol.climb_stairs(5))  # Output: 8


"""
3. House Robber
Question: You are a robber trying to rob houses along a street. Each house has a certain amount of money, but you cannot rob two adjacent houses.
Find the maximum amount of money you can rob.
Example:
Input: houses = [2, 7, 9, 3, 1]
Output: 12
Constraints: 1 <= len(houses) <= 100
"""

class Solution:
    def rob(self, houses: list[int]) -> int:
        # If there are no houses, return 0
        if not houses:
            return 0
        # If there's only one house, return its value
        if len(houses) == 1:
            return houses[0]
        
        # Initialize a DP list to store the maximum amount that can be robbed
        dp = [0] * len(houses)
        dp[0], dp[1] = houses[0], max(houses[0], houses[1])  # Base cases
        
        # Fill the DP table
        for i in range(2, len(houses)):
            dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])  # Choose to rob or not
        
        return dp[-1]  # Return the maximum amount that can be robbed

# Example usage
sol = Solution()
print(sol.rob([2, 7, 9, 3, 1]))  # Output: 12

class Solution:
    def rob(self, nums):
        """
        Find the maximum amount of money that can be robbed without alerting the police.
        
        Args:
        nums (List[int]): Money in each house
        
        Returns:
        int: Maximum money that can be robbed
        """
        prev = curr = 0  # Initialize DP variables for the two previous states
        
        for num in nums:
            prev, curr = curr, max(curr, prev + num)  # Choose to rob or skip
        
        return curr  # Maximum money robbed

# Test
print(Solution().rob([2, 7, 9, 3, 1]))  # Output: 12

# Time Complexity: O(n) (linear time)
# Space Complexity: O(1) (constant space)



"""
House Robber II
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.That means the first house is the neighbor of the last one. Meanwhile, adjacent houses
have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without
alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3

"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        # Helper function to calculate max amount in a linear setup
        def rob_linear(houses):
            prev, curr = 0, 0
            for money in houses:
                prev, curr = curr, max(curr, prev + money)
            return curr
        
        # Handle edge cases
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # Calculate the two cases
        exclude_last = rob_linear(nums[:-1])  # Exclude the last house
        exclude_first = rob_linear(nums[1:])  # Exclude the first house
        
        # Return the maximum of the two cases
        return max(exclude_last, exclude_first)

# Example usage
sol = Solution()
print(sol.rob([2, 3, 2]))  # Output: 3
print(sol.rob([1, 2, 3, 1]))  # Output: 4
print(sol.rob([1, 2, 3]))  # Output: 3


"""
4. Coin Change
Question: Given an array coins representing coin denominations and an integer amount, find the minimum number of coins needed to make up that amount.
Return -1 if it is not possible.
Example:
Input: coins = [1, 2, 5], amount = 11
Output: 3 (5 + 5 + 1)
Constraints: 1 <= amount <= 10^4

"""
class Solution:
    def coin_change(self, coins: list[int], amount: int) -> int:
        # Initialize a DP array with infinity for all amounts
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # 0 coins are needed to make amount 0
        
        # Calculate the minimum coins needed for all amounts
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)  # Min coins needed

        # Separate calculation and return result
        result = dp[amount] if dp[amount] != float('inf') else -1
        return result  # Return the result after calculation

# Example usage
sol = Solution()
print(sol.coin_change([1, 2, 5], 11))  # Output: 3

"""
5. Longest Increasing Subsequence
Question: Given an array of integers nums, return the length of the longest strictly increasing subsequence.
Example:
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Constraints: 1 <= len(nums) <= 2500
"""
class Solution:
    def length_of_lis(self, nums: list[int]) -> int:
        # If the list is empty, return 0
        if not nums:
            return 0
        
        # Initialize a DP array where each element starts as 1
        dp = [1] * len(nums)
        
        # Fill the DP table
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:  # Check for increasing order
                    dp[i] = max(dp[i], dp[j] + 1)  # Update the LIS count
        
        return max(dp)  # Return the maximum length found

# Example usage
sol = Solution()
print(sol.length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4


"""
6. Partition Equal Subset Sum
Question: Given a list nums, determine if it can be split into two subsets with equal sums.
Example:
Input: nums = [1, 5, 11, 5]
Output: True
Constraints: 1 <= len(nums) <= 200
"""

class Solution:
    def can_partition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)  # Calculate total sum
        # If the sum is odd, we cannot partition it into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2  # Target for each subset
        # Initialize a set to store possible sums
        dp = set([0])
        
        # Fill the DP table
        for num in nums:
            dp |= {num + x for x in dp}  # Update possible sums
        
        return target in dp  # Return if target sum is possible

# Example usage
sol = Solution()
print(sol.can_partition([1, 5, 11, 5]))  # Output: True

"""
7. Knapsack Problem
Question: Given weights and values of n items and a weight capacity W, maximize the value you can get while staying within the weight limit.
Example:
Input: weights = [1, 3, 4, 5], values = [1, 4, 5, 7], W = 7
Output: 9
Constraints: 1 <= n, W <= 1000
"""
class Solution:
    def knapsack(self, weights: list[int], values: list[int], W: int) -> int:
        n = len(weights)  # Number of items
        # Initialize a DP array for maximum value at each weight
        dp = [0] * (W + 1)
        
        # Fill the DP table
        for i in range(n):
            for w in range(W, weights[i] - 1, -1):
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])  # Max value
        
        return dp[W]  # Return the maximum value that can be carried

# Example usage
sol = Solution()
print(sol.knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7))  # Output: 9


"""
8. Longest Common Subsequence
Problem: Find the length of the longest subsequence present in both strings.

Input: text1 = "abcde", text2 = "ace"

Output: 3 (subsequence: "ace")

Time Complexity: 
O(m×n)
Space Complexity: 
O(m×n)
"""


class Solution:
    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # Create a DP table initialized with 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:  # Characters match
                    dp[i][j] = dp[i - 1][j - 1] + 1  # Increment length of LCS
                else:  # Characters don't match
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # Take the maximum

        return dp[m][n]  # Return the length of the LCS

# Example usage
sol = Solution()
print(sol.longest_common_subsequence("abcde", "ace"))  # Output: 3

"""
9. Edit Distance
Problem: Find the minimum number of operations (insert, delete, replace) to convert one string into another.

Input: word1 = "horse", word2 = "ros"

Output: 3

Time Complexity: O(m×n)
Space Complexity: O(m×n)
"""

class Solution:
    def min_distance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # Create a DP table initialized with 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize base cases
        for i in range(m + 1):
            dp[i][0] = i  # Deletion cost
        for j in range(n + 1):
            dp[0][j] = j  # Insertion cost

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:  # Characters match
                    dp[i][j] = dp[i - 1][j - 1]  # No extra cost
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1,    # Deletion
                                   dp[i][j - 1] + 1,    # Insertion
                                   dp[i - 1][j - 1] + 1)  # Replacement

        return dp[m][n]  # Return the minimum edit distance

# Example usage
sol = Solution()
print(sol.min_distance("horse", "ros"))  # Output: 3

"""
10. Decode Ways
Problem: Given a string of digits, find the number of ways to decode it (1 to 26).

Input: s = "226"

Output: 3

Time Complexity: 
O(n)
Space Complexity: 
O(n)
"""

class Solution:
    def num_decodings(self, s: str) -> int:
        if not s or s[0] == '0':  # No valid encoding if empty or starts with '0'
            return 0

        # Create a DP array initialized for decoding counts
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1  # Base cases

        # Fill the DP table
        for i in range(2, len(s) + 1):
            if s[i - 1] != '0':  # Current digit can stand alone
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2:i]) <= 26:  # Previous and current digits can form a valid number
                dp[i] += dp[i - 2]

        return dp[len(s)]  # Return the number of decoding ways

# Example usage
sol = Solution()
print(sol.num_decodings("226"))  # Output: 3

"""
11. Minimum Path Sum
Problem: Find the minimum sum path from the top-left to the bottom-right corner of a grid.

Input: grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

Output: 7

Time Complexity: 
O(m×n)
Space Complexity: 
O(m×n)
"""


class Solution:
    def min_path_sum(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        # Create a DP table initialized with the same size as the grid
        dp = [[0] * n for _ in range(m)]
        
        # Fill the DP table
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]  # Start point
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]  # Only from left
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]  # Only from above
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]  # Min from left or above

        return dp[m - 1][n - 1]  # Return the min path sum to the bottom-right corner

# Example usage
sol = Solution()
print(sol.min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # Output: 7


"""
12. Maximum Subarray Sum (Kadane’s Algorithm)
Problem: Find the largest sum of any contiguous subarray.

Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output: 6

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def max_sub_array(self, nums: list[int]) -> int:
        current_sum = max_sum = nums[0]  # Initialize with the first element

        # Iterate through the array
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)  # Update current sum
            max_sum = max(max_sum, current_sum)  # Update max sum if needed

        return max_sum  # Return the maximum sum of contiguous subarray

# Example usage
sol = Solution()
print(sol.max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6

"""
13. Unique Paths
Problem: Find the number of unique paths from the top-left to the bottom-right corner of a grid.

Input: m = 3, n = 7

Output: 28

Time Complexity: O(m×n)
Space Complexity: O(m×n)
"""

class Solution:
    def unique_paths(self, m: int, n: int) -> int:
        # Create a DP table initialized with 1 for the first row and column
        dp = [[1] * n for _ in range(m)]

        # Fill the DP table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]  # Unique paths from top and left

        return dp[m - 1][n - 1]  # Return unique paths to the bottom-right corner

# Example usage
sol = Solution()
print(sol.unique_paths(3, 7))  # Output: 28

"""
14. Palindromic Substrings
Problem: Find the number of palindromic substrings in a string.

Input: s = "aaa"

Output: 6

Time Complexity: O(n^2)
Space Complexity: O(n 2)
"""

class Solution:
    def count_substrings(self, s: str) -> int:
        n = len(s)
        count = 0
        # Create a DP table initialized to False
        dp = [[False] * n for _ in range(n)]

        # Fill the DP table
        for length in range(1, n + 1):  # Length of substring
            for i in range(n - length + 1):
                j = i + length - 1  # End index
                if length == 1:  # Single character is a palindrome
                    dp[i][j] = True
                elif length == 2:  # Two characters are a palindrome if they are the same
                    dp[i][j] = s[i] == s[j]
                else:  # More than two characters
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

                if dp[i][j]:
                    count += 1  # Increment count if palindrome

        return count  # Return the number of palindromic substrings

# Example usage
sol = Solution()
print(sol.count_substrings("aaa"))  # Output: 6

"""
Fibonacci Sequence
Question: Given a positive integer n, return the n-th Fibonacci number. The Fibonacci sequence is defined as follows:
F(0) = 0, F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1
Example:
Input: n = 7
Output: 13
Constraints: 0 <= n <= 30
"""

class Solution:
    def fibonacci(self, n: int) -> int:
        # Base case: return n if it's 0 or 1
        if n <= 1:
            return n
        
        # Initialize a list to store Fibonacci numbers
        fib = [0] * (n + 1)
        fib[1] = 1  # F(1) = 1
        
        # Fill the Fibonacci table
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]  # F(n) = F(n-1) + F(n-2)
        
        return fib[n]  # Return the nth Fibonacci number

# Example usage
sol = Solution()
print(sol.fibonacci(7))  # Output: 13


# print(fibonacci(7))  # Output: 13

""""
The given code solves the problem of finding the longest palindromic substring in a given string. The question is:

"Given a string s, find the longest substring in s that is a palindrome. A palindrome is a string that reads the same backward as forward."
Time Complexity: O(n^2)
Space Complexity: O(n^2)

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)  # Length of the input string
        if n <= 1:
            return s  # If the string has 0 or 1 characters, it is already a palindrome
        
        # Initialize variables to store the start and maximum length of the longest palindrome
        start, max_len = 0, 1  
        
        # Create a 2D list (table) to store whether a substring s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]
        
        # Expand palindromic substrings from each end of the string
        for j in range(n):  # Right end of the substring
            for i in range(j + 1):  # Left end of the substring
                # Check if characters at positions i and j are the same
                # For length 1 or 2 substrings, they are palindromes if the characters match
                # For longer substrings, s[i:j+1] is a palindrome if s[i+1:j-1] is a palindrome
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True  # Mark the substring s[i:j+1] as a palindrome
                    
                    # Update longest palindrome details if this substring is longer
                    if j - i + 1 > max_len:
                        start, max_len = i, j - i + 1  # Update start index and max length

        # Return the longest palindromic substring found in s
        return s[start:start + max_len]

# Example usage
solution = Solution()
print(solution.longestPalindrome("babad"))  # Output: "bab" or "aba"


""""
Longest Palindromic Subsequence
Problem: Find the longest palindromic subsequence in a string.

Input: s = "bbbab"

Output: 4 (subsequence: "bbbb")
"""

"""
Time Complexity: 

O(n2)
Space Complexity: 

O(n^2)
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)  # Length of the input string
        if n <= 1:
            return n  # If the string has 0 or 1 characters, its length is the answer
        
        # Initialize variables to store the start and maximum length of the longest palindrome
        max_len = 1  
        
        # Create a 2D list (table) to store whether a substring s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]
        
        # Expand palindromic substrings from each end of the string
        for j in range(n):  # Right end of the substring
            for i in range(j + 1):  # Left end of the substring
                # Check if characters at positions i and j are the same
                # For length 1 or 2 substrings, they are palindromes if the characters match
                # For longer substrings, s[i:j+1] is a palindrome if s[i+1:j-1] is a palindrome
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True  # Mark the substring s[i:j+1] as a palindrome
                    
                    # Update longest palindrome length if this substring is longer
                    max_len = max(max_len, j - i + 1)

        # Return the length of the longest palindromic substring
        return max_len

# Example usage
solution = Solution()
print(solution.longestPalindrome("babad"))  # Output: 3
from typing import List
