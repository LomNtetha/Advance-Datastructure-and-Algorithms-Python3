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
    

    