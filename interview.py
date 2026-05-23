def longest_substring_length(s):

    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])

            left += 1

        seen.add(s[right])

        curr_window = right - left + 1

        max_length = max(max_length,curr_window)
    return max_length

s = "abcabcbb"

print(longest_substring_length(s))

def longest_substring(s):

    seen = set()
    left = 0
    max_len = 0
    result = ""


    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])

            left += 1

        seen.add(s[right])

        current_window = right - left + 1
        if current_window > max_len:
            max_len = current_window
            result = s[left:right+1]

    return result
s = "pwwkew"

print(longest_substring(s))