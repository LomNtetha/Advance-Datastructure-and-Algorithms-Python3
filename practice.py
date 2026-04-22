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


def length_LIS(nums):

    n = len(nums)

    dp = [1] * n

    for i in range(n):
        for j in range(i):

            if nums[i] < nums[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)

nums = [10, 9, 2, 5, 3, 7, 101, 18]

print(length_LIS(nums))

def longset_increaing_subsquence(nums):

    n = len(nums)

    dp = [[num] for num in nums]

    for i in range(n):
        for j in range(i):

            if nums[i] > nums[j] and len(dp[j]) + 1 > len(dp[i]):
                
                dp[i] = dp[j] + [nums[i]]

    return max(dp,key=len)


nums = [10, 9, 2, 5, 3, 7, 101, 18]


print(longset_increaing_subsquence(nums))


def longest_Increasing_substring(nums):

    left = 0
    best_start = 0
    max_len = 0

    for right in range(len(nums)):

        if nums[right] <= nums[right-1]:

            left = right

        curr_len = right - left + 1

        if curr_len > max_len:
            max_len = curr_len
            best_start = left

    return nums[best_start:best_start+max_len]

nums = [10, 9, 2, 5, 3, 7, 101, 18]

print(longest_Increasing_substring(nums))

def longest_increasing_substring_length(nums):

    if not nums:
        return 0
    
    left  = 0
    max_len = 1

    for right in range(1,len(nums)):

        if nums[right] <= nums[right - 1]:

            left = right


        curr_len = right - left + 1

        max_len = max(max_len,curr_len)

    return max_len



nums = [10, 9, 2, 5, 3, 7, 101, 18]

print(longest_increasing_substring_length(nums))

from collections import Counter
def longest_k_distincs(s,k):

    left = 0
    max_len = 0
    count = Counter()

    for right in range(len(s)):

        count[s[right]] += 1

        while len(count) > k:
            count[s[left]] -= 1

            if count[s[left]] == 0:
                del count[s[left]]
                
            left += 1
            
        current_len = right - left + 1
            
        max_len = max(max_len, current_len)

    return max_len

s = "eceba"
k = 2

print(longest_k_distincs(s,k))

def get_intent(payload):

    result = []

    for intent in payload["message"]["nlp"]["intents"]:

        result.append((intent["name"], intent["confidence"]))

    return result

   

payload = {
    "message": {
        "nlp": {
            "intents": [
                {"name": "greet", "confidence": 0.98},
                {"name": "help", "confidence": 0.85},
                {"name": "order", "confidence": 0.60},
                {"name": "bye", "confidence": 0.40},
                {"name": "fallback", "confidence": 0.20}
            ]
        }
    }
}

print(get_intent(payload))

def get_all_intents_plain(payload):

    result  = ""

    for intent in payload["message"]["nlp"]["intents"]:

        result += f"{intent["name"]}: {intent["confidence"]}\n"

    return result


payload = {
    "message": {
        "nlp": {
            "intents": [
                {"name": "greet", "confidence": 0.98},
                {"name": "help", "confidence": 0.85},
                {"name": "order", "confidence": 0.60},
                {"name": "bye", "confidence": 0.40},
                {"name": "fallback", "confidence": 0.20}
            ]
        }
    }
}
print(get_all_intents_plain(payload))

def get_all_messages(payload):

    result = []

    messeges = payload["entry"][0]["changes"][0]["value"]["messages"]

    for msg in messeges:
        result.append(msg["text"]["body"])
    return result


payload = {
    "entry": [{
        "changes": [{
            "value": {
                "messages": [
                    {"text": {"body": "Hello bot"}},
                    {"text": {"body": "How are you?"}},
                    {"text": {"body": "Order pizza"}}
                ]
            }
        }]
    }]
}

print(get_all_messages(payload))

def get_all_messages_plain(payload):

    result = ""

    messages = payload["entry"][0]["changes"][0]["value"]["messages"]

    for msg in messages:

        result += f"{msg["text"]["body"]}\n"

    return result

payload = {
    "entry": [{
        "changes": [{
            "value": {
                "messages": [
                    {"text": {"body": "Hello bot"}},
                    {"text": {"body": "How are you?"}},
                    {"text": {"body": "Order pizza"}}
                ]
            }
        }]
    }]
}

print(get_all_messages_plain(payload))

from collections import Counter

import re

def frequently_words(paragraph):

    result = []

    words = re.findall(r'\b\w+\b', paragraph.lower())

    count = Counter(words)

    max_freq = max(count.values())

    for word,freq in count.items():

        if freq >= max_freq:
            result.append(word)

    return result
paragraph = "Hello world. Hello everyone. World is beautiful."

print(frequently_words(paragraph))

import re
from collections import Counter


def most_popular_words(text):

    result = []

    words = re.findall(r'\b\w+\b', text.lower())

    count = Counter(words)

    for word, freq in count.most_common():

        result.append(word)

    return result

text = "apple banana apple apple orange banana"

print(most_popular_words(text))

import re

from collections import Counter

def most_frequent_letter_and_words(text):

    words = re.findall(r'\b[a-zA-Z]+\b',text.lower())
    count_words = Counter(words)
    top_5_words = count_words.most_common(5)

    letters = [char for char in text.lower() if char.isalpha()]
    count_letters = Counter(letters)
    top_5_letters = count_letters.most_common(5)

    print("Top 5 words")
    for word, freq in top_5_words:
          print(f'{word}:{freq}')
    
    print("\nTop 5 letters")
    for character, freq_ch in top_5_letters:
        print(f'{character}:{freq_ch}')

text = "This is a simple sentence example. This sentence is simple."

print(most_frequent_letter_and_words(text))

from collections import Counter, defaultdict

def group_words_by_idexes(sentences):

    group_word = defaultdict(set)
    
    for i, sentence in enumerate(sentences):

        words = sentence.split()

        for word in words:
            group_word[word].add(i)

    result  = []

    for indexes in group_word.values():
        if len(indexes) > 1:
            result.append(list(indexes))

    return result

sentences = [
  "hello world the world is beautiful",
  "i am tired today hello world",
]

print(group_words_by_idexes(sentences))

from collections import defaultdict

def group_words_by_words(paragraphs):

    map_word = defaultdict(set)

    for i,sentence in enumerate(sentences):

        words = sentence.split()

        for word in words:

            map_word[word].add(i)

    result = []


    for para,indexes in map_word.items():

        if len(indexes) == len(sentences):

            result.append(para)

    return result


paragraphs = [
    "hello world beautiful day",
    "hello everyone in the world",
    "what a beautiful world hello"
]

print(group_words_by_words(paragraphs))




