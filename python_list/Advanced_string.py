"""1️⃣ Most Frequent Word in Paragraph

Problem:
Given a paragraph as a string, find the words that appears most frequently. Ignore punctuation and case.

Sample Input:

paragraph = "Hello world. Hello everyone. World is beautiful."


Sample Output:

['hello', 'world']

"""

import re
from collections import Counter

def most_frequent_words(paragraph):
    # Normalize and split words
    words = re.findall(r'\b\w+\b', paragraph.lower())
    
    # Count frequencies
    count = Counter(words) # so by default count is dictionary,{ 'hello': 2,'world': 2,'everyone': 1,'is': 1,'beautiful': 1}
    
    # Find the highest frequency
    max_freq = max(count.values()) # dict_values([2, 2, 1, 1, 1])
    
    # Collect words with the highest frequency
    most_common_words = []
    for word, freq in count.items(): # dict_items([ ('hello', 2), ('world', 2),('everyone', 1), ('is', 1), ('beautiful', 1)])
        if freq == max_freq:
            #append the word
            most_common_words.append(word)
    
    # Return the result
    return most_common_words

paragraph = "Hello world. Hello everyone. World is beautiful."

result = most_frequent_words(paragraph)
print(result)  # ['hello', 'world']

"""
Problem: Group Words by Paragraph Index

You are given a list of strings where each string represents a paragraph.

Your task is to:

Identify all words that appear in more than one paragraph.

For each such word, return the list of paragraph indexes where the word appears.

Return the result as a list of lists of paragraph indexes.

📌 Input

A list of strings:

sentences = [
  "hello world the world is beautiful",
    "i am tired today hello world",
]

📌 Output
[[0,1], [0,1]


Each list represents the paragraph indexes where a word appears more than once across different paragraphs.
"""


from collections import defaultdict

def group_words_by_paragraph(sentences):
    # Create a hash map where:
    # key = word, value = set of paragraph indexes where the word appears
    # Using a set ensures that each paragraph index is stored only once
    word_map = defaultdict(set)

    # First loop: iterate over each sentence by its index
    for i, sentence in enumerate(sentences):
        # Split the sentence into words
        for word in sentence.split():
            # Add the paragraph index to the set for this word to prevent duplicates
            word_map[word].add(i)

    # Prepare the final result list
    result = []

    # Second loop: go through all sets of paragraph indexes
    for indexes in word_map.values():
        # Include only words that appear in more than one paragraph
        if len(indexes) > 1:
            # Convert the set to a list and append to the result
            result.append(list(indexes))

    # Return the list of index groups
    return result
sentences = [
    "hello world the world is beautiful",
    "i am tired today hello world",
]

print(group_words_by_paragraph(sentences))

from collections import defaultdict

def group_words_by_paragraph(sentences):
    # key = word
    # value = set of paragraph indexes
    word_map = defaultdict(set)

    # Loop through sentences with index
    for i, sentence in enumerate(sentences):
        # Split sentence into words
        words = sentence.split()

        for word in words:
            # Add paragraph index to the word's set
            word_map[word].add(i)

    result = []

    # Collect indexes that appear in more than one paragraph
    for indexes in word_map.values():
        if len(indexes) > 1:
            result.append(list(indexes))

    return result


sentences = [
    "hello world the world is beautiful",
    "i am tired today hello world",
]

print(group_words_by_paragraph(sentences))




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
    # Convert text to lowercase and extract words using regex
    # \b\w+\b matches word boundaries with one or more word characters
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the frequency of each word
    count = Counter(words)
    
    # Get words sorted by frequency in descending order
    most_common_words = []
    for word, _ in count.most_common():
        most_common_words.append(word)
    
    # Return the sorted list of words
    return most_common_words

# Example usage
text = "apple banana apple apple orange banana"
print(word_frequency_sort(text))  # ['apple', 'banana', 'orange']

import re
from collections import Counter

def word_frequency_sort(text: str):
    # 1. Convert text to lowercase and extract words
    # \b\w+\b matches word boundaries with one or more letters/digits/underscore
    words = re.findall(r'\b\w+\b', text.lower())
    
    # 2. Count the frequency of each word
    count = Counter(words)
    
    # 3. Collect words sorted by frequency
    most_common_words = []
    for word, frequency in count.most_common():  # Instead of using _, we name it 'frequency'
        most_common_words.append(word)
    
    # 4. Return the final list
    return most_common_words

# Example usage
text = "apple banana apple apple orange banana"
result = word_frequency_sort(text)
print(result)  # ['apple', 'banana', 'orange']

def word_frequency_with_count(text: str):
    # 1. Convert text to lowercase and extract words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # 2. Count the frequency of each word
    count = Counter(words)
    
    # 3. Collect words along with their frequencies
    # The list will contain tuples: (word, frequency)
    result = []
    for word, frequency in count.most_common():  # sorted by frequency descending
        result.append((word, frequency))
    
    # 4. Return the list of tuples
    return result

# Example usage
text = "apple banana apple apple orange banana"
result = word_frequency_with_count(text)
print(result) #[('apple', 3), ('banana', 2), ('orange', 1)]


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
    # 1. Create a set of letters in the sentence
    # - Convert each character to lowercase
    # - Only include alphabetic characters (ignore digits, spaces, punctuation)
    letters = set(c.lower() for c in sentence if c.isalpha())
    
    # 2. Check if the number of unique letters is 26 (all letters of the English alphabet)
    return len(letters) == 26

# Example usage
sentence = "The quick brown fox jumps over a lazy dog"
print(is_pangram(sentence))  # True

def is_pangram(sentence: str) -> bool:
    # 1. Initialize an empty set to store unique letters
    letters = set()
    
    # 2. Loop through each character in the sentence
    for c in sentence:
        # 3. Consider only alphabetic characters
        if c.isalpha():
            # 4. Convert character to lowercase and add to the set
            letters.add(c.lower())
    
    # 5. Check if we have all 26 letters of the alphabet
    return len(letters) == 26

# Example usage
sentence = "The quick brown fox jumps over a lazy dog"
print(is_pangram(sentence))  # True


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

from collections import defaultdict

def group_sentences_by_words(sentences):
    # Create a dictionary where each word maps to a set of sentence indexes it appears in
    word_map = defaultdict(set)  # word -> set of sentence indexes

    # Loop over each sentence and its index
    for i, sentence in enumerate(sentences):
        # Split the sentence into words
        words = sentence.split()
        # Add the current sentence index to the set of indexes for each word
        for word in words:
            word_map[word].add(i)

    # Prepare a list to store words that appear in all sentences
    result = []
    # Loop through the word_map to find words appearing in every sentence
    for word, indexes in word_map.items():
        # If the word appears in all sentences, add it to the result
        if len(indexes) == len(sentences):
            result.append(word)

    return result


# Example sentences
sentences = [
    "hello world beautiful day",
    "hello everyone in the world",
    "what a beautiful world hello"
]

# Call the function and print the words appearing in all sentences
print(group_sentences_by_words(sentences)) #['hello', 'world']


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

from typing import List

def common_words(paragraphs: List[str]):
    # 1. Convert each paragraph into a set of words
    # - p.split() splits the paragraph into words by spaces
    # - set(...) removes duplicates within the paragraph
    sets = [set(p.split()) for p in paragraphs]
    
    # 2. Find the intersection of all sets
    # - set.intersection(*sets) returns words that appear in every paragraph
    common = set.intersection(*sets)
    
    # 3. Convert the result back to a list and return
    return list(common)

# Example usage
paragraphs = [
    "hello world beautiful day",
    "hello everyone in the world",
    "what a beautiful world hello"
]

print(common_words(paragraphs))  # ['hello', 'world']


"""
1️⃣ Longest Substring Without Repeating Characters

Problem:
Given a string s, find the length of the longest substring without repeating characters.

Sample Input:

s = "abcabcbb"


Sample Output:

3  # "abc"

"""

def length_of_longest_substring_set(s: str) -> int:
    seen = set()  # Set to store characters in current window
    start = 0     # Start index of current window
    max_len = 0

    for end, char in enumerate(s):
        # If char is already in the set, shrink the window from the left
        while char in seen:
            seen.remove(s[start])
            start += 1
        
        # Add the current character to the set
        seen.add(char)
        
        # Update max length
        max_len = max(max_len, end - start + 1)
    
    return max_len

# Example usage
s = "abcabcbb"
print(length_of_longest_substring_set(s))  # Output: 3


def length_of_longest_substring_set(s: str) -> int:
    seen = set()  # Set to store characters in the current window
    start = 0     # Start index of current window
    max_len = 0

    # Loop over the indices using range
    for end in range(len(s)):
        char = s[end]  # Get the character at index 'end'

        # If char is already in the set, shrink the window from the left
        while char in seen:
            seen.remove(s[start])
            start += 1
        
        # Add the current character to the set
        seen.add(char)
        
        # Update max length
        max_len = max(max_len, end - start + 1)
    
    return max_len

# Example usage
s = "abcabcbb"
print(length_of_longest_substring_set(s))  # Output: 3


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
    # 🔹 Clean the string:
    # - Convert to lowercase
    # - Keep only letters and numbers
    s = ''.join(c.lower() for c in s if c.isalnum())

    n = len(s)
    count = 0

    # There are 2*n - 1 possible centers
    for center in range(2 * n - 1):
        # divide by Floor division //  and it always round down
        left = center // 2  #gives the starting left index for the palindrome
        right = left + center % 2 #starting right index

        # Expand around center
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    return count


# Example usage
s = "A man, a plan, a canal Panama!"
print(count_substrings(s))


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
    n = len(s)  # Length of the input string
    res = ""    # To store the longest palindromic substring found

    # Loop through all possible centers of palindromes
    # There are 2*n - 1 possible centers:
    # - n single-character centers (for odd-length palindromes)
    # - n-1 two-character centers (for even-length palindromes)
    for center in range(2 * n - 1):
        # Compute left pointer for the current center
        left = center // 2
        # Compute right pointer; for even-length palindromes, start at left+1
        right = left + center % 2

        # Expand around the center as long as the substring is a palindrome
        while left >= 0 and right < n and s[left] == s[right]:
            # If the current palindrome is longer than previously found, update result
            if right - left + 1 > len(res):
                res = s[left:right + 1]
            
            # Expand to the next characters
            left -= 1
            right += 1

    # Return the longest palindromic substring
    return res

# Example usage
s = "babad"
print(longest_palindrome(s))  # Output: "bab" or "aba"




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
def groupAnagrams( strs):
        """
        Group anagrams from a list of strings.
        """
        # Dictionary to group words that are anagrams
        anagrams = defaultdict(list)
        
        # Iterate through each string
        for s in strs:
            # Sort the string to create a key and group anagrams together
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s)
        
        # Return the grouped anagrams
        return list(anagrams.values())

# Example input
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(strs))


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
    # 1. If the needle is empty, return 0
    # This follows the convention: empty string is found at index 0
    if not needle:
        return 0

    # 2. Loop through haystack where the needle could start
    # - Stop at len(haystack) - len(needle) + 1 to avoid index out of range
    for i in range(len(haystack) - len(needle) + 1):
        # 3. Check if the substring of haystack matches needle
        # - haystack[i:i+len(needle)] extracts a substring of the same length as needle
        if haystack[i:i+len(needle)] == needle:
            return i  # Found the needle, return its starting index

    # 4. Needle not found in haystack, return -1
    return -1

# Example usage
haystack = "hello"
needle = "ll"
print(str_str(haystack, needle))  # Output: 2

"""
📱 Problem Statement

You are building a messaging app like WhatsApp.

When a user searches for a word inside a chat message, the system should return the starting index of the first time the keyword appears.

If the keyword does not exist in the message, return -1.

If the keyword is empty, return 0.

✅ Sample Input
message = "Hey, are you coming to the party tonight?"
keyword = "party"

✅ Sample Output
27


Because "party" starts at index 27.

❌ Another Example (Not Found)
message = "Hey, are you coming to the party tonight?"
keyword = "meeting"


Output:

-1


Because "meeting" does not exist in the message.
"""


def search_keyword(message: str, keyword: str) -> int:
    # 1️⃣ If keyword is empty, return 0
    if not keyword:
        return 0

    # 2️⃣ Loop through possible starting positions
    for i in range(len(message) - len(keyword) + 1):

        # 3️⃣ Compare substring with keyword
        if message[i:i + len(keyword)] == keyword:
            return i  # Found it

    # 4️⃣ If not found
    return -1


# Example usage
message = "Hey, are you coming to the party tonight?"
keyword = "party"

print(search_keyword(message, keyword))  # Output: 27


# here is the simple version 
def search_keyword(message: str, keyword: str) -> int:
    """
    Returns the starting index of the first occurrence
    of keyword inside message.
    
    If keyword is not found, returns -1.
    If keyword is empty, returns 0.
    """
    return message.find(keyword)


# Example 1: Found
message = "Hey, are you coming to the party tonight?"
keyword = "party"

result = search_keyword(message, keyword)
print(result)   # Output: 27



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
    # 1️⃣ Start with the first term in the sequence
    result = "1"

    # 2️⃣ We already have term 1, so repeat (n - 1) times
    # to build up to the nth term
    for _ in range(n - 1):

        new_result = ""   # This will store the next term
        count = 1         # Count of repeated digits

        # 3️⃣ Loop through the current result starting from index 1
        for i in range(1, len(result)):

            # 4️⃣ If current digit is same as previous digit,
            # increase the count
            if result[i] == result[i - 1]:
                count += 1
            else:
                # 5️⃣ If digit changes:
                # append count + previous digit
                # Example: "111" → "31"
                new_result += str(count) + result[i - 1]

                # Reset count for new digit
                count = 1

        # 6️⃣ After loop ends, we must add the last group
        # (because the loop stops before adding it)
        new_result += str(count) + result[-1]

        # 7️⃣ Update result for the next iteration
        result = new_result

    # 8️⃣ Return the nth term
    return result


# Example usage
print(count_and_say(4))  # Output: "1211"

def count_and_say(n: int) -> str:
    # 1. Start with the first term in the sequence
    s = "1"

    # 2. Build the sequence up to the nth term
    # - Repeat (n-1) times because we already have the first term
    for _ in range(n - 1):
        next_s = ""  # Will hold the next term in the sequence
        i = 0        # Pointer to iterate over current term 's'

        # 3. Process the current string 's'
        while i < len(s):
            count = 1  # Count occurrences of the same digit

            # 4. Count consecutive identical digits
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1

            # 5. Append count and the digit to next_s
            # Example: "111" → "31" (three 1's)
            next_s += str(count) + s[i]

            # 6. Move to the next new digit
            i += 1

        # 7. Set s to next_s for the next iteration
        s = next_s

    # 8. Return the nth term of the sequence
    return s

# Example usage
n = 5
print(count_and_say(n))  # Output: "111221"

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
    # 1. Count the characters we need from string t
    need = Counter(t)
    
    # 2. Number of characters we are still missing in the current window
    missing = len(t)
    
    # 3. Pointers to define the sliding window
    left = 0       # Left end of the window
    start = 0      # Start index of the minimum window found
    end = 0        # End index of the minimum window found

    # 4. Expand the window by moving 'right' through the string s
    for right, char in enumerate(s):
        # If this character is needed, reduce the missing count
        if need[char] > 0:
            missing -= 1
        
        # Decrement the need for this character
        # (can go negative if the character appears more than needed)
        need[char] -= 1

        # 5. When we have all characters from t in the current window
        while missing == 0:
            # Update the minimum window if it's smaller than previously found
            if end == 0 or right - left + 1 < end - start + 1:
                start, end = left, right

            # Move the left pointer to try and shrink the window
            need[s[left]] += 1  # Add back the character at 'left' to need
            if need[s[left]] > 0:  # If we now miss this character
                missing += 1      # Increment missing count

            left += 1  # Shrink the window from the left

    # 6. Return the minimum window substring, or "" if no valid window found
    return s[start:end + 1] if end >= start else ""

# Example usage
s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))  # Output: "BANC"


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
    # 1. Initialize the maximum word count found so far
    max_words = 0
    
    # 2. Initialize the sentence that has the maximum words
    result = ""

    # 3. Loop through each sentence in the list
    for sentence in sentences:
        # Count the number of words in the current sentence
        # - split() splits by spaces and returns a list of words
        word_count = len(sentence.split())

        # 4. If this sentence has more words than the previous maximum
        if word_count > max_words:
            max_words = word_count  # Update the maximum word count
            result = sentence       # Update the result sentence

    # 5. Return the sentence with the most words
    return result

# Example usage
sentences = [
    "hello world",
    "this is a leetcode style problem",
    "python"
]

print(longestSentence(sentences))  
# Output: "this is a leetcode style problem"



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
    # 1. Initialize the maximum character count found so far
    max_chars = 0
    
    # 2. Initialize the sentence that has the maximum alphabetic characters
    result = ""

    # 3. Loop through each sentence in the list
    for sentence in sentences:
        # Count the number of alphabetic characters in the current sentence
        # - sum(1 for c in sentence if c.isalpha()) counts letters only
        char_count = sum(1 for c in sentence if c.isalpha())

        # 4. If this sentence has more alphabetic characters than the previous maximum
        if char_count > max_chars:
            max_chars = char_count  # Update the maximum character count
            result = sentence       # Update the result sentence

    # 5. Return the sentence with the most alphabetic characters
    return result


# Example usage
sentences = [
    "hello world m l p k p pp pp pp",
    "this is a leetcode style problem",
    "python"
]

print(longestCharacters(sentences))  
# Output: "this is a leetcode style problem"




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



"""
Now, lets look into this through a question. Given a string of braces named bound_by, and a string named tag_name. 
The task is to print a new string such that tag_name is in the middle of bound_by.

Example 1:

Input: 
bound_by = [[]], tag_name = tag
Output:
[[tag]]
Example 2:

Input: 
bound_by = <>, tag_name = body
Output:
<body>
"""
class Solution:
    def createBoundedTag(self, bound_by, tag_name):
        # Find the midpoint to split bound_by
        midpoint = len(bound_by) // 2
        opening = bound_by[:midpoint]  # First half
        closing = bound_by[midpoint:]  # Second half
        
        # Form the result with tag_name in the middle
        return f"{opening}{tag_name}{closing}"

# Example usage:
solution = Solution()

# Test case 1
bound_by = "[[]]"
tag_name = "tag"
print(solution.createBoundedTag(bound_by, tag_name))  # Output: "[[tag]]"

# Test case 2
bound_by = "<>"
tag_name = "body"
print(solution.createBoundedTag(bound_by, tag_name))  # Output: "<body>"

"""
5️⃣ Longest Common Prefix

Question
Find the longest common prefix among an array of strings.

Input

["flower","flow","flight"]


Output

"fl"


Edge cases

["dog","racecar","car"] → ""

[""] → ""

["a"] → "a"

[] → ""
"""

def longestCommonPrefix(strs):
    # If the input list is empty, there is no common prefix
    if not strs:
        return ""

    # Start by assuming the first word is the common prefix
    prefix = strs[0]

    # Compare the prefix with each remaining word
    for word in strs[1:]:
        # While the current word does NOT start with the prefix
        # keep shortening the prefix from the end
        while not word.startswith(prefix):
            prefix = prefix[:-1]

            # If prefix becomes empty, no common prefix exists
            if not prefix:
                return ""

    # After checking all words, return the longest common prefix
    return prefix

strs = ["flower","flow","flight"]

print(longestCommonPrefix(strs))


