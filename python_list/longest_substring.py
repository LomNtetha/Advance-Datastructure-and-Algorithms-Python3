"""1. Longest Substring Without Repeating Characters
🧠 Problem

Given a string s, return the length of the longest substring without repeating characters.

✅ Example
Input: "abcabcbb"
Output: 3
Explanation: "abc"
💻 Solution
"""
def longest_unique_substring(s):
    seen = set()   # Stores unique characters in current window
    left = 0           # Left pointer of sliding window
    max_length = 0     # Result

    for right in range(len(s)):
        # If duplicate character found, shrink window from left
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        # Add current character to set
        seen.add(s[right])

        # Update max length
        max_length = max(max_length, right - left + 1)

    return max_length


print(longest_unique_substring("abcabcbb"))  # 3


# Time Complexity: 𝑂(𝑛)

# Space Complexity:O(1) with constant character set sizes

"""
5. Return the Actual Longest Substring (No Repeats)
Problem

Return the actual substring instead of length.

✅ Example
Input: "pwwkew"
Output: "wke"

Input:  "abcabcbb"
Output: "abc"

Explanation:
The longest substring without repeating characters is "abc".
"""
def longest_unique_substring_str(s):
    seen = set()
    left = 0
    max_length = 0
    result = ""        # Store substring result

    for right in range(len(s)):
        # Remove duplicates
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        seen.add(s[right])

        # Update result if longer substring found
        if right - left + 1 > max_length:
            max_length = right - left + 1
            result = s[left:right+1]

    return result


print(longest_unique_substring_str("pwwkew"))  # "wke"

"""8. Optimized Longest Unique Substring (HashMap Index)
Optimized version using index tracking.

✅ Example
Input: "abba"
Output: 2
"""
def longest_unique_optimized(s):
    char_index = {}    # Store last seen index of each character
    left = 0
    max_length = 0

    for right in range(len(s)):
        # If character seen before, move left pointer
        if s[right] in char_index:
            left = max(left, char_index[s[right]] + 1)

        # Update latest index
        char_index[s[right]] = right

        # Update max length
        max_length = max(max_length, right - left + 1)

    return max_length


print(longest_unique_optimized("abba"))  # 2


"""10. Longest Palindromic Substring
Problem

Find the longest substring that is a palindrome.

✅ Example
Input: "babad"
Output: "bab" or "aba"
"""

def longest_palindrome(s):
    # Helper function to expand around center
    def expand(left, right):
         # Expand while characters on both sides match and we are within bounds
        while left >= 0 and right < len(s) and s[left] == s[right]:
              left -= 1  # Move left pointer outward
              right += 1  # Move right pointer outward
        
        # Return valid palindrome substring
        return s[left+1:right]

    result = ""

    for i in range(len(s)):
        # Odd length palindrome
        odd = expand(i, i)

        # Even length palindrome
        even = expand(i, i+1)

        # Pick longer one
        result = max(result, odd, even, key=len)

    return result


print(longest_palindrome("babad"))  # "bab" or "aba"

"""
Given a string s, find the length of the longest substring that is a palindrome.
A palindrome is a string that reads the same forward and backward.
The substring must be contiguous (continuous characters).

✅ Example
Input: s = "babad"
Output: 3
Explanation: "bab" or "aba" is the longest palindromic substring

"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Helper function to expand around a given center
        def expand_around_center(left: int, right: int) -> int:
            # Expand while:
            # 1. We are within bounds
            # 2. Characters on both sides are equal
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1   # move left pointer outward
                right += 1  # move right pointer outward
            
            # After loop ends, pointers go one step too far
            # So actual palindrome length = (right - 1) - (left + 1) + 1
            # Simplified to:
            return right - left - 1  

        max_len = 0  # Store maximum palindrome length found

        # Try every index as the center
        for i in range(len(s)):
            # Case 1: Odd-length palindrome (center at i)
            odd_length = expand_around_center(i, i)

            # Case 2: Even-length palindrome (center between i and i+1)
            even_length = expand_around_center(i, i + 1)

            # Take the maximum of current results
            max_len = max(max_len, odd_length, even_length)

        return max_len


# Example usage
solution = Solution()
print(solution.longestPalindrome("babad"))  # Output: 3

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)


"""
Problem: Longest Increasing Substring
🧠 Problem

Given an array nums, return:
The actual substring

👉 Rules:

Must be continuous (no skipping)
Each next element must be strictly greater
✅ Example
Input:  [10, 9, 2, 5, 3, 7, 101, 18]
Output:
Substring: [3, 7, 101]

👉 Other valid substring: [2, 5] (but shorter)
"""
def longest_increasing_substring(nums):
    # If list is empty, return empty result
    if not nums:
        return []

    left = 0           # Start of current window
    best_start = 0     # Start index of best substring found
    max_len = 1       # Track length internally (not returned)

    # Right pointer expands the window
    for right in range(1, len(nums)):

        # If sequence breaks (not strictly increasing)
        if nums[right] <= nums[right - 1]:
            left = right   # reset window start

        # Current window length
        curr_len = right - left + 1

        # Update best window if longer
        if curr_len > max_len:
            max_len = curr_len
            best_start = left

    # Return ONLY the substring
    return nums[best_start:best_start + max_len]


# Example
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_increasing_substring(nums))
# Output: [3, 7, 101]

# Time Complexity: O(n)
# Space Complexity: O(n) (because of returned substring)

"""
Problem

Given an array nums, return the length of the longest strictly increasing substring.

👉 Must be continuous (no skipping)

✅ Example
Input:  [10, 9, 2, 5, 3, 7, 101, 18]
Output: 3

Explanation:
Longest increasing substring is [3, 7, 101]
"""
def longest_increasing_substring_length(nums):
    # If empty, no substring exists
    if not nums:
        return 0

    left = 0        # Start of current window
    max_len = 1     # Best length found

    # Expand window with right pointer
    for right in range(1, len(nums)):

        # If sequence breaks (not increasing)
        if nums[right] <= nums[right - 1]:
            left = right   # reset window

        # Calculate current window length
        curr_len = right - left + 1

        # Update maximum length
        max_len = max(max_len, curr_len)

    return max_len


# Example
print(longest_increasing_substring_length([10, 9, 2, 5, 3, 7, 101, 18]))
# Output: 3

# ⏱ Time Complexity: O(n)
# We loop through the array once
# Each element is visited only one time

# 👉 Very efficient

# 🧠 Space Complexity: O(1)
# We only use a few variables:
# left
# max_len
# curr_len

"""
2. Longest Substring With At Most K Distinct Characters
🧠 Problem

Return the length of the longest substring with at most k distinct characters.

✅ Example
Input: s = "eceba", k = 2
Output: 3
Explanation: "ece"
💻 Solution
"""

from collections import Counter

def longest_k_distinct(s, k):
    left = 0
    max_len = 0
    count = Counter()   # stores frequency of characters in window

    for right in range(len(s)):
        # Add current character to window
        count[s[right]] += 1

        # If more than k distinct chars → shrink window
        while len(count) > k:
            count[s[left]] -= 1

            # Remove character if its count becomes 0
            if count[s[left]] == 0:
                del count[s[left]]

            left += 1
        

         # Calculate length AFTER window is valid
        curr_len = right - left + 1

        # Update maximum length
        max_len = max(max_len, curr_len)

    return max_len


# Example
print(longest_k_distinct("eceba", 2))  # Output: 3

# ⚡ Complexity
# Time: O(n)
# Space: O(k) (at most k characters in Counter)

"""
3. Longest Substring With At Most Two Distinct Characters
🧠 Problem

Same as above, but k = 2.

✅ Example
Input: s = "ccaabbb"
Output: 5
Explanation: "aabbb"
💻 Solution
"""

def longest_two_distinct(s):
    # Reuse previous function
    return longest_k_distinct(s, 2)


print(longest_two_distinct("ccaabbb"))  # 5

"""
4. Longest Repeating Character Replacement
🧠 Problem

You can replace at most k characters. Find longest substring with same characters.

✅ Example
Input: s = "AABABBA", k = 1
Output: 4
💻 Solution
"""

from collections import Counter

def character_replacement(s, k):
    count = Counter()   # stores frequency of characters in current window
    left = 0            # left pointer of sliding window
    max_freq = 0        # highest frequency of a single character in window
    res = 0             # result (maximum window size)

    # expand window using right pointer
    for right in range(len(s)):
        # add current character to frequency map
        count[s[right]] += 1

        # update the most frequent character in the window
        max_freq = max(max_freq, count[s[right]])

        # if we need more than k replacements, shrink window
        if (right - left + 1) - max_freq > k:
            # remove left character from window
            count[s[left]] -= 1
            left += 1  # move left pointer forward

        curr_window =  right - left + 1

        # update maximum length found so far
        res = max(res,curr_window)

    return res


# Example
print(character_replacement("AABABBA", 1))  # Output: 4

# ⚡ Complexity
# Time: O(n)
# Space: O(1) (at most 26 letters)

"""
6. Longest Substring With Equal 0s and 1s

Problem

Find longest substring with equal number of 0s and 1s.

✅ Example
Input: "110100"
Output: 6
"""

def longest_equal_01(s):
    prefix_map = {0: -1}  # Store first occurrence of count
    count = 0             # Balance counter
    max_length = 0

    for i in range(len(s)):
        # Convert '0' → -1 and '1' → +1
        if s[i] == '1':
            count += 1
        else:
            count -= 1

        # If same count seen before → valid substring
        if count in prefix_map:
            max_length = max(max_length, i - prefix_map[count])
        else:
            prefix_map[count] = i

    return max_length


print(longest_equal_01("110100"))  # 6

"""7. Longest Substring With K Replacements (General)
Problem

Similar to character replacement but generalized.

✅ Example
Input: s = "ABAB", k = 2
Output: 4
"""
from collections import Counter

def longest_replacement_general(s, k):
    count = Counter()
    left = 0
    max_freq = 0
    res = 0

    for right in range(len(s)):
        # add current character
        count[s[right]] += 1

        # track most frequent character in window
        max_freq = max(max_freq, count[s[right]])

        # shrink window if replacements needed > k
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        current_len = right - left + 1

        # update result
        res = max(res,current_len)

    return res


print(longest_replacement_general("ABAB", 2))  # 4


"""9. Longest Substring With At Least K Repeating Characters
Problem

Each character must appear at least k times.

✅ Example
Input: s = "aaabb", k = 3
Output: 3
Explanation: "aaa"
"""
from collections import Counter

def longest_substring_k_repeating(s, k):
    # Base case
    if not s:
        return 0

    counter = Counter(s)

    for i, char in enumerate(s):
        # If a character appears less than k → split problem
        if counter[char] < k:
            left = longest_substring_k_repeating(s[:i], k)
            right = longest_substring_k_repeating(s[i+1:], k)
            return max(left, right)

    # If all characters valid
    return len(s)


print(longest_substring_k_repeating("aaabb", 3))  # 3


"""
Problem

Find the length of the longest palindromic subsequence in a string.

Example:

Input:  "bbbab"
Output:  4   # "bbbb"
"""


def longest_palindrome_subseq(s):
    n = len(s)

    # dp[i][j] = LPS length in substring s[i..j]
    dp = [[0] * n for _ in range(n)]

    # every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # build the table bottom-up
    for length in range(2, n + 1):  # substring length
        for i in range(n - length + 1):
            j = i + length - 1

            # if characters match
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                # take best by skipping one side
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


# Test
print(longest_palindrome_subseq("bbbab"))  # 4

"""
Longest Increasing Subsequence (LIS)
🧩 Problem

Given an array nums, return the length of the longest strictly increasing subsequence.

👉 A subsequence means:

You can skip elements
But order must stay the same
✅ Example
Input:  [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: One LIS is [2, 3, 7, 101]
"""

def length_of_lis(nums):
    n = len(nums)

    # dp[i] = longest increasing subsequence ending at i
    dp = [1] * n  # every element is at least length 1

    for i in range(n):
        for j in range(i):
            # if increasing order found
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# Test
print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))  # 4

"""
Problem

Given an array nums, return the actual longest increasing subsequence (LIS), not just its length.

👉 Rules:

The subsequence must be strictly increasing
You can skip elements
Maintain original order
✅ Example
Input:  [10, 9, 2, 5, 3, 7, 101, 18]
Output: [2, 3, 7, 101]

👉 Note: There can be multiple valid answers like [2, 5, 7, 101]
"""
def longest_increasing_subsequence(nums):
    n = len(nums)
    
    # dp[i] will store the actual LIS ending at index i
    dp = [[num] for num in nums]   # start with each number alone
    
    for i in range(n):
        for j in range(i):
            # If increasing and longer subsequence found
            if nums[i] > nums[j] and len(dp[j]) + 1 > len(dp[i]):
                # Extend previous subsequence
                dp[i] = dp[j] + [nums[i]]
    
    # Return the longest subsequence from dp
    return max(dp, key=len)


print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
# Output: [2, 3, 7, 101]
# 🚀 Complexity
# Time: O(n²) (simple DP)
# Space: O(n)