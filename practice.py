def add_two_numbers(nums,target):

    left,right = 0, len(nums)-1

    while left < right:

        total = nums[left] + nums[right]

        if total == target:
            return [left + 1, right + 1]
        
        elif total < target:
            left += 1
        else:
            right -= 1

nums = [2, 7, 11, 15]
target = 9

two_pointer = add_two_numbers(nums,target)

print(two_pointer)

def isPalindrome(s):

    left,right =0,len(s)-1

    while left < right:

        while left < right and not s[left].isalnum():
            left+=1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
        
    return True

s = "A man, a plan, a canal: Panama"

check_palindrome = isPalindrome(s)

print(check_palindrome)

def maxArea(height):

    left,right = 0,len(height) - 1

    max_area = 0

    while left < right:

        width = right -left

        h = min(height[left], height[right])

        max_area = max(max_area, width * h)

        if height[left] < height[right]:
            left += 1

        else:
            right -= 1
        
    return max_area

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]


max = maxArea(height)

print(max)
    

    