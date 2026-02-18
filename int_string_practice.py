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
        result.append((word,freq))

    return result
text = "apple banana apple apple orange banana"

print(most_freq_words(text))
import re

from collections import Counter
def top_5_words_character(text):

    words = re.findall(r'\b\w+\b',text.lower())
    count = Counter(words)
    top_5_words = count.most_common(5)

    letters = [char for char in text.lower() if char.isalpha()]
    count_char = Counter(letters)
    top_5_char = count_char.most_common(5)

    print("Top 5 words")
    for word,freq in top_5_words:
        print(f"{word}:{freq}")
     
    print("\nTop 5 characters")
    for char,fr in top_5_char:

        print(f"{char}:{fr}")


text = "This is this a simple sentence example. This sentence is simple."

top_5_words_character(text)