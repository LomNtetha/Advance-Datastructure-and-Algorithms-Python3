
"""
Write a function to find the maximum of each pair of adjacent elements in an array."

Analysis of the Code:
The function max_adjacent_pairs does the following:

Iterates through the array and compares each element with the next one.
Appends the maximum of each pair to the result list.
Returns the list of maximum values for each adjacent pair.
"""
def max_adjacent_pairs(arr):
    result = []
    for i in range(len(arr) - 1):
        max_value = max(arr[i], arr[i + 1])
        result.append(max_value)
    return result

# Example usage:
arr1 = [1, 3, 2, 3, 4, 5]
arr2 = [1, 5,7,8,9,10]
arr3 = [1, 2, 2, 3, 4, 5]

print(max_adjacent_pairs(arr1))
print(max_adjacent_pairs(arr2))  
print(max_adjacent_pairs(arr3) )

"""
Write a function that takes an array of integers and returns a list of the strongest neighbors for each element. 
A 'strongest neighbor' is the maximum value between an element and its adjacent (next) element.
Example:
Input:
arr = [1, 2, 2, 3, 4, 5]

Output Reasoning:

Adjacent comparisons: (1, 2), (2, 2), (2, 3), (3, 4), (4, 5)
Strongest neighbors: [2, 2, 3, 4, 5]
"""
def find_strongest_neighbour(arr):
    # Initialize an empty list to store the results
    strongest_neighbours = []

    # Iterate through the array up to the second last element
    for i in range(len(arr) - 1):
        # Find the maximum of the current element and the next element
        strongest_neighbours.append(max(arr[i], arr[i + 1]))

    return strongest_neighbours

# Example usage:
arr = [1, 2, 2, 3, 4, 5]
print(find_strongest_neighbour(arr))  # Output: [2, 2, 3, 4, 5]


"""
Write a function to count the number of unique elements in a list without using built-in Python functions like set.s
"""
def count_unique_numbers(input_list):
    l1 = []
    count = 0

    for item in input_list:
        if item not in l1:
            count += 1
            l1.append(item)
    
    return count

input_list = [1, 2, 2, 5, 8, 4, 4, 8]

print("Number of unique items are:", count_unique_numbers(input_list))

"""
Write a function to count the number of unique elements in a list using Python's set data structure
"""
def count_unique_numbers_using_set(lists):
    # Convert the list to a set to remove duplicates, then convert back to a list
    unique_list = list(set(lists))
    
    # The number of unique items is simply the length of the unique list
    count = len(unique_list)
    
    return count

lists = [1, 2, 2, 5, 8, 4, 4, 8]

print("Number of unique items are:", count_unique_numbers_using_set(lists))


def unique_product(input_list):
    
    # Remove duplicates by converting the list to a set, then back to a list
    unique_list = list(set(input_list))

    # Initialize product to 1 (since multiplying by 1 has no effect)
    product = 1
    
    # Calculate the product of unique elements
    for num in unique_list:
        product *= num
    print("Duplication removal list product :", product)

# Example input
input_list = [1, 3, 5, 6, 3, 5, 6, 1]

# Call the function
unique_product(input_list)


from collections import Counter

"""
Write a function to find all elements in a list that appear more than a given number of times K

Example Walkthrough:
Input 1:
test_list1 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K1 = 3

Step-by-Step Process:

Count frequencies: {4: 4, 6: 1, 3: 4, 8: 1}
Extract elements with frequency > 3: [4, 3]
Output:
Here is the frequency [4, 3]

"""
def find_elements_with_frequency_greater_than_k(test_list, K):
    # Count the frequency of each element in the list
    frequency = Counter(test_list)
    
    # Extract elements whose frequency is greater than K
    result = [element for element, count in frequency.items() if count > K]
    
    return result

# Example usage:
test_list1 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K1 = 3
print("Here is the frequency",find_elements_with_frequency_greater_than_k(test_list1, K1))  # Output: [4, 3]

test_list2 = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
K2 = 2
print("Here is the frequency",find_elements_with_frequency_greater_than_k(test_list2, K2))  # Output: [4, 3, 6]


"""
This is to address the frequence question using Counter()

"""


from collections import Counter

def find_elements_with_frequency_greater_than_k(test_list, K):
    # Count the frequency of each element in the list
    frequency = Counter(test_list)
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate through the frequency dictionary
    for element, count in frequency.items():
        if count > K:
            result.append(element)
    
    return result

# Example usage:
test_list1 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K1 = 3
print(find_elements_with_frequency_greater_than_k(test_list1, K1))  # Output: [4, 3]

test_list2 = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
K2 = 2
print(find_elements_with_frequency_greater_than_k(test_list2, K2))  # Output: [4, 3, 6]

"""
Write a function that takes a list and returns all elements after the first three, ignoring the initial three elements.
Example:
Input:
cons = [1, 1, 1, 64, 23, 64, 22, 22, 22]
Output:
[64, 23, 64, 22, 22, 22]
"""
def print_three_consective_numbers(cons):

    count = 0
    new_list = []

    for item in cons:
        count +=1
        if count > 3:
         new_list.append(item)
    return new_list
cons= [1, 1, 1, 64, 23, 64, 22, 22, 22]

print (print_three_consective_numbers(cons))

"""
Write a function that finds and returns elements in a list that appear consecutively at least three times.
Example:
Input:
cons = [1, 1, 1, 64, 23, 64, 22, 22, 22]
Output:
[1, 22]
"""

def print_three_consecutive_numbers(cons):
    new_list = []
    count = 1  # Start count from 1 since we need to compare with the previous item

    for i in range(1, len(cons)):
        if cons[i] == cons[i - 1]:
            count += 1
        else:
            count = 1
        
        # Append item to the new list if it appears consecutively 3 times
        if count == 3:
            new_list.append(cons[i])

    return new_list

cons = [1, 1, 1, 64, 23, 64, 22, 22, 22]
print(print_three_consecutive_numbers(cons))

"""
To use list comprehension to find and return elements that appear consecutively at least three times, 
you can use a combination of list comprehension with a helper function. Here's how you can achieve this:

"""
def find_three_consecutive_numbers(cons):
    # Helper function to determine if an element appears consecutively three times
    def appears_three_times(index):
        return (index > 1 and
                cons[index] == cons[index - 1] and
                cons[index] == cons[index - 2])

    # List comprehension to find elements that appear consecutively three times
    return [cons[i] for i in range(2, len(cons)) if appears_three_times(i)]

cons = [1, 1, 1, 64, 23, 64, 22, 22, 22]
print(find_three_consecutive_numbers(cons))


def find_three_consecutive_numbers(cons):
    new_list = []
    
    # Iterate over the list and check for three consecutive identical numbers
    for i in range(len(cons) - 2):
        if cons[i] == cons[i + 1] == cons[i + 2]:
            new_list.append(cons[i])
    
    return new_list

cons = [1, 1, 1, 64, 23, 64, 22, 22, 22]
print(find_three_consecutive_numbers(cons))


from itertools import permutations

def find_all_combinations(digits):
    # Generate all permutations of the list
    comb = permutations(digits)

    # Print each permutation
    for c in comb:
        print(" ".join(map(str, c)))

# Example usage:
digits = [1, 2, 3]
find_all_combinations(digits)


def find_all_combinations(test_list):
    result = []
    
    # Generate combinations of different lengths
    for i in range(len(test_list)):
        for j in range(i + 1, len(test_list) + 1):
            result.append(test_list[i:j])

    return result

# Example usage:
test_list = [1, 2, 3]
combinations = find_all_combinations(test_list)

# Print each combination
for comb in combinations:
    print(comb)



from itertools import combinations
# initializing list
test_list = ["GFG", [5, 4], "is",
            ["best", "good", "better", "average"]]
idx=0
temp = combinations(test_list, 2)
for i in list(temp):
    idx = idx+1
    print ("Combination", idx, ": ", i)


"""
Given a list of tuples, write a Python function to filter the tuples based on two conditions:

The tuple must contain the element K at least N times.
Return a list of tuples that satisfy this condition.

"""


def filter_tuples(test_list, K, N):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over each tuple in the list
    for tup in test_list:
        # Count the occurrences of K in the current tuple
        if tup.count(K) >= N:
            # If the count is greater than or equal to N, add the tuple to the result list
            result.append(tup)
    
    return result

# Example inputs
test_list = [(4, 5, 5, 4), (5, 4, 3)]
K = 5
N = 2

# Call the function and print the result
print("Output:", filter_tuples(test_list, K, N))

# Another example
test_list = [(4, 5, 5, 4), (5, 4, 3)]
K = 5
N = 3

# Call the function and print the result
print("Output:", filter_tuples(test_list, K, N))


def filter_tuples(test_list, K, N):
    # Use list comprehension to filter tuples based on the condition
    return [tup for tup in test_list if tup.count(K) >= N]

# Example inputs
test_list = [(4, 5, 5, 4), (5, 4, 3)]
K = 5
N = 2

# Call the function and print the result
print("Output:", filter_tuples(test_list, K, N))

# Another example
test_list = [(4, 5, 5, 4), (5, 4, 3)]
K = 5
N = 3

# Call the function and print the result
print("Output:", filter_tuples(test_list, K, N))
