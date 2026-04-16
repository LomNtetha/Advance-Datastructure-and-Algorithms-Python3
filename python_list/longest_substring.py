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
    char_set = set()   # Stores unique characters in current window
    left = 0           # Left pointer of sliding window
    max_length = 0     # Result

    for right in range(len(s)):
        # If duplicate character found, shrink window from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character to set
        char_set.add(s[right])

        # Update max length
        max_length = max(max_length, right - left + 1)

    return max_length


print(longest_unique_substring("abcabcbb"))  # 3

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
def longest_k_distinct(s, k):
    char_count = {}    # Dictionary to count characters
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Add current character
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        # If more than k distinct characters, shrink window
        while len(char_count) > k:
            char_count[s[left]] -= 1

            # Remove char if count becomes 0
            if char_count[s[left]] == 0:
                del char_count[s[left]]

            left += 1
        
        # Update max length
        max_length = max(max_length, right - left + 1)

    return max_length


print(longest_k_distinct("eceba", 2))  # 3

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
def character_replacement(s, k):
    count = {}         # Frequency map
    left = 0
    max_freq = 0       # Highest frequency of a single char in window
    max_length = 0

    for right in range(len(s)):
        # Update frequency
        count[s[right]] = count.get(s[right], 0) + 1

        # Track most frequent character
        max_freq = max(max_freq, count[s[right]])

        # If replacements needed > k, shrink window
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        
        # Update answer
        max_length = max(max_length, right - left + 1)

    return max_length


print(character_replacement("AABABBA", 1))  # 4
"""
5. Return the Actual Longest Substring (No Repeats)
Problem

Return the actual substring instead of length.

✅ Example
Input: "pwwkew"
Output: "wke"
"""
def longest_unique_substring_str(s):
    char_set = set()
    left = 0
    max_length = 0
    result = ""        # Store substring result

    for right in range(len(s)):
        # Remove duplicates
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])

        # Update result if longer substring found
        if right - left + 1 > max_length:
            max_length = right - left + 1
            result = s[left:right+1]

    return result


print(longest_unique_substring_str("pwwkew"))  # "wke"
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
def longest_replacement_general(s, k):
    count = {}
    left = 0
    max_freq = 0
    max_length = 0

    for right in range(len(s)):
        # Add current character
        count[s[right]] = count.get(s[right], 0) + 1

        # Track max frequency
        max_freq = max(max_freq, count[s[right]])

        # If invalid window, shrink
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)

    return max_length


print(longest_replacement_general("ABAB", 2))  # 4

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
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # Return valid palindrome substring
        return s[left+1:right]

    result = ""

    for i in range(len(s)):
        # Odd length palindrome
        temp1 = expand(i, i)

        # Even length palindrome
        temp2 = expand(i, i+1)

        # Pick longer one
        result = max(result, temp1, temp2, key=len)

    return result


print(longest_palindrome("babad"))  # "bab" or "aba"