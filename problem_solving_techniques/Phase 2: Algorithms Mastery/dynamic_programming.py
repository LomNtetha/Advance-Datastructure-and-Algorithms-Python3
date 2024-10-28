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



from typing import List

"""
 A cab service offers three types of passes. 1D, 7D, 30D. A T days pass can be used for a continuous

# duration only. Consider the days of the year being labeled sequentially from 1 to 365. Travelling is

# required only on some selected days of the year(input). Given the cost of different passes and the

# days on which travel is required, Calculate the minimum amount using which we can travel on all these days.

# Input: days = [1,4,6,7,8,20], costs = [2,7,15]

# Output: 11(2 + 7 + 2)
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

