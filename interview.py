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