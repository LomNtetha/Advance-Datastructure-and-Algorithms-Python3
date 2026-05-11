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

def longest_increasing_substring(nums):

    left = 0
    max_len = 1
    best_start = 0

    for right in range(1,len(nums)):

        if nums[right] <= nums[right - 1]:
            left = right

        cur_windwow = right -left +1

        if cur_windwow > max_len:
            max_len = cur_windwow
            best_start = left

    return nums[best_start:best_start+max_len]

nums = [10, 9, 2, 5, 3, 7, 101, 18]

print(longest_increasing_substring(nums))

def length_longest_increasing_substring(nums):

    left = 0
    max_len = 1

    for right in range(1,len(nums)):

        if nums[right] <= nums[right-1]:

            left = right

        current_len = right - left+ 1
        max_len = max(max_len,current_len)

    return max_len

nums = [10, 9, 2, 5, 3, 7, 101, 18]

print(length_longest_increasing_substring(nums))

from collections import Counter

def longest_k_distinct(s,k):

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

        curr_len = right - left+1
        max_len = max(max_len,curr_len)

    return max_len

s = "ccaabbb"
k = 2

print(longest_k_distinct(s,k))

from collections import Counter

def longest_repeating_charater(s,k):

    max_freq = 0
    left = 0
    res = 0
    count = Counter()

    for right in range(len(s)):
        count[s[right]] += 1

        max_freq = max(max_freq, count[s[right]])

        while (right - left + 1) - max_freq > k:

            count[s[left]] -= 1
            left += 1

        curr_window = right -left + 1

        res = max(res,curr_window)

    return res


s = "AABABBA"
k = 1

print(longest_repeating_charater(s,k))
import re
from collections import Counter
def most_appear_words(paragraph):

    result = []
    words = re.findall(r'\b\w+\b', paragraph.lower())

    count = Counter(words)

    max_freq = max(count.values())

    for word,freq in count.items():

        if freq >= max_freq:
            result.append(word)

    return result



paragraph = "Hello world. Hello everyone. World is beautiful."

print(most_appear_words(paragraph))

from collections import Counter

import re
def more_common_fruits(text):
    
    fruits = re.findall(r'\b\w+\b',text.lower())
    result = []
    count = Counter(fruits)

    freq_fruits = count.most_common()

    for word,frq in freq_fruits:

        result.append(word)

    return result

text = "apple banana apple apple orange banana"

print(more_common_fruits(text))

from collections import Counter
import re

def top_words_character_5(text):

    words = re.findall(r'\b[a-zA-Z]+\b',text.lower())
    count_words = Counter(words)
    top_words = count_words.most_common(5)

    characters = re.findall(r'[a-zA-z]', text.lower())
    count_char = Counter(characters)
    top_char = count_char.most_common(5)
    
    print("\ntop 5 words")
    for word,frq_word in top_words:

        print(f"{word}:{frq_word}")

    print("\ntop 5 characters")
    for char,frq_char in top_char:

        print(f"{char}:{frq_char}")

text = "This is a simple sentence example. This sentence is simple."

top_words_character_5(text)

from collections import defaultdict
def group_words_paragraph(sentences):

    map_word = defaultdict(set)

    for i, sentence in enumerate(sentences):
        

        words = sentence.split()

        for word in words:
            map_word[word].add(i)

    result = []

    for indexes in map_word.values():
        if len(indexes) > 1:
            result.append(list(indexes))

    return result


sentences = [
  "hello world the world is beautiful",
  "i am tired today hello world",
]

print(group_words_paragraph(sentences))

from collections import defaultdict
def group_words_names(paragraphs):

    map_word = defaultdict(set)

    for i,paragraph in enumerate(paragraphs):

        words = paragraph.split()

        for word in words:
            map_word[word].add(i)

    result = []

    for para,indexes in map_word.items():
        if len(indexes) == len(paragraphs):
            result.append(para)

    return result

paragraphs = [
    "hello world beautiful day",
    "hello everyone in the world",
    "what a beautiful world hello"
]

print(group_words_names(paragraphs))


def sentence_longest_words(sentences):

    max_words = 0

    result = ""

    for sentence in sentences:

        word_count = len(sentence.split())

        if word_count > max_words:
            max_words=word_count
            result = sentence

    return result

sentences = [
    "programming is fun",
    "i like python"
]
print(sentence_maximum_words(sentences))
