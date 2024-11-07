class Solution:
    def removeDuplicates(self, s):
        result = ""
        seen = set()
        
        for char in s:
            # Add character if it's not in the set
            if char not in seen:
                result += char
                seen.add(char)
                
        return result

# Example usage:
str = "geEksforGEeks"
solution = Solution()
print(solution.removeDuplicates(str))


class Solution:
    def removeDuplicates(self, s):
        results = ""
        results =''.join(dict.fromkeys(s))
        return results

# Example usage:
str = "geEksforGEeks"
results = str
solution = Solution()
print(solution.removeDuplicates(results))  # Output: "geksfor"

class Solution:
    def cat_hat(self, s):
        # Count occurrences of "cat" and "hat" in the string
        cat_count = s.count("cat")
        hat_count = s.count("hat")
        
        # Check if the counts are the same
        return cat_count == hat_count

# Example usage:
solution = Solution()

# Test case 1
str1 = "catinahat"
print(solution.cat_hat(str1))  # Output: True

# Test case 2
str2 = "bazingaa"
print(solution.cat_hat(str2))  # Output: True

class Solution:
    def isAnagram(self, s1, s2):
        # Anagrams must be of the same length
        if (len(s1) == len(s2) and sorted(s1) == sorted(s2)):
            return True
        # Compare sorted versions of both strings
        else:
            return False

# Example usage:
solution = Solution()

# Test cases
print(solution.isAnagram("geeks", "kseeg"))    # Output: True
print(solution.isAnagram("allergy", "allergic")) # Output: False
print(solution.isAnagram("g", "g"))            # Output: True




"""
Now, lets look into this through a question. Given a string of braces named bound_by, and a string named tag_name. The task is to print a new string such that tag_name is in the middle of bound_by.

Example 1:

Input: 
bound_by = [[]], tag_name = tag
Output:
[[tag]]
Example 2:

Input: 
bound_by = <>, tag_name = body
Output:
<body>
"""
class Solution:
    def createBoundedTag(self, bound_by, tag_name):
        # Find the midpoint to split bound_by
        midpoint = len(bound_by) // 2
        opening = bound_by[:midpoint]  # First half
        closing = bound_by[midpoint:]  # Second half
        
        # Form the result with tag_name in the middle
        return f"{opening}{tag_name}{closing}"

# Example usage:
solution = Solution()

# Test case 1
bound_by = "[[]]"
tag_name = "tag"
print(solution.createBoundedTag(bound_by, tag_name))  # Output: "[[tag]]"

# Test case 2
bound_by = "<>"
tag_name = "body"
print(solution.createBoundedTag(bound_by, tag_name))  # Output: "<body>"

class Solution:
    def makeNewString(self, a, b):
        # Determine the shorter and longer strings
        if len(a) < len(b):
            shorter, longer = a, b
        else:
            shorter, longer = b, a
        
        # Form the new string in the required format
        return shorter + longer + shorter

# Example usage:
solution = Solution()

# Test case 1
a = "Hi"
b = "There"
print(solution.makeNewString(a, b))  # Output: "HiThereHi"

# Test case 2
a = "Hello"
b = "Hi"
print(solution.makeNewString(a, b))  # Output: "HiHelloHi"
