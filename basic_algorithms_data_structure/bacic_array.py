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


