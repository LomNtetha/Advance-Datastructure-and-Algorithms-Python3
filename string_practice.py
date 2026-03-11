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


def ma_number(arr):

    max_num = min(arr)

    return max_num


arr = [10, 5, 8]

print(ma_number(arr))

def even_odd(numbers):

    even = 0
    odd = 0
    # result = []

    for num in numbers:
        if num % 2 == 0:
            even += 1
            # result.append(even)
        elif num % 2 == 1:
            odd += 1
            # result.append(odd)
    return odd,even
numbers = [1,2,3,4]

print(even_odd(numbers))