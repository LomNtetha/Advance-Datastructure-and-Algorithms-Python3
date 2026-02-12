
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

    




sentences = [
    "hello world the world is beautiful",
    "i am tired today hello world",
]