
import re
from collections import Counter
def most_common_word(paragraph):

    words = re.findall(r'\b\w+\b',paragraph.lower())


    count = Counter(words)

    most_freq = max(count.values())

    result = []

    for word,freq in count.items():

        if freq == most_freq:
            result.append(word)

    return result


paragraph = "Hello world. Hello everyone. World is beautiful."

print(most_common_word(paragraph))

from collections import defaultdict

def group_sentences_by_words(sentences):

    word_map = defaultdict(set)

    results = []



    for i, sentence in enumerate(sentences):

        words = sentence.split()


        for word in words:
            word_map[word].add(i)


    for indexes in  word_map.values():
        if len(indexes) > 1:
            results.append(list(indexes))

    return results

sentences = [
    "hello world the world is beautiful",
    "i am tired today hello world",
]

print(group_sentences_by_words(sentences))

import re
from collections import Counter
    
def most_common_freq_word(text):

    words = re.findall(r'\b\w+\b',text.lower())

    count = Counter(words)

    common_words = []

    for word, freq in count.most_common():

        common_words.append(word)

    return common_words

text = "apple banana apple banana apple banana orange banana"

print(most_common_freq_word(text))


import re

from collections import Counter

def words_with_thier_frequency(text):

    words = re.findall(r'\b\w+\b',text.lower())

    count = Counter(words)

    result = []


    for word,frequency in count.most_common():

        result.append((word,frequency))

    return result

text = "apple banana banana banana apple apple orange banana"

print(words_with_thier_frequency(text))

def is_pangram(sentence):

    letters = set(c.lower() for c in sentence if c.isalpha())

    return len(letters) == 26

sentence = "The quick brown fox jumps over a lazy dog"

print(is_pangram(sentence))

from collections import defaultdict

def group_word_by_sentence(sentences):

    map_word = defaultdict(set)

    for i,sentence in enumerate(sentences):

        words = sentence.split()

        for word in words:
            map_word[word].add(i)

    result = []

    for word,indexes in map_word.items():

        if len(indexes) == len(sentences):
            result.append(word)

    return result

sentences = [
    "hello world beautiful day",
    "hello everyone in the world",
    "what a beautiful world hello"
]

print(group_word_by_sentence(sentences))

def lenght_longest_substring(s):

    seen = set()
    left = 0
    max_len = 0

    for right, char in enumerate(s):

        while char in seen:
            seen.remove(s[left])
            left += 1

        seen.add(char)

        max_len = max(max_len, right - left + 1)

    return max_len

s = "abcabcbb"


print(lenght_longest_substring(s))


def count_palindrome(s):

    s = ''.join(c.lower() for c in s if c.isalnum())

    count = 0
    n = len(s)


    for center in range(2*n -1):

        left = center // 2
        right = left + center % 2

        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            right += 1
            left -= 1

    return count

s = "A man, a plan, a canal Panama!"


print(count_palindrome(s))

from collections import defaultdict
def group_anagrams(strs):

    groupAnagram = defaultdict(list)

    for s in strs:

        sorted_str = ''.join(sorted(s))
        groupAnagram[sorted_str].append(s)

    return list(groupAnagram.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(strs))


def reverse_words(s):

    return ' '.join(s.strip() .split() [::-1])

s = "hello world today is monday on the 16 feb 2026"

print(reverse_words(s))

from collections import Counter

def longest_palindome(s):

    n = len(s)

    res = ""

    for center in range(2*n-1):

        left = center // 2
        right = left + center % 2

        while left >=0 and right < n and s[left] == s[right]:
            if right - left + 1 > len(res):
                res = s[left:right + 1]

            left -=1
            right +=1
    return res

s = "babad"

print(longest_palindome(s))

from collections import Counter


def min_window(s,t):

    need = Counter(t)
    missing = len(t)

    left = 0
    start = 0
    end = 0

    for right,char in enumerate(s):

        if need[char]>0:
            missing -= 1
        need[char] -= 1


        while missing == 0:
            if (end == 0) or (right - left + 1) < (end - start + 1):
                start,end = left,right

            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1

    return s[start:end + 1]


s = "ADOBECODEBANC"
t = "ABC"

print(min_window(s,t))

def longestSentence(sentences):

    max_words = 0
    result = ""

    for sentence in sentences:
        word_count = len(sentence.split())

        if word_count > max_words:
            max_words = word_count
            result = sentence

    return result


sentences = [
    "hello world b b ",
    "this is c c g",
    "python"
]

print(longestSentence(sentences))

def longestcharacter(sentences):

    max_words = 0
    result = ""

    for sentence in sentences:
        count_char = sum(1 for c in sentence if c.isalpha())

        if count_char > max_words:
            max_words = count_char
            result = sentence

    return result
sentences = [
    "hello world m l p k p pp pp pp",
    "this is a leetcode style problem",
    "python"
]

print(longestcharacter(sentences))

from collections import Counter
import re

def most_letters_words(sentence):

    letters = [char for char in sentence.lower() if char.isalpha()]
    count_letter = Counter(letters)
    top_5_letters = count_letter.most_common(5)

    words = re.findall(r'\b[a-zA-Z]+\b',sentence.lower())
    count_word = Counter(words)
    top_5_words = count_word.most_common(5)

    print("top 5 letters")
    for letter,count in top_5_letters:
        print(f"{letter}:{count}")
       
    print("\ntop 5 words")
    for word,count in top_5_words:
        print(f"{word}:{count}")



sentence = "This is a simple sentence example. This sentence is simple."

most_letters_words(sentence)