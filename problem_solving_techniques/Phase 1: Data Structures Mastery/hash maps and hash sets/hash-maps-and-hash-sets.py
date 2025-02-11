"""
1. Given an array of integers, return True if any value appears at least twice, otherwise return False.

Example:
Input:
nums = [1, 2, 3, 1]
Output: True

"""
"""
Time Complexity:
O(n) because creating a set requires iterating through the list once.
Space Complexity:
O(n) since the set may store up to n elements.

"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check if there are any duplicate numbers in the input list.
        Compare the length of the list with the length of the set (which removes duplicates).
        """
        return len(nums) != len(set(nums))

# Example input
example_input = [1, 2, 3, 4, 5, 1]

# Create an instance of Solution
sol = Solution().containsDuplicate(example_input)

# Call the containsDuplicate function and print the result
print(f"Contains Duplicate: {sol}")

    
"""
2 .Given two strings s and t, return True if t is an anagram of s, and False otherwise.

Example:
Input:
s = "anagram"
t = "nagaram"
Output: True

"""
"""
Time Complexity:
O(n log n) due to sorting both strings.
Space Complexity:
O(n) because we create new sorted versions of the strings.

"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if two strings are anagrams of each other.
        An anagram is a word or phrase formed by rearranging the letters of another.
        Sort both strings and compare them.
        """
        return sorted(s) == sorted(t)

# Example inputs
s = "listen"
t = "silent"

# Create an instance of Solution
sol = Solution().isAnagram(s, t)

# Call the isAnagram function and print the result
print(f"Are '{s}' and '{t}' anagrams? {sol}")


"""
3 .Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique.

Example:
Input:
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
Output: [2]
"""
"""
Time Complexity:
O(n + m) where n is the length of nums1 and m is the length of nums2.
Space Complexity:
O(n + m) due to the space needed for storing the sets.

"""

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Find the intersection of two arrays.
        Convert both arrays to sets and return the intersection as a list.
        """
        return list(set(nums1) & set(nums2))

# Example inputs
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

# Create an instance of Solution
sol = Solution().intersection(nums1, nums2)

# Call the intersection function and print the result
print(f"The intersection of {nums1} and {nums2} is: {sol}")


"""
4. Given an array of strings, group the anagrams together.

Example:
Input:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output:

[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

"""

"""
Time Complexity:
O(n * k log k) where n is the number of strings and k is the maximum length of a string (sorting takes O(k log k)).
Space Complexity:
O(n * k) because we are storing the strings grouped by their sorted versions.

"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams from a list of strings.
        """
        # Dictionary to group words that are anagrams
        anagrams = defaultdict(list)
        
        # Iterate through each string
        for s in strs:
            # Sort the string to create a key and group anagrams together
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s)
        
        # Return the grouped anagrams
        return list(anagrams.values())

# Example input
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Create an instance of Solution
sol = Solution().groupAnagrams(strs)

# Call the groupAnagrams function and print the result
print(f"Grouped anagrams for {strs}: {sol}")

    
"""
5. Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals k.

Example:
Input:
nums = [1, 1, 1]
k = 2
Output: 2

"""
"""
Time Complexity:
O(n) since we traverse the array once.
Space Complexity:
O(n) for the hash map storing cumulative sums.

"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Calculate the number of continuous subarrays whose sum equals k.
        """
        # Initialize count and current sum
        count = 0
        curr_sum = 0
        # Hash map to store cumulative sums and their frequencies
        hash_map = {0: 1}
        
        # Iterate through the array
        for num in nums:
            curr_sum += num  # Update the cumulative sum
            
            # Check if the current sum minus k exists in the hash map
            if curr_sum - k in hash_map:
                count += hash_map[curr_sum - k]
            
            # Add the current sum to the hash map or update its count
            hash_map[curr_sum] = hash_map.get(curr_sum, 0) + 1
            
        return count

# Example input
nums = [1, 1, 1]
k = 2

# Create an instance of Solution
sol = Solution().subarraySum(nums, k)

# Call the subarraySum function and print the result
print(f"Number of subarrays in {nums} that sum to {k}: {sol}")

"""
6. Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Example:
Input:
nums = [100, 4, 200, 1, 3, 2]
Output: 4

"""

"""
Time Complexity:
O(n) since we check each number in the set only once.
Space Complexity:
O(n) for storing the numbers in a set.

"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Find the length of the longest consecutive elements sequence in the array.
        """
        # Convert the list to a set to remove duplicates and allow O(1) lookups
        num_set = set(nums)
        longest_streak = 0
        
        # Iterate through each number in the set
        for num in num_set:
            # Only start counting when it's the beginning of a sequence
            if num - 1 not in num_set:  # Start of a sequence
                current_num = num
                current_streak = 1
                
                # Continue incrementing the streak
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update the longest streak found so far
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak

# Example input
nums = [100, 4, 200, 1, 3, 2]

# Create an instance of Solution
sol = Solution().longestConsecutive(nums)

# Call the longestConsecutive function and print the result
print(f"The length of the longest consecutive sequence in {nums}: {sol}")


"""
7. Given two strings s and t, determine if they are isomorphic.

Example:
Input:
s = "egg"
t = "add"
Output: True
"""
"""
Time Complexity:
O(n) since we traverse both strings once.
Space Complexity:
O(n) for the two dictionaries storing the mappings.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Determine if two strings s and t are isomorphic.
        Two strings are isomorphic if the characters in s can be replaced 
        to get t, preserving the order of characters.
        """
        # Mappings for characters in s to t and vice versa
        mapping_s_t = {}  # Maps characters from s to t
        mapping_t_s = {}  # Maps characters from t to s
        
        # Iterate through both strings simultaneously
        for c1, c2 in zip(s, t):
            # If the mappings do not exist, create them
            if c1 not in mapping_s_t and c2 not in mapping_t_s:
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1
            # If there is a mismatch in the mappings, return False
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False
        # If all characters satisfy the mapping, return True
        return True

# Example input
s = "egg"
t = "add"

# Create an instance of Solution
sol = Solution().isIsomorphic(s, t)

# Call the isIsomorphic function and print the result
print(f"Are the strings '{s}' and '{t}' isomorphic? {sol}")

    
"""
8. Given a pattern and a string s, find if s follows the same pattern.

Example:
Input:
pattern = "abba"
s = "dog cat cat dog"
Output: True
"""
"""
Time Complexity:
O(n) since we process each character and word once.
Space Complexity:
O(n) for the two dictionaries storing the mappings.
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split the string into words
        words = s.split()
        
        # Return False if lengths are different
        if len(pattern) != len(words):
            return False
        
        # Mappings for characters to words and vice versa
        char_to_word = {}
        word_to_char = {}
        
        # Iterate through the pattern and the corresponding words
        for cha, word in zip(pattern, words):
            # If the mapping doesn't exist, create it
            if cha not in char_to_word and word not in word_to_char:
                char_to_word[cha] = word
                word_to_char[word] = cha
            # If there is a mismatch, return False
            elif char_to_word.get(cha) != word or word_to_char.get(word) != cha:
                return False
        
        return True

# Example input
pattern = "abba"
s = "dog cat cat dog"
solution = Solution().wordPattern(pattern, s)
# Print the output
print(solution)  # Output: True

    
"""
9. You are given two strings s and t where t is generated by shuffling the string s and adding one more letter at a random position.
Find the extra letter added in t.

Example:
Input:
s = "abcd"
t = "abcde"
Output: 'e'
"""
"""
Time Complexity:
O(n) where n is the length of s + t.
Space Complexity:
O(1) since we use a constant amount of space for the XOR result.
"""
"""
Given a string s, find the first non-repeating character and return its index. If it does not exist, return -1.

Example:
Input:
s = "loveleetcode"
Output: 2 (the character 'v' is the first unique character)
"""

"""
Time Complexity:
O(n) where n is the length of the string.
Space Complexity:
O(1) because the alphabet contains a fixed number of characters.
"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Initialize a variable to store the XOR of all characters
        result = 0
        
        # XOR all characters in both strings
        for c in s + t:
            result ^= ord(c)  # XOR operation with the ASCII value of each character
        
        # Return the resulting character (the extra character in t)
        return chr(result)

# Example input

s = "abcd"
t = "abcde"
solution = Solution().findTheDifference(s, t)

# Print the output
print(solution)  # Output: "e"

"""
10. Given an array nums of size n, return the majority element (the element that appears more than n / 2 times).

Example:
Input:
nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2
"""

"""
Time Complexity:
O(n) where n is the number of elements in nums.
Space Complexity:
O(n) due to the hash map storing counts of elements.
"""
from typing import List

class Solution:
    def majorityElement(self, nums):
        counts = Counter(nums)
        maximum_majority = max(counts, key=counts.get)
        return maximum_majority

# Example usage:
nums = [2, 2, 1, 1, 1, 2, 2]
solution = Solution()
print(solution.majorityElement(nums))  # Output: 2


            
"""
11. Given two lists list1 and list2, find the common interest with the least index sum. If there is a tie, return all such common interests.

Example:
Input:
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
"""

"""
Time Complexity:
O(n + m) where n is the length of list1 and m is the length of list2.
Space Complexity:
O(n) due to the hash map storing restaurant indices from list1.
"""
from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Create a hash map to store the index of each restaurant in list1
        index_map = {restaurant: i for i, restaurant in enumerate(list1)}
        
        # Variable to store the minimum index sum, initialized to infinity
        min_sum = float('inf')
        
        # List to store the restaurants with the smallest index sum
        result = []
        
        # Iterate through list2 and calculate the index sum for common restaurants
        for i, restaurant in enumerate(list2):
            # Check if the restaurant is present in list1 (using the hash map)
            if restaurant in index_map:
                # Calculate the index sum for the restaurant
                index_sum = i + index_map[restaurant]
                
                # If we found a smaller index sum, update min_sum and result list
                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [restaurant]  # Update result with the new restaurant
                # If we found an index sum equal to the current min_sum, append the restaurant
                elif index_sum == min_sum:
                    result.append(restaurant)  # Append restaurant to the result list
        
        # Return the list of restaurants with the minimum index sum
        return result

# Example input

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]
solution = Solution().findRestaurant(list1, list2)

# Print the output
print(solution)  # Output: ['Shogun']


"""
12. Given two strings s and p, return all the start indices of p's anagrams in s. You may return the answer in any order.

Example:
Input:
s = "cbaebabacd"
p = "abc"
Output: [0, 6]
"""
"""
Time Complexity:
O(n) where n is the length of string s.
Space Complexity:
O(1) since both p_count and s_count are bounded by the alphabet size (fixed size).

"""
from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Create a hash map for the target string p, counting the frequency of characters
        p_count = Counter(p)
        # Create a hash map to track the frequency of characters in the sliding window of s
        s_count = Counter()
        result = []  # To store the starting indices of the anagrams
        
        # Iterate through the string s with a sliding window
        for i in range(len(s)):
            # Add the current character to the sliding window's count
            s_count[s[i]] += 1
            
            # If the window size exceeds the size of p, remove the leftmost character
            if i >= len(p):
                # If the count of the character is 1, remove it from the window count
                if s_count[s[i - len(p)]] == 1:
                    del s_count[s[i - len(p)]]
                else:
                    # Otherwise, decrease the count of that character
                    s_count[s[i - len(p)]] -= 1
            
            # If the character counts match, it means we found an anagram
            if s_count == p_count:
                # Add the starting index of the anagram to the result list
                result.append(i - len(p) + 1)
        
        return result

# Example usage

s = "cbaebabacd"
p = "abc"
solution = Solution().findAnagrams(s, p)

print(solution)  # Output: [0, 6]

    
"""
13. Given an integer array nums and an integer k, return the k most frequent elements.

Example:
Input:
nums = [1, 1, 1, 2, 2, 3]
k = 2
Output: [1, 2]
"""

"""
Time Complexity:
O(n log k) due to using the heap to extract the top k elements.
Space Complexity:
O(n) for the hash map storing the frequency counts.

"""

from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element in nums
        count = Counter(nums)
        
        # Step 2: Use the most_common method of Counter to get the k most frequent elements
        # The most_common(k) method returns a list of tuples where each tuple contains (element, frequency)
        # We extract only the elements (item) from these tuples and return them as a list
        results = [item for item, freq in count.most_common(k)]
        return results
# Example usage

nums = [1,1,1,2,2,3]
k = 2
solution = Solution().topKFrequent(nums, k)
print(solution)  # Output: [1, 2]


"""
16. A string frequency problem involves counting the frequency of characters or words in a given string and performing operations based on that frequency.

Problem:
Write a function characterFrequency(s: str) -> List[Tuple[str, int]] that takes a string s as input and returns a list of tuples representing each character and its frequency, sorted by frequency in descending order. If two characters have the same frequency, they should be sorted alphabetically.

Example Input:
s = "tree"
Expected Output:
[('e', 2), ('r', 1), ('t', 1)]
Explanation:
Character frequencies:
'e' appears 2 times,
'r' appears 1 time,
't' appears 1 time.
Sorting: By frequency in descending order. For characters with the same frequency, sort alphabetically.
"""
from collections import Counter
from typing import List, Tuple

class Solution:
    def characterFrequency(self, s: str) -> List[Tuple[str, int]]:
        """
        Returns the frequency of each character in the string, sorted by
        frequency (descending) and alphabetically for ties.
        """
        # Count frequencies of characters
        freq = Counter(s)
        
        # Sort by frequency (descending) and alphabetically (ascending)
        sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        
        return sorted_freq

# Example usage
s = "tree"
sol = Solution().characterFrequency(s)
print(sol)


"""
14. Write an algorithm to determine if a number is "happy." A happy number is a number that eventually reaches 1 when replaced
by the sum of the square of its digits. If it loops endlessly in a cycle, return False.

Example:
Input:
n = 19
Output: True (Explanation: 19 -> 82 -> 68 -> 100 -> 1)
"""
"""
Time Complexity:
O(log n) due to the number of digits involved in each iteration.
Space Complexity:
O(log n) because we store the numbers we've seen in a set.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        # Step 1: Create a set to store numbers we've seen to detect cycles
        seen = set()
        
        # Step 2: Loop until n becomes 1 (a happy number) or a cycle is detected
        while n != 1 and n not in seen:
            seen.add(n)  # Mark the current number as seen
            
            # Step 3: Calculate the sum of the squares of the digits of n
            n = sum(int(digit) ** 2 for digit in str(n))
        
        # Step 4: If n becomes 1, it means n is a happy number, so return True
        # If a cycle is detected (n repeats), return False
        return n == 1

# Example usage
solution = Solution()

# Test Case 1: Happy number
n1 = 19
print(solution.isHappy(n1))  # Output: True

# Test Case 2: Non-happy number
n2 = 2
print(solution.isHappy(n2))  # Output: False

    

"""
15. Ransom Note Problem:
Write a function canConstruct(ransomNote: str, magazine: str) -> bool that determines if the string ransomNote can be constructed from the characters in the string magazine.

Each character in magazine can only be used once.

Example:
Input:
ransomNote = "aa"
magazine = "aab"
Output:
True
Explanation: The characters 'a' and 'a' in the ransom note can be constructed using the characters 'a' and 'a' in the magazine.
"""

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Determines if ransomNote can be constructed from magazine.
        """
        # Count the frequency of each character in the magazine and ransom note
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        # Check if magazine contains enough of each character
        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False
        return True

# Example usage
ransomNote = "aa"
magazine = "aab"

sol = Solution().canConstruct(ransomNote, magazine)
print(f"Can construct '{ransomNote}' from '{magazine}'? {sol}")

"""
This approach uses the collections.Counter class to count the frequencies of characters and check if the magazine contains enough characters to 
fulfill the ransom note's requirements. It has a time complexity of O(n+m), 
where n and m are the lengths of ransomNote and magazine, respectively.
"""
