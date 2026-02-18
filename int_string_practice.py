import re
from collections import Counter

def Most_common_words(paragraph):

    words = re.findall(r'\b\w+\b',paragraph.lower())

    count = Counter(words)



    max_freq = max(count.values())

    result = []

    for word,freq in count.items():

        if freq == max_freq:
            result.append(word)

    return result
paragraph = "Hello world. Hello everyone. World is beautiful."

print(Most_common_words(paragraph))


from collections import Counter
import re

def most_freq_words(text):

    result = []

    words = re.findall(r'\b\w+\b', text.lower())

    count = Counter(words)

    most_freq_words= count.most_common()

    for word,freq in most_freq_words:
        result.append(word)

    return result
text = "apple banana apple apple orange banana"

print(most_freq_words(text))