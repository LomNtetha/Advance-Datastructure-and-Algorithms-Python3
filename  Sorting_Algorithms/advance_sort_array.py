"""

Quick Sort Algorithm (Ascending Order)
The Quick Sort algorithm works by selecting a pivot element and partitioning the array such that:

Elements smaller than the pivot go to the left.
Elements larger than the pivot go to the right.
Then, it recursively applies the same process to the left and right subarrays.

"""

#without class
def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1        # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i = i + 1  # Increment the index of the smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    # Swap the pivot element with the element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the partition index

def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the partition index
        pi = partition(arr, low, high)

        # Recursively apply quick sort to the left of the partition index
        quick_sort(arr, low, pi - 1)

        # Recursively apply quick sort to the right of the partition index
        quick_sort(arr, pi + 1, high)
        
# Test array
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# Apply quick sort to the array
quick_sort(my_array, 0, len(my_array) - 1)

# Print the sorted array
print("Sorted array (ascending):", my_array)


#Quick sort algorithms with Class
class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    # Partition method to place the pivot element at the correct position
    def partition(self, low, high):
        pivot = self.arr[high]  # Choose the last element as the pivot
        i = low - 1             # Index of smaller element

        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if self.arr[j] <= pivot:
                i += 1  # Increment index of smaller element
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]  # Swap elements

        # Swap the pivot element with the element at i+1
        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1  # Return the partition index

    # Quick Sort method
    def quick_sort(self, low, high):
        if low < high:
            # Partition the array and get the partition index
            pi = self.partition(low, high)

            # Recursively apply quick sort to the left of the partition index
            self.quick_sort(low, pi - 1)

            # Recursively apply quick sort to the right of the partition index
            self.quick_sort(pi + 1, high)

    # Method to initiate the sorting process
    def sort(self):
        self.quick_sort(0, len(self.arr) - 1)

    # Method to print the array
    def print_array(self):
        print("Sorted array (ascending):", self.arr)


# Test the QuickSort class
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
qs = QuickSort(my_array)

# Apply quick sort to the array
qs.sort()

# Print the sorted array
qs.print_array()

