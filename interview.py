def longest_unique_substring(s):

    max_lenght = 0
    seen = set()
    left = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        length = right - left + 1
        max_lenght = max(max_lenght,length)

    return max_lenght
s = "abcabcbb"

print(longest_unique_substring(s))

def longest_substring(words):
    max_length = 0
    result = ""
    left = 0
    seen = set()

    for right in range(len(words)):

        while words[right] in seen:
            seen.remove(words[left])
            left += 1

        seen.add(words[right])

        lenght = right - left + 1
        if lenght > max_length:
            max_length = lenght
            result = words[left:right + 1]
    return result
        

words = "pwwkew"

print(longest_substring(words))


def longest_palindrome(s):

    def expand(left,right):

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1:right]
    result = ""

    for i in range(len(s)):

        odd = expand(i,i)

        even = expand(i,i+1)

        result = max(result,odd,even,key=len)

    return result


s = "babad"

print(longest_palindrome(s))

def length_longest_palindrome(s):
    def expand_length(left,right):

        max_len = 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        length = right - left - 1
        max_len = max(max_len,length)
        return max_len
    result = 0

    for i in range(len(s)):

        odd = expand_length(i,i)

        even = expand_length(i,i+1)

        result = max(result,odd,even)

    return result
s = "babad"

print(length_longest_palindrome(s))