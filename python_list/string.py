"""
Write a Python class with a method to remove duplicate characters from a given string while preserving the order of their first appearance.
Case sensitivity should be maintained (i.e., uppercase and lowercase characters are treated as distinct).

Method 1
"""
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

"""
Write a Python class with a method to remove duplicate characters from a given string while preserving the order of their first appearance. 
Case sensitivity should be maintained (i.e., uppercase and lowercase characters are treated as distinct).

Method 2
"""

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

"""
Write a Python class with a method that takes a string as input and checks whether the number of occurrences of the word "cat"
is equal to the number of occurrences of the word "hat". Return True if the counts match, otherwise return False.

Key Points:

Use the str.count() method to calculate the occurrences of "cat" and "hat".
Compare the counts and return the result.
"""

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

"""
Write a Python class with a method that determines whether two given strings are anagrams of each other. 
Two strings are considered anagrams if they have the same characters in the same frequency, regardless of the order. 
Return True if the strings are anagrams, otherwise return False.

Key Points:

Anagrams must have the same length.
Use the sorted() function to compare the sorted versions of the strings.
Handle edge cases such as strings of length 1 or empty strings.
"""

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


