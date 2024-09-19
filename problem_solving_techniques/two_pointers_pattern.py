"""
1. Sum of Two Elements (Two Sum II - Input Array is Sorted)
Example Question: You are given a sorted array nums of integers and a target value target. Your goal is to find two numbers in the array whose sum equals the target. Return the indices of the two numbers.

Input:

nums = [2, 7, 11, 15]
target = 9
Approach:

Use two pointers: one starting at the beginning (left = 0), and one at the end (right = len(nums) - 1).
Move the pointers inward based on the sum of the elements they point to.
If the sum is less than the target, increment the left pointer to increase the sum. If the sum is more than the target, decrement the right pointer to reduce the sum.
Time Complexity: O(n) – You are traversing the array once.

"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # Assuming 1-indexed result.
            elif current_sum < target:
                left += 1  # Move left pointer to increase sum.
            else:
                right -= 1  # Move right pointer to decrease sum.

# Example
numbers = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(numbers, target))  # Output: [1, 2]


"""
Problem: Reverse a string in-place using the two-pointer approach.

Approach: Use two pointers, swap the characters, and move towards the center.

Time Complexity: O(n) – Half of the array is traversed.

"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Example
s = ["h", "e", "l", "l", "o"]
Solution().reverseString(s)
print(s)  # Output: ["o", "l", "l", "e", "h"]


"""
Problem: Given a sorted array, remove duplicates in-place such that each element appears only once and return the new length.

Approach: Use two pointers – left keeps track of the last unique element, and right scans through the array.

Time Complexity: O(n) – Each element is visited once.

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        left = 0  # Pointer for the position of unique elements
        
        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
        
        return left + 1

# Example
nums = [1, 1, 2]
length = Solution().removeDuplicates(nums)
print(nums[:length])  # Output: [1, 2]

"""
Problem: Determine if a given string is a palindrome considering only alphanumeric characters and ignoring case.

Approach: Use two pointers, one from the start and one from the end, comparing characters while ignoring non-alphanumeric ones.

Time Complexity: O(n) – Single pass through the string.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move left pointer to next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer to previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True

# Example
s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))  # Output: True


"""
Problem: Given an array representing heights of vertical lines, find two lines that together with the x-axis form a container that holds the most water

Approach: Use two pointers – calculate the area between the two lines, and move the pointer with the shorter line to try and find a larger area.

Time Complexity: O(n) – Each pair of pointers is evaluated once.

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the area formed by lines at left and right
            width = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, width * h)
            
            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# Example
height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))  # Output: 49


"""
Merging Two Sorted Arrays
Example Question: Given two sorted arrays nums1 and nums2, merge them into a single sorted array.

Input:

nums1 = [1, 2, 4]
nums2 = [1, 3, 4]
Approach:

Use two pointers: one for each array (i for nums1 and j for nums2).
Compare the elements at i and j, append the smaller one to the result, and move that pointer forward.
Time Complexity: O(m + n) – You are traversing both arrays.

"""

class Solution:
    def merge_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i, j = 0, 0  # Pointers for nums1 and nums2
        result = []

        # Traverse both arrays
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        # Append any remaining elements in nums1
        while i < len(nums1):
            result.append(nums1[i])
            i += 1

        # Append any remaining elements in nums2
        while j < len(nums2):
            result.append(nums2[j])
            j += 1

        return result

# Test the class method
solution = Solution()
nums1 = [1, 2, 4]
nums2 = [1, 3, 4]
print(solution.merge_sorted_arrays(nums1, nums2))

"""
Linked List Cycle Detection (Floyd’s Cycle Detection)
Example Question: Given a linked list, determine if there is a cycle in it. Use constant space.

Input: A linked list.

Approach:

Use two pointers: a slow pointer (slow) that moves one step at a time, and a fast pointer (fast) that moves two steps at a time.
If the fast pointer meets the slow pointer, there is a cycle. If the fast pointer reaches the end (null), there is no cycle.
Time Complexity: O(n) – Each pointer will traverse the list once.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        
        # Traverse the linked list with two pointers
        while fast and fast.next:
            slow = slow.next           # Move slow pointer by 1 step
            fast = fast.next.next      # Move fast pointer by 2 steps
            
            if slow == fast:           # Cycle detected
                return True
        
        return False                   # No cycle

# Example Usage
# Create a linked list with a cycle for testing
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creates a cycle back to node2

solution = Solution()
print(solution.hasCycle(node1))  # Output: True

"""
Partitioning Array (QuickSort Partition)
Example Question: Given an unsorted array, partition it around a pivot such that elements less than the pivot come before all elements greater than the pivot.

Input:

nums = [3, 2, 1, 5, 6, 4]
Pivot = 3
Approach:

Use two pointers: one from the left and one from the right.
Swap elements such that the elements less than the pivot are on the left and greater than the pivot are on the right.
Time Complexity: O(n) – Each element is moved once.

"""

class Solution:
    def partitionArray(self, nums: List[int], pivot: int) -> List[int]:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # Move left pointer until we find an element >= pivot
            while left <= right and nums[left] < pivot:
                left += 1
            # Move right pointer until we find an element < pivot
            while left <= right and nums[right] >= pivot:
                right -= 1
            
            # If pointers haven't crossed, swap the elements
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums

# Example Usage
nums = [3, 2, 1, 5, 6, 4]
pivot = 3
solution = Solution()
print("partitionArray",solution.partitionArray(nums, pivot))

"""
Three Sum Problem
Example Question: Given an array nums, find all unique triplets such that the sum of the three numbers is zero.

Input:

nums = [-1, 0, 1, 2, -1, -4]
Approach:

Sort the array and use a fixed pointer to loop through each number.
For each number, use two pointers to find pairs whose sum with the current number equals zero.
Time Complexity: O(n^2) – Looping through each element with two pointers for every element.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        result = []
        
        # Step 2: Loop through each number as the fixed pointer
        for i in range(len(nums) - 2):
            # Skip duplicate elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two-pointer approach
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate elements for `left` and `right`
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers inward after finding a valid triplet
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1  # Increase left pointer to get a larger sum
                else:
                    right -= 1  # Decrease right pointer to get a smaller sum
        
        return result

# Example Usage
nums = [-1, 0, 1, 2, -1, -4]
solution = Solution()
print(solution.threeSum(nums))

"""
Trapping Rain Water
Example Question: Given n non-negative integers representing the height of bars, compute how much water it can trap after raining.

Input:

height = [0,1,0,2,1,0,1,3,2,1,2,1]
Approach:

Use two pointers: one from the left and one from the right.
Calculate the trapped water by comparing the heights from both sides, and move the pointer with the smaller height inward.
Time Complexity: O(n) – Single pass through the array.
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0
        
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water_trapped += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water_trapped += right_max - height[right]
        
        return water_trapped

# Example Usage
height = [0,1,0,2,1,0,1,3,2,1,2,1]
solution = Solution()
print(solution.trap(height))  # Output: 6


"""
Subarray with Sum Equal to Target
Example Question: Given an array of positive integers, find the subarray that sums up to a given target.

Input:

nums = [1, 2, 3, 4, 5]
target = 9
Approach:

Use two pointers to form a sliding window. Start both pointers at the beginning and move the right pointer to grow the sum until it equals or exceeds the target.
If the sum exceeds the target, move the left pointer to reduce the sum.
Time Complexity: O(n) – Each element is visited once.

"""

class Solution:
    def subarraySum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        current_sum = 0
        
        # Step 2: Loop over nums using right pointer to expand the window
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Step 3: Shrink the window if current_sum exceeds target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
            
            # Step 4: Check if we found the target sum
            if current_sum == target:
                return nums[left:right+1]  # Return the subarray that sums up to target
        
        return []  # Return an empty list if no subarray is found

# Example Usage
nums = [1, 2, 3, 4, 5]
target = 9
solution = Solution()
print(solution.subarraySum(nums, target))  # Output: [2, 3, 4]