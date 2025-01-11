"""
1. Maximum Subarray Sum (Kadane's Algorithm)
Problem Statement:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example:
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the largest sum = 6.

Input: nums = [1]
Output: 1
Explanation: The only subarray is [1].

Input: nums = [5, 4, -1, 7, 8]
Output: 23
Explanation: The subarray [5, 4, -1, 7, 8] has the largest sum = 23.
"""

"""
Type: Sliding Window, Greedy
Time Complexity: 
O(n)
Space Complexity: 
O(1)
"""

class Solution:
    def maxSubArray(self, nums):
        """
        Find the maximum sum of a contiguous subarray.
        
        Args:
        nums (List[int]): Input array
        
        Returns:
        int: Maximum sum of contiguous subarray
        """
        max_sum = float('-inf')  # Largest sum found so far
        current_sum = 0  # Current window sum

        for num in nums:
            current_sum = max(num, current_sum + num)  # Expand the window
            max_sum = max(max_sum, current_sum)  # Update the maximum sum found so far
        
        return max_sum

# Test
print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6

"""
2. Longest Increasing Subsequence
Problem Statement:
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence derived from another sequence where all elements are in the same order, but not necessarily contiguous.

Example:
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.

Input: nums = [0, 1, 0, 3, 2, 3]
Output: 4

Input: nums = [7, 7, 7, 7, 7, 7, 7]
Output: 1
"""

"""
Type: Dynamic Programming
Time Complexity: 
O(n^2)
Space Complexity: 
O(n)
"""
class Solution:
    def lengthOfLIS(self, nums):
        """
        Find the length of the longest increasing subsequence.
        
        Args:
        nums (List[int]): Input array
        
        Returns:
        int: Length of the LIS
        """
        dp = [1] * len(nums)  # Initialize a DP array

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:  # Extend the subsequence
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)  # Return the longest subsequence length

# Test
print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4

"""
3. Best Time to Buy and Sell Stock (Single Transaction)
Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the 𝑖 𝑡ℎ  day.
You want to maximize your profit by choosing a single day to buy one stock and a different day to sell.
Return the maximum profit you can achieve. If no profit is possible, return 0.

Example:
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.

Input: prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: In this case, no transactions are done, and the maximum profit is 0.
"""

"""
Type: Greedy
Time Complexity: 
O(n)
Space Complexity: 
O(1)
"""
class Solution:
    def maxProfit(self, prices):
        """
        Find the maximum profit from a single stock transaction.
        
        Args:
        prices (List[int]): Stock prices
        
        Returns:
        int: Maximum profit
        """
        min_price = float('inf')  # Minimum price seen so far
        max_profit = 0  # Maximum profit found so far

        for price in prices:
            min_price = min(min_price, price)  # Update minimum price
            max_profit = max(max_profit, price - min_price)  # Update maximum profit
        
        return max_profit

# Test
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5

"""
4. Climbing Stairs (Min Cost)
Problem Statement:
You are given an integer array cost where cost[i] is the cost of the 𝑖𝑡ℎ
  step on a staircase.
Once you pay the cost, you can either climb one or two steps. You need to reach the top with the minimum cost.
You can start from either step 0 or step 1.

Example:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Start at step 1, pay 15, and reach the top.

Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Take steps 0 → 2 → 4 → 6 → 8 → top.

"""
"""
Type: Dynamic Programming
Time Complexity: 
O(n)
Space Complexity: 
O(n)
"""
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        Find the minimum cost to climb to the top of the stairs.
        
        Args:
        cost (List[int]): Cost at each step
        
        Returns:
        int: Minimum cost to reach the top
        """
        dp = [0] * (len(cost) + 1)  # Initialize DP array

        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])  # Take 1 or 2 steps
        
        return dp[-1]  # Cost to reach the top

# Test
print(Solution().minCostClimbingStairs([10, 15, 20]))  # Output: 15

"""
5. Best Time to Buy and Sell Stock II (Multiple Transactions)
Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the i th day.
You can perform as many transactions as you like (buy one and sell one share of the stock multiple times).
Return the maximum profit you can achieve.

Example:
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 7
Explanation: Buy on day 2 (price = 1), sell on day 3 (price = 5), profit = 4. Then buy on day 4 (price = 3), sell on day 5 (price = 6), profit = 3.

Input: prices = [1, 2, 3, 4, 5]
Output: 4
Explanation: Buy on day 1 (price = 1), sell on day 5 (price = 5).
"""
"""
Type: Greedy
Time Complexity: 
O(n)
Space Complexity: 
O(1)
"""

class Solution:
    def maxProfit(self, prices):
        """
        Find the maximum profit from multiple stock transactions.
        
        Args:
        prices (List[int]): Stock prices
        
        Returns:
        int: Maximum profit
        """
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:  # Sell every profitable transaction
                profit += prices[i] - prices[i-1]
        
        return profit

# Test
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 7

"""
6. Coin Change (Dynamic Programming)
Problem Statement:
You are given an integer array coins representing denominations of coins and an integer amount representing a total amount of money.
Return the fewest number of coins needed to make up that amount. If it is not possible to make that amount, return -1.

You may assume that you have an infinite number of each coin.

Example:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 
11=5+5+1 (3 coins).

Input: coins = [2], amount = 3
Output: -1
Explanation: There is no combination of coins that sums to 3.

Input: coins = [1], amount = 0
Output: 0
"""

"""
Technique: Dynamic Programming
Time Complexity: 
O(n⋅amount), where  n is the number of coins.
Space Complexity: 
O(amount).
"""

class Solution:
    def coinChange(self, coins, amount):
        """
        Find the fewest number of coins needed to make up the amount.
        
        Args:
        coins (List[int]): List of coin denominations
        amount (int): Target amount
        
        Returns:
        int: Fewest coins needed or -1 if not possible
        """
        dp = [float('inf')] * (amount + 1)  # dp[i] stores the fewest coins to make amount i
        dp[0] = 0  # Base case: 0 coins to make amount 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)  # Choose the coin
        
        return dp[amount] if dp[amount] != float('inf') else -1

# Test
print(Solution().coinChange([1, 2, 5], 11))  # Output: 3
"""
7. House Robber (Dynamic Programming)
Problem Statement:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses are arranged in a line, and adjacent houses have security systems connected.
You cannot rob two adjacent houses.
Return the maximum amount of money you can rob without alerting the police.

Example:
Input: nums = [1, 2, 3, 1]
Output: 4
Explanation: Rob house 1 ($1) and house 3 ($3). Total = $4.

Input: nums = [2, 7, 9, 3, 1]
Output: 12
Explanation: Rob house 1 ($2), house 3 ($9), and house 5 ($1). Total = $12.
"""

"""
Technique: Dynamic Programming
Time Complexity: 
O(n), where  n is the number of houses.
Space Complexity: 
O(1), as we optimize to use constant space.
"""

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
"""
8. Target Sum (Dynamic Programming)
Problem Statement:
You are given an integer array nums and an integer target. You can add + or - before each integer in nums. Return the number of ways to assign symbols to make the sum of nums equal to target.

Example:
Input: nums = [1, 1, 1, 1, 1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to get the target sum:


+1−1+1+1+1=3

−1+1+1+1+1=3

+1+1−1+1+1=3

+1+1+1−1+1=3

+1+1+1+1−1=3
Input: nums = [1], target = 1
Output: 1

Technique: Dynamic Programming (Subset Sum)

Time Complexity: 
O(n⋅sum), where  n is the number of elements in nums.

Space Complexity: 
O(sum).
"""

class Solution:
    def findTargetSumWays(self, nums, target):
        """
        Find the number of ways to achieve the target sum with + and - operations.
        
        Args:
        nums (List[int]): Array of numbers
        target (int): Target sum
        
        Returns:
        int: Number of ways to achieve target
        """
        total_sum = sum(nums)
        if total_sum < abs(target) or (total_sum + target) % 2 != 0:
            return 0  # No solution exists

        # Subset sum to achieve (total_sum + target) // 2
        subset_sum = (total_sum + target) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # Base case: 1 way to achieve sum 0

        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]  # Add the ways from previous states
        
        return dp[subset_sum]

# Test
print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))  # Output: 5

"""
9. Shortest Path in Binary Matrix (Breadth-First Search)
Problem Statement:
Given an 

n×n binary matrix grid, return the length of the shortest path from the top-left corner to the bottom-right corner.
You can move in 8 directions, and the path can only travel through cells with value 0.
If no such path exists, return -1.

Example:
Input:
grid = [[0, 1], 
        [1, 0]]
Output: 2

Input:
grid = [[0, 0, 0], 
        [1, 1, 0], 
        [1, 1, 0]]
Output: 4

Technique: Breadth-First Search (BFS)
Time Complexity: 

O(n^2), where 
n is the size of the matrix.
Space Complexity: 
O(n^2), for the visited array.
"""

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        """
        Find the shortest path in a binary matrix from top-left to bottom-right.
        
        Args:
        grid (List[List[int]]): Binary matrix
        
        Returns:
        int: Length of the shortest path or -1 if no path exists
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1  # No path if start or end is blocked
        
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        queue = deque([(0, 0, 1)])  # (row, col, path length)
        visited = set((0, 0))

        while queue:
            r, c, path = queue.popleft()
            if (r, c) == (n - 1, n - 1):
                return path  # Reached destination
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, path + 1))
        
        return -1  # No path exists

# Test
print(Solution().shortestPathBinaryMatrix([[0, 1], [1, 0]]))  # Output: 2


"""
10. Knapsack Problem (Dynamic Programming)
Problem Statement:
Given weights and values of n items, and a maximum weight capacity W, find the maximum value you can achieve by selecting items such that their total weight does not exceed W.
You cannot split an item; either you take it or leave it.

Example:
Input:
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
W = 7

Output: 9
Explanation: Select items with weights 
3 and 4 for a total value of 
4+5=9.

Input:
weights = [2, 1, 3]
values = [4, 2, 3]
W = 4

Output: 6
Explanation: Select items with weights 
1 and 
3 for a total value of 
2+4=6.

Technique: Dynamic Programming
Time Complexity: 
O(n⋅W), where 

n is the number of items and 
W is the weight capacity.
Space Complexity: 
O(W), with space optimization.
"""

class Solution:
    def knapsack(self, weights, values, W):
        """
        Find the maximum value that can be obtained in the knapsack.
        
        Args:
        weights (List[int]): List of item weights
        values (List[int]): List of item values
        W (int): Maximum weight capacity of the knapsack
        
        Returns:
        int: Maximum value obtainable
        """
        dp = [0] * (W + 1)  # dp[i] stores the max value for capacity i

        for i in range(len(weights)):
            for j in range(W, weights[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
        
        return dp[W]

# Test
print(Solution().knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7))  # Output: 9

"""11. Edit Distance (Dynamic Programming)
Problem Statement:
Given two strings word1 and word2, return the minimum number of operations required to convert word1 into word2.
You have three operations available:

Insert a character
Delete a character
Replace a character

Example:

Input:
word1 = "horse"
word2 = "ros"

Output: 3

Explanation:
Replace 'h' with 'r'.
Delete 'o'.
Delete 'e'.

Input:
word1 = "intention"
word2 = "execution"

Output: 5
Explanation:

Replace 'i' with 'e'.
Replace 'n' with 'x'.
Replace 't' with 'c'.
Insert 'u'.
Replace 'n' with 'o'.
Technique: Dynamic Programming
Time Complexity: 
O(m⋅n), where 
m and  n are the lengths of the two strings.
Space Complexity: 
O(m⋅n), for the DP table."""

class Solution:
    def minDistance(self, word1, word2):
        """
        Find the minimum number of operations to convert word1 to word2.
        
        Args:
        word1 (str): Source string
        word2 (str): Target string
        
        Returns:
        int: Minimum operations needed
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # Create DP table

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j  # Insert all characters of word2
                elif j == 0:
                    dp[i][j] = i  # Delete all characters of word1
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # Characters match, no cost
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])  
                    # Insert, Delete, Replace
        
        return dp[m][n]

# Test
print(Solution().minDistance("horse", "ros"))  # Output: 3

""""
12. Longest Increasing Subsequence (Dynamic Programming)
Problem Statement:
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example:
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: The longest increasing subsequence is 
[2,3,7,101].

Input: nums = [0, 1, 0, 3, 2, 3]
Output: 4

Input: nums = [7, 7, 7, 7]
Output: 1

Technique: Dynamic Programming
Time Complexity: 
O(n ^2), for the nested loop solution.
Space Complexity: 
O(n), for the DP array.
"""

class Solution:
    def lengthOfLIS(self, nums):
        """
        Find the length of the longest increasing subsequence.
        
        Args:
        nums (List[int]): Input array
        
        Returns:
        int: Length of the LIS
        """
        dp = [1] * len(nums)  # dp[i] stores the LIS ending at index i
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

# Test
print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4

"""
13. Partition Equal Subset Sum (Dynamic Programming)
Problem Statement:
Given a non-empty array nums containing only positive integers, determine if the array can be partitioned into two subsets such that the sum of the elements in both subsets is equal.

Example:
Input:

nums = [1, 5, 11, 5]
Output: True
Explanation: The array can be partitioned as 

[1,5,5] and [11].

Input:
nums = [1, 2, 3, 5]
Output: False
Explanation: The array cannot be partitioned into subsets of equal sum.

Technique: Dynamic Programming (Subset Sum Problem)
Time Complexity: 
O(n⋅sum), where 

n is the length of nums, and sum is the total sum of the array.
Space Complexity: 

O(sum), using a 1D DP array.
"""

class Solution:
    def canPartition(self, nums):
        """
        Determine if the array can be partitioned into two subsets with equal sum.
        
        Args:
        nums (List[int]): Input array of positive integers
        
        Returns:
        bool: True if possible, otherwise False
        """
        total_sum = sum(nums)
        # If the total sum is odd, we cannot partition into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: 0 sum is always possible

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]

# Test
print(Solution().canPartition([1, 5, 11, 5]))  # Output: True
print(Solution().canPartition([1, 2, 3, 5]))  # Output: False

"""
14. Maximum Product Subarray (Dynamic Programming)
Problem Statement:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest product and return its product.

Example:
Input: nums = [2, 3, -2, 4]
Output: 6
Explanation: The subarray 

[2,3] has the largest product.

Input: nums = [-2, 0, -1]
Output: 0
Explanation: The result cannot be obtained from a single subarray due to the zero element.

Technique: Dynamic Programming (Tracking Min and Max Products)
Time Complexity: 
O(n), as we traverse the array once.
Space Complexity: 
O(1), as we use constant space.
"""


class Solution:
    def maxProduct(self, nums):
        """
        Find the maximum product subarray.
        
        Args:
        nums (List[int]): Input array
        
        Returns:
        int: Maximum product of a contiguous subarray
        """
        if not nums:
            return 0
        
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            temp = max_product
            max_product = max(nums[i], nums[i] * max_product, nums[i] * min_product)
            min_product = min(nums[i], nums[i] * temp, nums[i] * min_product)
            result = max(result, max_product)
        
        return result

# Test
print(Solution().maxProduct([2, 3, -2, 4]))  # Output: 6
print(Solution().maxProduct([-2, 0, -1]))   # Output: 0

"""
15. Word Break (Dynamic Programming)
Problem Statement:
Given a string s and a dictionary of strings wordDict, return True if s can be segmented into a space-separated sequence of one or more dictionary words.

Example:
Input:
s = "leetcode"
wordDict = ["leet", "code"]
Output: True
Explanation: The string can be segmented as "leet code".

Input:
s = "applepenapple"
wordDict = ["apple", "pen"]
Output: True
Explanation: The string can be segmented as "apple pen apple".

Technique: Dynamic Programming
Time Complexity: 
O(n^2), where 
𝑛
n is the length of the string s.
Space Complexity: 
O(n), for the DP array.
"""

class Solution:
    def wordBreak(self, s, wordDict):
        """
        Determine if the string can be segmented into words from the dictionary.
        
        Args:
        s (str): Input string
        wordDict (List[str]): List of words in the dictionary
        
        Returns:
        bool: True if segmentation is possible, otherwise False
        """
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: Empty string is always valid

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[len(s)]

# Test
print(Solution().wordBreak("leetcode", ["leet", "code"]))  # Output: True
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Output: False

"""
16. Longest Palindromic Substring (Dynamic Programming)
Problem Statement:
Given a string s, return the longest palindromic substring in s.

Example:
Input:

s = "babad"
Output: "bab"
Explanation: "bab" is a palindrome and "aba" is also a valid answer.

Input:
s = "cbbd"
Output: "bb"
Explanation: "bb" is the longest palindromic substring.

Technique: Dynamic Programming (Expand Around Center)
Time Complexity: 
O(n^2), where 
n is the length of the string.
Space Complexity: 
O(1), as we only use variables to store the result.
"""
class Solution:
    def longestPalindrome(self, s):
        """
        Find the longest palindromic substring.
        
        Args:
        s (str): Input string
        
        Returns:
        str: The longest palindromic substring
        """
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        if not s:
            return ""
        
        longest = ""
        for i in range(len(s)):
            odd_palindrome = expand_around_center(i, i)
            even_palindrome = expand_around_center(i, i + 1)
            
            longest = max(longest, odd_palindrome, even_palindrome, key=len)
        
        return longest

# Test
print(Solution().longestPalindrome("babad"))  # Output: "bab" or "aba"
print(Solution().longestPalindrome("cbbd"))  # Output: "bb"

"""
17. Merge Intervals (Greedy)
Problem Statement:
Given a collection of intervals, merge any overlapping intervals.

Example:
Input:

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output:

[[1, 6], [8, 10], [15, 18]]
Explanation:
Intervals [1, 3] and [2, 6] overlap, so we merge them into [1, 6].

Input:


intervals = [[1, 4], [4, 5]]
Output:


[[1, 5]]
Explanation: The intervals [1, 4] and [4, 5] can be merged into [1, 5].

Technique: Greedy
Time Complexity: 

O(nlogn), where 

n is the number of intervals, due to sorting.
Space Complexity: 

O(n), for storing the merged intervals.
"""

class Solution:
    def merge(self, intervals):
        """
        Merge overlapping intervals.
        
        Args:
        intervals (List[List[int]]): List of intervals
        
        Returns:
        List[List[int]]: Merged intervals
        """
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])  # Sort intervals by the start time
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            # If current interval overlaps with the last merged one
            if intervals[i][0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])
        
        return merged

# Test
print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Output: [[1, 6], [8, 10], [15, 18]]
print(Solution().merge([[1, 4], [4, 5]]))  # Output: [[1, 5]]

"""
18. Trapping Rain Water (Dynamic Programming / Two Pointers)
Problem Statement:
Given n non-negative integers representing the elevation of bars, where the width of each bar is 1, compute how much water it can trap after raining.

Example:
Input:

height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The water trapped between the bars is 6 units.

Technique: Two Pointers / Dynamic Programming
Time Complexity: 

O(n), where 
n is the length of the input list.
Space Complexity: 

O(1), as we use constant space for the two-pointer approach.
"""

class Solution:
    def trap(self, height):
        """
        Calculate how much water can be trapped between bars.
        
        Args:
        height (List[int]): Array representing the height of the bars
        
        Returns:
        int: Total amount of water trapped
        """
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0
        
        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                water_trapped += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water_trapped += max(0, right_max - height[right])
        
        return water_trapped

# Test
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6

"""19. Container With Most Water (Two Pointers)
Problem Statement:
You are given n non-negative integers representing the height of the walls. Find two indices 

i and j, such that the container formed by these two lines has the maximum area.

Example:
Input:

height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The container formed by lines at indices 1 and 8 will have the maximum area, which is 49.

Technique: Two Pointers
Time Complexity: 
O(n), where 
n is the number of lines.
Space Complexity: 
O(1), using constant space for two pointers.
"""
class Solution:
    def maxArea(self, height):
        """
        Calculate the maximum area of water between two lines.
        
        Args:
        height (List[int]): Array representing the height of the lines
        
        Returns:
        int: Maximum area of water
        """
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# Test
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49

"""
20. Kth Largest Element in an Array (Heap / Quickselect)
Problem Statement:
Find the kth largest element in an unsorted array.

Example:
Input:
nums = [3,2,1,5,6,4], k = 2
Output: 5
Explanation: The second largest element in the array is 5.

Technique: Heap or Quickselect
Time Complexity: 

O(nlogk), for the heap-based approach. Quickselect has an average complexity of 
O(n).
Space Complexity: 

O(k) for the heap-based solution.

"""
import heapq

class Solution:
    def findKthLargest(self, nums, k):
        """
        Find the kth largest element in an unsorted array.
        
        Args:
        nums (List[int]): Array of integers
        k (int): The kth position to find
        
        Returns:
        int: The kth largest element
        """
        return heapq.nlargest(k, nums)[-1]

# Test
print(Solution().findKthLargest([3,2,1,5,6,4], 2))  # Output: 5


"""
22. Breadth-First Search (BFS) for Shortest Path
Problem Statement:
Given an unweighted graph, find the shortest path from the source to all other nodes.

Example:
Input:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
source = 'A'
Output:
{'A': 0, 'B': 1, 'C': 1, 'D': 2}
Explanation: The shortest distances from 'A' to all other nodes.

Technique: BFS (Graph Traversal)
Time Complexity: 
O(V+E), where 
V is the number of vertices and 
E is the number of edges.
Space Complexity: 
O(V), for storing distances and the queue.

"""
from collections import deque

class Solution:
    def bfs(self, graph, source):
        """
        Perform BFS to find the shortest path in an unweighted graph.
        
        Args:
        graph (dict): An unweighted graph
        source (str): The source node
        
        Returns:
        dict: A dictionary of shortest paths
        """
        queue = deque([source])
        distances = {source: 0}
        
        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                if neighbor not in distances:
                    distances[neighbor] = distances[node] + 1
                    queue.append(neighbor)
        
        return distances

# Test
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
print(Solution().bfs(graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 1, 'D': 2}

""""
23. Top K Frequent Elements (Heap / Bucket Sort)
Problem Statement:
Given a non-empty array of integers, return the k most frequent elements.

Example:
Input:
nums = [1,1,1,2,2,3], k = 2

Output:
[1, 2]

Technique: Heap / Bucket Sort
Time Complexity: 

O(nlogk) where 

n is the number of elements in the input list.
Space Complexity: 
O(n) for storing frequency counts.
"""

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        """
        Find the k most frequent elements in the array.
        
        Args:
        nums (List[int]): The input list of integers
        k (int): The number of most frequent elements to return
        
        Returns:
        List[int]: List of the k most frequent elements
        """
        # Count the frequency of each element
        freq_map = Counter(nums)
        
        # Use a heap to get the top k frequent elements
        return [item[0] for item in heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])]

# Test
print(Solution().topKFrequent([1,1,1,2,2,3], 2))  # Output: [1, 2]

"""
24. Union-Find / Disjoint Set (Cycle Detection)
Problem Statement:
Given an undirected graph, determine if the graph contains a cycle.

Example:
Input:
edges = [[0,1],[1,2],[2,3],[3,0]]

Output:
True

Technique: Union-Find / Disjoint Set
Time Complexity: 

O(E⋅α(V)), where 
E is the number of edges and 
V is the number of vertices.
Space Complexity: 
O(V), for storing parent and rank arrays.
"""

class Solution:
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])  # Path compression
        return parent[x]
    
    def union(self, parent, rank, x, y):
        rootX = self.find(parent, x)
        rootY = self.find(parent, y)
        
        if rootX != rootY:
            # Union by rank
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
        else:
            return True  # Cycle detected
        
        return False
    
    def hasCycle(self, edges, n):
        parent = [i for i in range(n)]
        rank = [0] * n
        
        for u, v in edges:
            if self.union(parent, rank, u, v):
                return True
        
        return False

# Test
print(Solution().hasCycle([[0,1],[1,2],[2,3],[3,0]], 4))  # Output: True

"""
25. Find the Kth Smallest Element in a Sorted Matrix (Min-Heap)
Problem Statement:
Given an n x n matrix where each row and column is sorted in ascending order, find the kth smallest element.

Example:
Input:
matrix = [
  [1, 5, 9],
  [10, 11, 13],
  [12, 13, 15]
], k = 8


Output:
13

Technique: Min-Heap
Time Complexity:  O(klogn), where 
n is the size of the matrix.
Space Complexity:  O(n) for the heap.
    
"""
import heapq

class Solution:
    def kthSmallest(self, matrix, k):
        """
        Find the kth smallest element in a sorted matrix.
        
        Args:
        matrix (List[List[int]]): The n x n matrix
        k (int): The k-th smallest element to find
        
        Returns:
        int: The kth smallest element
        """
        n = len(matrix)
        heap = []
        
        # Initialize the heap with the first element from each row
        for i in range(n):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        
        count = 0
        while heap:
            val, r, c = heapq.heappop(heap)
            count += 1
            if count == k:
                return val
            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

# Test
matrix = [
  [1, 5, 9],
  [10, 11, 13],
  [12, 13, 15]
]
print(Solution().kthSmallest(matrix, 8))  # Output: 13

"""
26. Kth Largest Element in an Array (Min-Heap)
Problem Statement:
Given an unsorted array, find the kth largest element in it.

Example:
Input:
nums = [3,2,1,5,6,4], k = 2

Output:
5
Technique: Min-Heap
Time Complexity: O(nlogk)
Space Complexity: O(k)
"""

import heapq

class Solution:
    def findKthLargest(self, nums, k):
        """
        Find the kth largest element in an array.
        
        Args:
        nums (List[int]): The input array
        k (int): The k-th largest element to find
        
        Returns:
        int: The kth largest element
        """
        return heapq.nlargest(k, nums)[-1]

# Test
print(Solution().findKthLargest([3,2,1,5,6,4], 2))  # Output: 5

"""
27. Find Duplicate in an Array (Set-based approach)
Problem Statement:
Given an array, find the first duplicate number.

Example:
Input:
nums = [1,2,3,4,5,2]
Output:

Copy code
2
Technique: Hash Set
Time Complexity: 
O(n)
Space Complexity: 
O(n)
"""

class Solution:
    def findDuplicate(self, nums):
        """
        Find the first duplicate number in the array.
        
        Args:
        nums (List[int]): The input array
        
        Returns:
        int: The duplicate number
        """
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1

# Test
print(Solution().findDuplicate([1,2,3,4,5,2]))  # Output: 2

"""
28. Find the Median of Two Sorted Arrays
Problem Statement:
Given two sorted arrays, find the median of the two arrays.

Example:
Input:
nums1 = [1, 3], nums2 = [2]
Output:
2.0
Technique: Binary Search
Time Complexity: 
O(log(min(n,m))), where 
m are the lengths of the two arrays.
Space Complexity: O(1)
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        Find the median of two sorted arrays.
        
        Args:
        nums1 (List[int]): First sorted array
        nums2 (List[int]): Second sorted array
        
        Returns:
        float: The median of the two sorted arrays
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == y else nums2[partitionY]
            
            if maxX <= minY and maxY <= minX:
                if (x + y) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                high = partitionX - 1
            else:
                low = partitionX + 1

# Test
print(Solution().findMedianSortedArrays([1, 3], [2]))  # Output: 2.0

"""
29. Topological Sort (Directed Acyclic Graph)
Problem Statement:
Given a directed acyclic graph, return a topological ordering of its nodes.

Example:
Input:
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

Output:
['A', 'B', 'C', 'D']
Technique: DFS or Kahn's Algorithm (BFS)
Time Complexity: 
O(V+E)
Space Complexity: 
O(V+E)
"""

from collections import defaultdict, deque

class Solution:
    def topologicalSort(self, graph):
        """
        Perform topological sort on a Directed Acyclic Graph.
        
        Args:
        graph (dict): The graph represented as adjacency list
        
        Returns:
        List[str]: The topologically sorted nodes
        """
        # Kahn's algorithm for topological sort (BFS)
        in_degree = defaultdict(int)
        for node in graph:
            for neighbor in graph[node]:
                in_degree[neighbor] += 1
        
        queue = deque([node for node in graph
                        if in_degree[node] == 0])
        top_order = []
        
        while queue:
            node = queue.popleft()
            top_order.append(node)
            
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return top_order

# Test
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}
print(Solution().topologicalSort(graph))  # Output: ['A', 'B', 'C', 'D']

"""
30. Sliding Window Maximum
Problem Statement:
Given an array of integers, find the maximum value in each sliding window of size k.

Example:
Input:
nums = [1,3,-1,-3,5,3,6,7], k = 3
Output:
[3,3,5,5,6,7]
Technique: Deque (Double-ended Queue)
Time Complexity: 
O(n)
Space Complexity: 
O(k)
"""

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        Find the maximum value in each sliding window of size k.
        
        Args:
        nums (List[int]): The input array
        k (int): The window size
        
        Returns:
        List[int]: The list of maximum values
        """
        result = []
        dq = deque()
        
        for i, num in enumerate(nums):
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(i)
            
            if dq[0] == i - k:
                dq.popleft()
            
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result

# Test
print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # Output: [3, 3, 5, 5, 6, 7]