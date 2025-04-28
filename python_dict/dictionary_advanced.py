"""Easy Questions (1–5)
Question: Write a Python program to count the frequency of each character in a string using a dictionary.

Comment: The program will loop through the string, and for each character, it will update the dictionary.
"""
def count_characters(s):
    # Initialize an empty dictionary to store character frequencies
    freq = {}  

    # Loop through each character in the string
    for char in s: 

        if char in freq:  # Check if the character is already in the dictionary
            
             # Increment the frequency count for the character
            freq[char] += 1 
        else:
            freq[char] = 1  # If character is not in the dictionary, initialize its count to 1
    return freq

# Example usage
print(count_characters("hello"))

# Time Complexity: O(n) (where n is the length of the string)

# Space Complexity: O(k) (where k is the number of unique characters in the string)


"""
Question: Write a Python function to merge two dictionaries into one.

Comment: We will use the update() method to merge the dictionaries.
"""
def merge_dicts(dict1, dict2):
    dict1.update(dict2)  # Adds keys from dict2 to dict1, updating the values if keys are the same
    return dict1  # Return the updated dictionary

# Example usage
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
print(merge_dicts(dict1, dict2))

# Time Complexity: O(k + m) (where k is the size of the first dictionary, and m is the size of the second)

# Space Complexity: O(k + m)


"""
Question: Write a Python program to check if a given key exists in a dictionary.

Comment: Using the in operator to check for key existence.
"""
def key_exists(d, key):
    return key in d  # Return True if the key exists in the dictionary, else False

# Example usage
my_dict = {'a': 1, 'b': 2}
print(key_exists(my_dict, 'a'))  # True

# Time Complexity: O(1) (average case for dictionary lookup)

# Space Complexity: O(1)


"""
Question: Write a Python program to find the largest value in a dictionary.

Comment: We can use the max() function with the key parameter to find the largest value.
"""
def largest_value(d):
    return max(d.values())  # Return the largest value in the dictionary

# Example usage
my_dict = {'a': 10, 'b': 20, 'c': 15}
print(largest_value(my_dict))  # 20

# Time Complexity: O(n) (where n is the number of keys in the dictionary)

# Space Complexity: O(1)


"""
Question: Write a Python program to remove a key from a dictionary.

Comment: The del statement can be used to remove the key.
"""
def remove_key(d, key):
    if key in d:  # Check if the key exists in the dictionary
        del d[key]  # If the key exists, remove it
    return d  # Return the updated dictionary

# Example usage
my_dict = {'a': 1, 'b': 2}
print(remove_key(my_dict, 'a'))

# Time Complexity: O(1) (average case for dictionary deletion)

# Space Complexity: O(1)


"""Medium Questions (6–10)
Question: Write a Python program to invert a dictionary (swap keys and values).

Comment: We will use dictionary comprehension to swap the keys and values.
"""
def invert_dict(d):
    return {v: k for k, v in d.items()}  # Swap keys and values using dictionary comprehension

# Example usage
my_dict = {'a': 1, 'b': 2}
print(invert_dict(my_dict))  # {1: 'a', 2: 'b'}

# Time Complexity: O(n) (where n is the number of key-value pairs)

# Space Complexity: O(n)


""""
Question: Write a Python program to merge multiple dictionaries into a single dictionary.

Comment: Use dictionary unpacking (**) to merge multiple dictionaries.
"""
def merge_multiple_dicts(*dicts):
    result = {}  # Initialize an empty dictionary to hold the merged result
    for d in dicts:  # Loop through each dictionary
        result.update(d)  # Merge the current dictionary into result
    return result  # Return the merged dictionary

# Example usage
dict1 = {'a': 1}
dict2 = {'b': 2}
dict3 = {'c': 3}
print(merge_multiple_dicts(dict1, dict2, dict3))

# Time Complexity: O(k1 + k2 + ... + kn) (where k1, k2, ..., kn are the sizes of the dictionaries)

# Space Complexity: O(k1 + k2 + ... + kn)


"""
Question: Write a Python program to remove all occurrences of a specific value from a dictionary.

Comment: We will iterate through the dictionary and remove entries with the specific value.
"""
def remove_value(d, value):
    return {k: v for k, v in d.items() if v != value}  # Remove entries with the specified value using dictionary comprehension

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 1}
print(remove_value(my_dict, 1))  # {'b': 2}

# Time Complexity: O(n) (where n is the number of keys in the dictionary)

# Space Complexity: O(1)


"""
Question: Write a Python program to count how many times each value appears in a dictionary.

Comment: We will use another dictionary to count occurrences.
"""
def count_values(d):
    value_count = {}  # Initialize an empty dictionary to store value frequencies
    for value in d.values():  # Loop through the values in the dictionary
        value_count[value] = value_count.get(value, 0) + 1  # Increment the count for the value
    return value_count  # Return the dictionary containing the count of each value

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 1}
print(count_values(my_dict))  # {1: 2, 2: 1}

# Time Complexity: O(n) (where n is the number of keys in the dictionary)

# Space Complexity: O(k) (where k is the number of unique values)


"""
Question: Write a Python program to get the common keys between two dictionaries.

Comment: Using set operations to find the common keys.
"""
def common_keys(dict1, dict2):
    return set(dict1.keys()) & set(dict2.keys())  # Use set intersection to find common keys

# Example usage
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(common_keys(dict1, dict2))  # {'b'}

# Time Complexity: O(min(k1, k2)) (where k1 and k2 are the number of keys in the dictionaries)

# Space Complexity: O(k) (where k is the number of common keys)


"""Hard Questions (11–15)
Question: Write a Python program to find the intersection of two dictionaries based on their values.

Comment: We will compare values and return keys where values match.
"""
def intersection_by_value(dict1, dict2):
    return {k: v for k, v in dict1.items() if v in dict2.values()}  # Compare values and return matching key-value pairs

# Example usage
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'x': 3, 'y': 2}
print(intersection_by_value(dict1, dict2))  # {'b': 2, 'c': 3}

# Time Complexity: O(n + m) (where n and m are the sizes of the dictionaries)

# Space Complexity: O(min(n, m))


"""
Question: Write a Python program to sort a dictionary by its values.

Comment: We will use the sorted() function and sort the dictionary based on values.
"""
def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))  # Sort dictionary items by their values

# Example usage
my_dict = {'a': 3, 'b': 1, 'c': 2}
print(sort_dict_by_value(my_dict))  # {'b': 1, 'c': 2, 'a': 3}

# Time Complexity: O(n log n) (where n is the number of keys in the dictionary)

# Space Complexity: O(n)


"""
Question: Write a Python program to get the most frequent value in a dictionary.

Comment: We will use the max() function with key parameter to find the most frequent value.
"""
def most_frequent_value(d):
    value_count = {}  # Initialize a dictionary to store value frequencies
    for value in d.values():  # Loop through the values in the dictionary
        value_count[value] = value_count.get(value, 0) + 1  # Count occurrences of each value
    return max(value_count, key=value_count.get)  # Return the value with the highest frequency

# Example usage
my_dict = {'a': 3, 'b': 2, 'c': 3, 'd': 1}
print(most_frequent_value(my_dict))  # 3

# Time Complexity: O(n) (where n is the number of values in the dictionary)

# Space Complexity: O(n)


"""
Question: Write a Python program to convert a dictionary into a list of tuples (key, value) pairs.

Comment: Use the items() method to retrieve key-value pairs.
"""
def dict_to_tuple_list(d):
    return list(d.items())  # Convert dictionary items to a list of tuples

# Example usage
my_dict = {'a': 1, 'b': 2}
print(dict_to_tuple_list(my_dict))  # [('a', 1), ('b', 2)]

# Time Complexity: O(n) (where n is the number of key-value pairs)

# Space Complexity: O(n)


"""
Question: Write a Python program to create a dictionary from two lists, one containing keys and the other containing values.

Comment: We will zip the two lists and convert the result into a dictionary.
"""
def lists_to_dict(keys, values):
    return dict(zip(keys, values))  # Zip the keys and values lists and convert to a dictionary

# Example usage
keys = ['a', 'b', 'c']
values = [1, 2, 3]
print(lists_to_dict(keys, values))  # {'a': 1, 'b': 2, 'c': 3}

# Time Complexity: O(n) (where n is the length of the lists)

# Space Complexity: O(n)
