"""
To solve this problem, where the goal is to sort the lists within each key of a dictionary, you can use dictionary comprehensio
"""
def sort_dict_values(test_dict):
    # Using dictionary comprehension to sort the list of values for each key
    sorted_dict = {key: sorted(value) for key, value in test_dict.items()}
    return sorted_dict

# Example 1
test_dict1 = {'c': [3], 'b': [12, 10], 'a': [19, 4]}
sorted_dict1 = sort_dict_values(test_dict1)
print("Output:", sorted_dict1)

# Example 2
test_dict2 = {'c': [10, 34, 3]}
sorted_dict2 = sort_dict_values(test_dict2)
print("Output:", sorted_dict2)


def sort_dict_values(test_dict):
    # Initialize an empty dictionary to store sorted results
    sorted_dict = {}
    
    # Iterate over each key-value pair in the original dictionary
    for key, value in test_dict.items():
        # Sort the list of values and store it in the new dictionary
        sorted_dict[key] = sorted(value)
    
    return sorted_dict

# Example 1
test_dict1 = {'c': [3], 'b': [12, 10], 'a': [19, 4]}
sorted_dict1 = sort_dict_values(test_dict1)
print("Output:", sorted_dict1)

# Example 2
test_dict2 = {'c': [10, 34, 3]}
sorted_dict2 = sort_dict_values(test_dict2)
print("Output:", sorted_dict2)