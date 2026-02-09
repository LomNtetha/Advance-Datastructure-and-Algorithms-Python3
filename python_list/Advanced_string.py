"""1️⃣ Most Frequent Word in Paragraph

Problem:
Given a paragraph as a string, find the word that appears most frequently. Ignore punctuation and case.

Sample Input:

paragraph = "Hello world. Hello everyone. World is beautiful."


Sample Output:

"hello"

"""

import re
from collections import Counter

def most_frequent_word(paragraph: str) -> str:
    words = re.findall(r'\b\w+\b', paragraph.lower())
    count = Counter(words)
    return count.most_common(1)[0][0]

paragraph = "Hello world. Hello everyone. World is beautiful."
print(most_frequent_word(paragraph))

"""
📌 Problem: Group Sentences by Shared Words

Problem Statement (Detailed):

You are given a list of sentences. Each sentence consists of words separated by spaces. Your task is to group sentences that share at least one word into the same group.

Two sentences are considered similar if they share at least one word.

A sentence can only belong to one group.

Return a list of groups, where each group contains the indices of sentences in the original list.

The order of groups or the order of indices inside a group does not matter.

📥 Input

sentences: A list of strings, each string representing a sentence.

Constraints:

1 <= len(sentences) <= 1000

Each sentence contains at most 1000 words

Words contain only lowercase and uppercase English letters

📤 Output

A list of groups, each group being a list of integers representing sentence indices that are similar.

🧪 Sample Input
sentences = [
    "hello world the world is beautiful",
    "i am tired today hello world",
    "i am tired today",
    "python is fun",
    "i love python"
]

📤 Sample Output
[[0, 1, 2], [3, 4]]

"""

def group_similar_sentences(sentences):
    groups = []
    seen = set()

    for i, sentence in enumerate(sentences):
        if i in seen:
            continue
        
        words_i = set(sentence.split())
        group = [i]

        for j in range(i + 1, len(sentences)):
            if j in seen:
                continue
            words_j = set(sentences[j].split())
            # If they share at least one word
            if words_i & words_j:
                group.append(j)
                seen.add(j)

        seen.add(i)
        groups.append(group)

    return groups


# Example
sentences = [
    "hello world the world is beautiful",
    "i am tired today hello world",
    "i am tired today",
    "python is fun",
    "i love python"
]

print(group_similar_sentences(sentences))


"""
3️⃣ Word Frequency Sort

Problem:
Given a string, return all words sorted by decreasing frequency. Ignore punctuation and case.

Sample Input:

text = "apple banana apple apple orange banana"


Sample Output:

["apple", "banana", "orange"]


"""

import re
from collections import Counter

def word_frequency_sort(text: str):
    words = re.findall(r'\b\w+\b', text.lower())
    count = Counter(words)
    return [word for word, _ in count.most_common()]

text = "apple banana apple apple orange banana"
print(word_frequency_sort(text))

"""
4️⃣ Check If Sentence is a Pangram

Problem:
Given a string, check if it contains all 26 letters of the English alphabet.

Sample Input:

sentence = "The quick brown fox jumps over a lazy dog"


Sample Output:

True
"""

def is_pangram(sentence: str) -> bool:
    letters = set(c.lower() for c in sentence if c.isalpha())
    return len(letters) == 26

sentence = "The quick brown fox jumps over a lazy dog"
print(is_pangram(sentence))

"""
5️⃣ Find Common Words Across Paragraphs

Problem:
Given multiple paragraphs (strings), find all words that appear in every paragraph.

Sample Input:

paragraphs = [
    "hello world beautiful day",
    "hello everyone in the world",
    "what a beautiful world hello"
]


Sample Output:

["hello", "world"]

"""

from typing import List

def common_words(paragraphs: List[str]):
    sets = [set(p.split()) for p in paragraphs]
    common = set.intersection(*sets)
    return list(common)

paragraphs = [
    "hello world beautiful day",
    "hello everyone in the world",
    "what a beautiful world hello"
]
print(common_words(paragraphs))

"""
1️⃣ Longest Substring Without Repeating Characters

Problem:
Given a string s, find the length of the longest substring without repeating characters.

Sample Input:

s = "abcabcbb"


Sample Output:

3  # "abc"

"""


def length_of_longest_substring(s: str) -> int:
    seen = {}
    start = 0
    max_len = 0

    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = i
        max_len = max(max_len, i - start + 1)
    return max_len


"""
2️⃣ Count Palindromic Substrings

Problem:
Given a string, count all palindromic substrings.

Sample Input:

s = "aaa"


Sample Output:

6  # "a", "a", "a", "aa", "aa", "aaa"


"""

def count_substrings(s: str) -> int:
    n = len(s)
    count = 0

    for center in range(2*n - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    return count


"""

4️⃣ Group Anagrams

Problem:
Given a list of strings, group anagrams together.

Sample Input:

strs = ["eat","tea","tan","ate","nat","bat"]


Sample Output:

[['eat','tea','ate'], ['tan','nat'], ['bat']]

"""


from collections import defaultdict
def group_anagrams(strs):
    res = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        res[key].append(s)
    return list(res.values())

"""
5️⃣ Implement strStr() (Substring Search)

Problem:
Return the index of the first occurrence of needle in haystack, or -1.

Sample Input:

haystack = "hello"
needle = "ll"


Sample Output:

2

"""

def str_str(haystack: str, needle: str) -> int:
    if not needle: return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

"""
6️⃣ Count and Say

Problem:
Generate the nth term of the "count and say" sequence.

Sample Input:

n = 4


Sample Output:

"1211"


"""
def count_and_say(n: int) -> str:
    s = "1"
    for _ in range(n-1):
        next_s = ""
        i = 0
        while i < len(s):
            count = 1
            while i+1 < len(s) and s[i] == s[i+1]:
                i += 1
                count += 1
            next_s += str(count) + s[i]
            i += 1
        s = next_s
    return s
"""
7️⃣ Reverse Words in a String

Problem:
Reverse the words in a string, removing extra spaces.

Sample Input:

s = "  hello world  "


Sample Output:

"world hello"

"""

def reverse_words(s: str) -> str:
    return ' '.join(s.strip().split()[::-1])

"""
8️⃣ Longest Palindromic Substring

Problem:
Find the longest palindromic substring in a string.

Sample Input:

s = "babad"


Sample Output:

"bab"  # or "aba"

"""

def longest_palindrome(s: str) -> str:
    n = len(s)
    res = ""
    for center in range(2*n-1):
        left = center // 2
        right = left + center % 2
        while left >=0 and right < n and s[left]==s[right]:
            if right-left+1 > len(res):
                res = s[left:right+1]
            left -=1
            right +=1
    return res

"""
9️⃣ Minimum Window Substring

Problem:
Find the minimum window in s which contains all characters of t.

Sample Input:

s = "ADOBECODEBANC"
t = "ABC"


Sample Output:

"BANC"

"""


from collections import Counter
def min_window(s: str, t: str) -> str:
    need = Counter(t)
    missing = len(t)
    left = start = end = 0

    for right, char in enumerate(s):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1

        while missing == 0:
            if end == 0 or right-left+1 < end-start+1:
                start, end = left, right
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return s[start:end+1] if end >= start else ""

"""🔟 Decode String (Nested Repetition)

Problem:
Given "3[a2[c]]", return "accaccacc".

Sample Input:

s = "3[a2[c]]"


Sample Output:

"accaccacc"
"""



def decode_string(s: str) -> str:
    stack_num = []
    stack_str = []
    num = 0
    res = ""
    for char in s:
        if char.isdigit():
            num = num*10 + int(char)
        elif char == '[':
            stack_num.append(num)
            stack_str.append(res)
            res = ""
            num = 0
        elif char == ']':
            times = stack_num.pop()
            res = stack_str.pop() + res*times
        else:
            res += char
    return res

"""
🧩 Problem Statement

You are given an array of strings sentences, where each string represents a sentence consisting of words separated by a single space.

Return the sentence that contains the maximum number of words.
If there are multiple sentences with the same maximum number of words, return the first one.

✍️ Input

sentences: List[str]

1 ≤ len(sentences) ≤ 10⁴

Each sentence contains only lowercase English letters and spaces

Words are separated by exactly one space

No leading or trailing spaces

📤 Output

Return a str — the sentence with the highest number of words

🔍 Example 1

Input

sentences = [
    "programming is fun",
    "i like python"
]


Output

"programming is fun"


Explanation

"programming is fun" → 3 words

"i like python" → 3 words
Both have the same number of words, so we return the first on

"""

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
    "hello world",
    "this is a leetcode style problem",
    "python"
]


print(longestSentence(sentences))


"""
Problem Statement

You are given a list of sentences.
Each sentence is a string that may contain letters, spaces, and other characters.

Your task is to find and return the sentence that contains the highest number of alphabetic characters.

Only letters (a–z, A–Z) should be counted.

Spaces and non-letter characters should be ignored.

If multiple sentences have the same maximum number of characters, return the first one.

📥 Input

A list of strings sentences.

sentences = [
    "hello world m l p k p pp pp pp",
    "this is a leetcode style problem",
    "python"
]
"""

def longestCharacters(sentences):
    max_chars = 0
    result = ""

    for sentence in sentences:
        char_count = sum(1 for c in sentence if c.isalpha())

        if char_count > max_chars:
            max_chars = char_count
            result = sentence

    return result


sentences = [
    "hello world m l p k p pp pp pp",
    "this is a leetcode style problem",
    "python"
]

print(longestCharacters(sentences))




"""
Problem Statement (Detailed):

You are given a string text which may contain letters, words, punctuation, and spaces. Your task is to:

Find the top 5 most frequent letters (ignore case, count only alphabetic characters).

Find the top 5 most frequent words (ignore case, count words separated by spaces or punctuation).

Return or print the letters and words along with their counts in descending order of frequency.

If there is a tie in frequency, any order is acceptable for those letters or words.

📥 Input

A string containing letters, words, spaces, and punctuation.

text = "This is a simple sentence example. This sentence is simple."

📤 Output
Top 5 Letters:
s:7
i:4
e:4
t:4
h:2

Top 5 Words:
this:2
is:2
simple:2
sentence:2
example:1

💡 Explanation

Letters:

Convert the string to lowercase.

Ignore non-alphabetic characters.

Count the frequency of each letter.

Return the top 5 letters with highest frequency.

Words:

Split the string into words using regex (\b[a-zA-Z]+\b)

This removes punctuation automatically.

Convert words to lowercase.

Count frequency of each word.

Return the top 5 words with highest frequency.

✅ Simple Solution (Python)
"""

from collections import Counter
import re

def top_5_letters_and_words(text):
    # ---------- LETTERS ----------
    # Keep only letters and convert to lowercase
    letters = [char for char in text.lower() if char.isalpha()]
    letter_counts = Counter(letters)
    top_5_letters = letter_counts.most_common(5)

    # ---------- WORDS ----------
    # Extract words using regex and convert to lowercase
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    word_counts = Counter(words)
    top_5_words = word_counts.most_common(5)

    # ---------- OUTPUT ----------
    print("Top 5 Letters:")
    for letter, count in top_5_letters:
        print(f"{letter}:{count}")

    print("\nTop 5 Words:")
    for word, count in top_5_words:
        print(f"{word}:{count}")


# Example Usage
sentence = "This is a simple sentence example. This sentence is simple."
top_5_letters_and_words(sentence)
