
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