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