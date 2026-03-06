import re
from collections import Counter
def most_freq_words(paragraph):

    words = re.findall(r'\b\w+\b', paragraph.lower())

    count = Counter(words)
    max_freq = max(count.values())

    freq_words = []
    

    for word, freq in count.items():

        if freq == max_freq:
            freq_words.append(word)
    return freq_words

paragraph = "Hello world. Hello everyone. World is beautiful."

print(most_freq_words(paragraph))