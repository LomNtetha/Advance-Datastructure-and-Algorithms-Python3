"""
Explanation:
- The Bubble Sort algorithm works by repeatedly swapping adjacent elements if they are in the wrong order.
- This process continues until the array is fully sorted, with larger elements "bubbling" to the end of the list.
- In the provided code, the list my_array is sorted in ascending order using Bubble Sort.
"""
def bubble_sort_array_in_ascending_order(arr):

    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
bubble_sort_array_in_ascending_order(my_array)

print("sorted arry",my_array )


def bubble_sort(arr):
     n = len(arr)
     for i in range(n-1):
          for j in range(n-i-1):
               if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]

lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]

bubble_sort(lst)

print ("sorted array",lst )



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
