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