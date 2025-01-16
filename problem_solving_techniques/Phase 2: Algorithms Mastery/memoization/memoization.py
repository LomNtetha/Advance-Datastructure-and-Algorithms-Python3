"""
1. Fibonacci Sequence (Memoized)
Calculate the n-th Fibonacci number using memoization.

Example:

Input: n = 5
Output: 5
"""
class Solution:
    def fibonacci(self, n: int, memo=None) -> int:
        # Initialize memoization dictionary if not provided
        if memo is None:
            memo = {}
        
        # Base case: if n is 0 or 1, return n as it’s the base case
        if n <= 1:
            return n
        
        # Check if the result is already in the memo
        if n not in memo:
            # Recursive case: store the result in the memo
            memo[n] = self.fibonacci(n - 1, memo) + self.fibonacci(n - 2, memo)
        
        return memo[n]

sol = Solution()
print(sol.fibonacci(10))  # Output: 55


# Complexity:
# Time: O(n) - Each Fibonacci number is computed once.
# Space: O(n) - Space used by the memoization dictionary.

"""
2. Factorial Calculation (Memoized)
Find the factorial of a given integer n using memoization.

Example:

Input: n = 4
Output: 24
"""

class Solution:
    def factorial(self, n: int, memo=None) -> int:
        # Initialize memoization dictionary if not provided
        if memo is None:
            memo = {}
        
        # Base case: if n is 0 or 1, factorial is 1
        if n == 0 or n == 1:
            return 1
        
        # Check if the result is already in the memo
        if n not in memo:
            # Recursive case: store the result in the memo
            memo[n] = n * self.factorial(n - 1, memo)
        
        return memo[n]
# Example usage
sol = Solution()
print(sol.factorial(5))  # Output: 120

# Complexity:
# Time: O(n) - Each factorial value is computed once.
# Space: O(n) - Space used by the memoization dictionary.
"""
3. Climbing Stairs
Count the number of distinct ways to climb n stairs, taking 1 or 2 steps at a time.

Example:

Input: n = 3
Output: 3 (ways: 1+1+1, 1+2, 2+1)
"""


class Solution:
    def climb_stairs(self, n: int, memo=None) -> int:
        # Initialize memoization dictionary if not provided
        if memo is None:
            memo = {}
        
        # Base case: there is 1 way to climb 0 stairs and 1 way to climb 1 stair
        if n <= 1:
            return 1
        
        # Check if the result is already in the memo
        if n not in memo:
            # Recursive case: sum of ways to climb (n-1) and (n-2) stairs
            memo[n] = self.climb_stairs(n - 1, memo) + self.climb_stairs(n - 2, memo)
        
        return memo[n]

# Complexity:
# Time: O(n) - Each step count is computed once.
# Space: O(n) - Space used by the memoization dictionary.
"""
4. Longest Common Subsequence
Find the length of the longest common subsequence of two strings.

Example:

Input: text1 = "abcde", text2 = "ace"
Output: 3 (LCS is "ace")
"""


class Solution:
    def longest_common_subsequence(self, text1: str, text2: str, i: int = 0, j: int = 0, memo=None) -> int:
        # Initialize memoization dictionary if not provided
        if memo is None:
            memo = {}
        
        # Base case: if we reach the end of either string
        if i == len(text1) or j == len(text2):
            return 0
        
        # Check if the result is already in the memo
        if (i, j) not in memo:
            # If characters match, increment count and recurse
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + self.longest_common_subsequence(text1, text2, i + 1, j + 1, memo)
            else:
                # If not, take the max of skipping one character from either string
                memo[(i, j)] = max(
                    self.longest_common_subsequence(text1, text2, i + 1, j, memo),
                    self.longest_common_subsequence(text1, text2, i, j + 1, memo)
                )
        
        return memo[(i, j)]

# Complexity:
# Time: O(m * n) - Where m and n are the lengths of the two strings.
# Space: O(m * n) - Space used by the memoization dictionary.
"""
5. Coin Change Problem
Given an amount and a list of coin denominations, determine the number of ways to make the amount.

Example:

Input: coins = [1, 2, 5], amount = 5
Output: 4 (ways: [5], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1])
"""

class Solution:
    def coin_change(self, coins: list, amount: int, memo=None) -> int:
        # Initialize memoization dictionary if not provided
        if memo is None:
            memo = {}
        
        # Base case: if amount is 0, one way to make change (no coins)
        if amount == 0:
            return 1
        
        # Base case: if amount is less than 0, no way to make change
        if amount < 0:
            return 0
        
        # Check if the result is already in the memo
        if amount not in memo:
            total_ways = 0
            for coin in coins:
                total_ways += self.coin_change(coins, amount - coin, memo)
            memo[amount] = total_ways
        
        return memo[amount]

# Complexity:
# Time: O(n * amount) - Where n is the number of coins.
# Space: O(amount) - Space used by the memoization dictionary.
"""
6. Edit Distance (Levenshtein Distance)
Compute the minimum edit distance between two strings (insertions, deletions, substitutions).

Example:

Input: word1 = "horse", word2 = "ros"
Output: 3 (horse -> rorse -> rose -> ros)
"""


class Solution:
    def min_distance(self, word1: str, word2: str, i: int = 0, j: int = 0, memo=None) -> int:
        # Initialize memoization dictionary if not provided
        if memo is None:
            memo = {}
        
        # Base case: if one string is empty, return length of the other string
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        
        # Check if the result is already in the memo
        if (i, j) not in memo:
            if word1[i] == word2[j]:
                memo[(i, j)] = self.min_distance(word1, word2, i + 1, j + 1, memo)
            else:
                # Compute minimum of insertion, deletion, and substitution
                memo[(i, j)] = 1 + min(
                    self.min_distance(word1, word2, i + 1, j, memo),    # Deletion
                    self.min_distance(word1, word2, i, j + 1, memo),    # Insertion
                    self.min_distance(word1, word2, i + 1, j + 1, memo) # Substitution
                )
        
        return memo[(i, j)]

# Complexity:
# Time: O(m * n) - Where m and n are the lengths of the two strings.
# Space: O(m * n) - Space used by the memoization dictionary.
"""
7. Unique Paths in a Grid
Count unique paths from the top-left to bottom-right of an m x n grid.

Example:

Input: m = 3, n = 2
Output: 3 (paths: down->down->right, down->right->down, right->down->down)

"""
class Solution:
    def unique_paths(self, m: int, n: int, memo=None) -> int:
        # Initialize memoization dictionary if not provided
        if memo is None:
            memo = {}
        
        # Base case: if at the first row or first column, only one path possible
        if m == 1 or n == 1:
            return 1
        
        # Check if the result is already in the memo
        if (m, n) not in memo:
            # Recursive case: sum paths from the left and above cells
            memo[(m, n)] = self.unique_paths(m - 1, n, memo) + self.unique_paths(m, n - 1, memo)
        
        return memo[(m, n)]

# Complexity:
# Time: O(m * n) - Each cell is computed once.
# Space: O(m * n) - Space used by the memoization dictionary.
"""
8. Palindromic Substrings
Count how many substrings of a given string are palindromic.

Example:

Input: s = "abc"
Output: 3 (palindromic substrings: "a", "b", "c")
"""

class Solution:
    def count_substrings(self, s: str, start: int = 0, end: int = 0, memo=None) -> int:
        # Initialize memoization dictionary if not provided
        if memo is None:
            memo = {}
        
        # Base case: if we've checked the entire string
        if start == len(s):
            return 0
        
        # Count palindromic substrings by expanding around the center
        if (start, end) not in memo:
            count = 0
            # Expand around single character
            while end < len(s) and s[start] == s[end]:
                count += 1
                end += 1
            # Count palindromes
            memo[(start, end)] = count + self.count_substrings(s, start + 1, start + 1, memo)
        
        return memo[(start, end)]

# Complexity:
# Time: O(n^2) - Each substring is checked for being a palindrome.
# Space: O(n) - Space used by the memoization dictionary.
"""
9. House Robber Problem
Maximize the amount of money you can rob from a line of houses without robbing two adjacent ones.

Example:

Input: nums = [2, 7, 9, 3, 1]
Output: 12 (rob houses 1, 3, and 5)
"""


class Solution:
    def rob(self, nums: list[int], n: int = None, memo=None) -> int:
        # Initialize memoization dictionary if not provided
        if memo is None:
            memo = {}
        
        if n is None:
            n = len(nums)
        
        # Base case: if there are no houses, return 0
        if n == 0:
            return 0
        # Base case: if only one house, return its value
        if n == 1:
            return nums[0]
        
        # Check if the result is already in the memo
        if n not in memo:
            # Recursive case: max of robbing this house + skip previous or skip this house
            memo[n] = max(nums[n - 1] + self.rob(nums, n - 2, memo), self.rob(nums, n - 1, memo))
        
        return memo[n]

# Complexity:
# Time: O(n) - Each house is considered once.
# Space: O(n) - Space used by the memoization dictionary.
"""
10. Maximum Product Cut (Dynamic Programming)
Given a rod of length n, maximize the product of the lengths of the pieces when the rod is cut.

Example:

Input: n = 10
Output: 36 (cut into pieces of lengths 3, 3, and 4)

"""

class Solution:
    def max_product_cut(self, n: int, memo=None) -> int:
        # Initialize memoization dictionary if not provided
        if memo is None:
            memo = {}
        
        # Base case: if rod length is 1, can't cut it
        if n <= 1:
            return 0
        
        # Check if the result is already in the memo
        if n not in memo:
            max_product = 0
            # Try cutting the rod at each length and take the maximum product
            for i in range(1, n):
                max_product = max(max_product, i * self.max_product_cut(n - i, memo))
            memo[n] = max_product
        
        return memo[n]

# Complexity:
# Time: O(n^2) - Each length can be checked with all possible cuts.
# Space: O(n) - Space used by the memoization dictionary.
"""
These questions are frequently encountered in coding interviews and can effectively demonstrate understanding
of memoization techniques and dynamic programming principles.
"""