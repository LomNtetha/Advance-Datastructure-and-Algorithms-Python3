"""
Explanation:
- The Bubble Sort algorithm works by repeatedly swapping adjacent elements if they are in the wrong order.
- This process continues until the array is fully sorted, with larger elements "bubbling" to the end of the list.
- In the provided code, the list my_array is sorted in ascending order using Bubble Sort.
- This number grows quadratically with the size of the array, which aligns with the time complexity of O(n²).
"""

"""


"""
# Function to sort an array using Bubble Sort in ascending order
def bubble_sort_array_in_ascending_order(arr):
    n = len(arr)  # Get the length of the array
    # Traverse through all elements in the array
    for i in range(n):
        # Traverse the array from 0 to n-i-1
        # The last i elements are already sorted
        for j in range(0, n-i-1):
             if arr[j] > arr[j+1]:  # Swap if the element found is greater than the next element
         
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the elements

# Define the array to be sorted
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# Apply the bubble sort function
bubble_sort_array_in_ascending_order(my_array)

# Print the sorted array
print("Sorted array:", my_array)

def bubble_sort_array_in_descending_order(arr):
    n = len(arr)  # Get the length of the array
    # Traverse through all elements in the array
    for i in range(n):
        # Traverse the array from 0 to n-i-1
        # The last i elements are already sorted
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:  # Swap if the element found is smaller than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the elements

# Define the array to be sorted
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# Apply the descending order bubble sort function
bubble_sort_array_in_descending_order(my_array)

# Print the sorted array
print("Sorted array in descending order:", my_array)

def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Keep track of whether a swap occurs
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the elements
                swapped = True  # Mark that a swap happened
        # If no swaps occurred during this pass, the array is already sorted
        if not swapped:
            break

# Define the array to be sorted
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# Apply the optimized bubble sort function
optimized_bubble_sort(my_array)

# Print the sorted array
print("Sorted array:", my_array)

# Another version of bubble sort function


"""
Selection Sort: Scans the unsorted part of the array to find the smallest (or largest) element and swaps it with the element at the current position.

Bubble Sort: Compares adjacent elements and swaps them if they are in the wrong order. It "bubbles" the largest element to the end in each pass.

"""

def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr  # Return the sorted array

# Define the array
my_array = [64, 34, 25, 5, 22, 11, 90, 12]

# Apply selection sort and capture the result
sorted_array = selection_sort(my_array)

# Print the sorted array
print("Selection Sorted array with return function:", sorted_array)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        # Find the minimum element in the unsorted portion
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Test list
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
selection_sort(lst)
print("Selection Sorted array without return function:", lst)

"""
The insertion sort works by dividing the array into two parts: a sorted and an unsorted section.
It iterates through the unsorted section, picks each element (key), and places it in its correct position in the sorted section 
by shifting larger elements to the right.

"""
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current_value = arr[i]
        j = i - 1

        # Shift elements of arr[0..i-1] that are greater than current_value to one position ahead
        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1

        # Place current_value at the correct position
        arr[j + 1] = current_value

# Test array
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# Apply insertion sort (no return needed)
insertion_sort(my_array)
# Print the sorted array
print("The insertion Sorted array without return statement:", my_array)


"""
The function now returns the sorted array using the return statement.
After calling the function, you can assign the returned sorted array to a variable (sorted_array) and print it.

"""

def insertion_sort(arr):
    n = len(arr)  # Get the length of the array
    
    # Traverse from the second element to the last element of the array
    for i in range(1, n):
        current_value = arr[i]  # The element to be placed at the correct position
        j = i - 1  # The index of the last element in the sorted portion of the array

        # Shift elements of arr[0..i-1] that are greater than current_value to one position ahead
        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]  # Move the larger element one position to the right
            j -= 1  # Move the index back to check the next element

        # Place current_value at the correct position
        arr[j + 1] = current_value

    return arr  # Return the sorted array

# Test array
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# Apply insertion sort and return the sorted array
sorted_array = insertion_sort(my_array)

# Print the sorted array
print("The insertion sorted array with return statement:", sorted_array)

