"""
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Input:
nums = [2, 7, 11, 15]
target = 9
Output: [0, 1]

"""
"""
Time Complexity:
O(n) because we traverse the nums array once.
Space Complexity:
O(n) because we store the elements in the hash map.

"""
from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hash map to store the complement and its index
        hash_map = {}
        
        # Iterate through the nums array
        for i, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num
            
            # If the complement exists in the hash map, return the indices
            if complement in hash_map:
                return [hash_map[complement], i]
            
            # Otherwise, add the current number and its index to the hash map
            hash_map[num] = i
            
        # Return an empty list if no solution is found (this case won't happen as per the problem's assumption)
        return []
"""
Given an array of integers, return True if any value appears at least twice, otherwise return False.

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

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Compare the length of the list with the length of the set (which removes duplicates)
        return len(nums) != len(set(nums))
    
"""
Given two strings s and t, return True if t is an anagram of s, and False otherwise.

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
        # Sort both strings and compare them
        return sorted(s) == sorted(t)

"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique.

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

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both arrays to sets and return the intersection
        return list(set(nums1) & set(nums2))

"""
Given an array of strings, group the anagrams together.

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

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to group words that are anagrams
        anagrams = defaultdict(list)
        
        # Iterate through each string
        for s in strs:
            # Sort the string to create a key and group anagrams together
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s)
        
        # Return the grouped anagrams
        return list(anagrams.values())
    
"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals k.

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

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
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
"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

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
        # Convert the list to a set to remove duplicates
        num_set = set(nums)
        longest_streak = 0
        
        # Iterate through each number in the set
        for num in num_set:
            # Only start counting when it's the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Continue incrementing the streak
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update the longest streak found
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak

"""
Given two strings s and t, determine if they are isomorphic.

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
        # Mappings for characters in s to t and vice versa
        mapping_s_t = {}
        mapping_t_s = {}
        
        # Iterate through both strings simultaneously
        for c1, c2 in zip(s, t):
            # If the mappings do not exist, create them
            if c1 not in mapping_s_t and c2 not in mapping_t_s:
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1
            # If there is a mismatch in the mappings, return False
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False
        return True
    
"""
Given a pattern and a string s, find if s follows the same pattern.

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
        for c, word in zip(pattern, words):
            # If the mapping doesn't exist, create it
            if c not in char_to_word and word not in word_to_char:
                char_to_word[c] = word
                word_to_char[word] = c
            # If there is a mismatch, return False
            elif char_to_word.get(c) != word or word_to_char.get(word) != c:
                return False
        
        return True
    
"""
You are given two strings s and t where t is generated by shuffling the string s and adding one more letter at a random position. Find the extra letter added in t.

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
    
"""
Given an array nums of size n, return the majority element (the element that appears more than n / 2 times).

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
    def majorityElement(self, nums: List[int]) -> int:
        # Create a hash map to count occurrences of each number
        counts = {}
        
        # Count each element's frequency
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        # Return the element with more than n // 2 occurrences
        for num, count in counts.items():
            if count > len(nums) // 2:
                return num
            
"""
Given two lists list1 and list2, find the common interest with the least index sum. If there is a tie, return all such common interests.

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
        # Variable to store the minimum index sum
        min_sum = float('inf')
        result = []
        
        # Iterate through list2 and calculate index sum for common restaurants
        for i, restaurant in enumerate(list2):
            if restaurant in index_map:
                index_sum = i + index_map[restaurant]
                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [restaurant]  # Update result with a new restaurant
                elif index_sum == min_sum:
                    result.append(restaurant)  # Append if it's a tie
        
        return result

"""
Given two strings s and p, return all the start indices of p's anagrams in s. You may return the answer in any order.

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
        # Create a hash map for the target string p
        p_count = Counter(p)
        s_count = Counter()
        result = []
        
        # Iterate through the string s with a sliding window
        for i in range(len(s)):
            # Add the current character to the window
            s_count[s[i]] += 1
            
            # When the window size exceeds the size of p, remove the leftmost character
            if i >= len(p):
                if s_count[s[i - len(p)]] == 1:
                    del s_count[s[i - len(p)]]
                else:
                    s_count[s[i - len(p)]] -= 1
            
            # If the counts match, it means an anagram is found
            if s_count == p_count:
                result.append(i - len(p) + 1)
        
        return result
    
"""
Given an integer array nums and an integer k, return the k most frequent elements.

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
from heapq import nlargest
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element
        count = Counter(nums)
        # Use a heap to extract the top k frequent elements
        return [item for item, freq in count.most_common(k)]



"""
Write an algorithm to determine if a number is "happy." A happy number is a number that eventually reaches 1 when replaced by the sum of the square of its digits. If it loops endlessly in a cycle, return False.

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
        # Create a set to store numbers we've seen to detect cycles
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)  # Mark the number as seen
            n = sum(int(digit) ** 2 for digit in str(n))  # Calculate the sum of squares of digits
        
        return n == 1  # Return True if n reaches 1, False otherwise
