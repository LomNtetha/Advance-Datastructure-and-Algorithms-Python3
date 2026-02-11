
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