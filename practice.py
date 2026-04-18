def longest_substring_length(s):

    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        seen.add(s[right])
        max_length = max(max_length, right -left + 1)
    return max_length

s = ("abcabcbb")

print(longest_substring_length(s))

def longest_substring(s):

    seen = set()
    left = 0
    max_lenght = 0
    result = ""

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left +=1 

        seen.add(s[right])

        if right - left + 1 > max_lenght:
            max_lenght = right - left + 1
            result = s[left:right+1]

    return result 

s = "pwwkew"

print(longest_substring(s))

def longest_palindrome(s):

    def expand(left,right):

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1:right]
    
    result = ""

    for i in range(len(s)):

        odd = expand(i,i)

        even  = expand(i,i+1)

        result = max(result,odd,even,key=len)

    return result

s = "babad"

print(longest_palindrome(s))

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
print(solution.longestPalindrome("bbbab"))  # Output: 3


def length_longest_palindrome_substring(s):

    def expand_from_center(left,right):

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1
    

    max_len = 0

    for i in range(len(s)):

        odd_len = expand_from_center(i,i)

        even_len = expand_from_center(i,i+1)

        max_len = max(max_len, odd_len,even_len)

    return max_len

s = "babad"

print(length_longest_palindrome_substring(s))