
"""
1. Fibonacci Sequence
Calculate the n-th Fibonacci number, where each number is the sum of the two preceding ones, starting from 0 and 1.

Example:

Input: n = 5
Output: 5
"""

class Solution:
    def fibonacci(self, n: int) -> int:
        # Base case: if n is 0 or 1, return n as it’s the base case.
        if n <= 1:
            return n
        
        # Recursive case: return the sum of previous two Fibonacci numbers
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

# Complexity:
# Time: O(2^n) - Each function call results in two further calls, leading to exponential growth.
# Space: O(n) - Due to recursion stack usage.
"""
2. Factorial Calculation
Find the factorial of a given integer n, defined as n! = n * (n - 1) * ... * 1.

Example:

Input: n = 4
Output: 24
"""

class Solution:
    def factorial(self, n: int) -> int:
        # Base case: if n is 0 or 1, factorial is 1.
        if n == 0 or n == 1:
            return 1
        
        # Recursive case: multiply n by the factorial of (n - 1).
        return n * self.factorial(n - 1)

# Complexity:
# Time: O(n) - Linear calls to reduce n to the base case.
# Space: O(n) - Recursion stack depth.
"""
3. Power of a Number
Calculate x raised to the power n (x^n).

Example:

Input: x = 2, n = 3
Output: 8

"""
class Solution:
    def power(self, x: float, n: int) -> float:
        # Base case: x^0 is always 1.
        if n == 0:
            return 1
        elif n < 0:
            # For negative powers, use reciprocal of positive power.
            return 1 / self.power(x, -n)
        
        # Recursive case: if n is even, split power; if odd, reduce by one.
        if n % 2 == 0:
            half_power = self.power(x, n // 2)
            return half_power * half_power
        else:
            return x * self.power(x, n - 1)

# Complexity:
# Time: O(log n) - Exponent is halved in each step.
# Space: O(log n) - Recursion stack depth proportional to log n.
"""
4. Sum of Digits
Calculate the sum of digits of a given integer n.

Example:

Input: n = 123
Output: 6

"""
class Solution:
    def sum_of_digits(self, n: int) -> int:
        # Base case: if n is 0, no digits left to add.
        if n == 0:
            return 0
        
        # Recursive case: last digit + sum of remaining digits.
        return n % 10 + self.sum_of_digits(n // 10)

# Complexity:
# Time: O(d) - Where d is the number of digits in n.
# Space: O(d) - Recursion stack depth.
"""
5. Binary Search (Recursive)
Implement binary search to find an element x in a sorted array arr.

Example:

Input: arr = [1, 2, 3, 4, 5], x = 4
Output: 3

"""
class Solution:
    def binary_search(self, arr: list, left: int, right: int, x: int) -> int:
        # Base case: If search space is exhausted, x is not in array.
        if right >= left:
            mid = left + (right - left) // 2
            
            # Check if mid element is the target.
            if arr[mid] == x:
                return mid
            
            # Recursive case: if target is less, search left half.
            elif arr[mid] > x:
                return self.binary_search(arr, left, mid - 1, x)
            
            # Otherwise, search right half.
            else:
                return self.binary_search(arr, mid + 1, right, x)
        
        # If element is not present, return -1.
        return -1

# Complexity:
# Time: O(log n) - The array is halved each step.
# Space: O(log n) - Recursion stack depth.
"""
6. Reverse a String
Reverse a string using recursion.

Example:

Input: s = "hello"
Output: "olleh"


"""
class Solution:
    def reverse_string(self, s: str) -> str:
        # Base case: a string of length 0 or 1 is already reversed.
        if len(s) <= 1:
            return s
        
        # Recursive case: last character + reverse of the rest.
        return s[-1] + self.reverse_string(s[:-1])

# Complexity:
# Time: O(n) - Each character is visited once.
# Space: O(n) - Recursion stack depth.
"""
7. Palindrome Check
Check if a given string is a palindrome.

Example:

Input: s = "racecar"
Output: True

"""

class Solution:
    def is_palindrome(self, s: str) -> bool:
        # Base case: if the string has 0 or 1 character, it’s a palindrome.
        if len(s) <= 1:
            return True
        
        # Recursive case: check first and last character and recurse.
        if s[0] == s[-1]:
            return self.is_palindrome(s[1:-1])
        
        return False

# Complexity:
# Time: O(n) - Half of the string is checked.
# Space: O(n) - Recursion stack depth.
"""
8. Permutations of a String
Generate all permutations of a given string.

Example:

Input: s = "abc"
Output: ["abc", "acb", "bac", "bca", "cab", "cba"]

"""
class Solution:
    def permutations(self, s: str) -> list:
        # Base case: a single character has only one permutation.
        if len(s) <= 1:
            return [s]
        
        # Recursive case: insert first character in all positions of each permutation.
        result = []
        first_char = s[0]
        for perm in self.permutations(s[1:]):
            for i in range(len(perm) + 1):
                result.append(perm[:i] + first_char + perm[i:])
        
        return result

# Complexity:
# Time: O(n!) - Permutations grow factorially with length.
# Space: O(n!) - Result storage and recursion depth.
"""
9. Count Paths in a Grid
Count all possible paths from the top-left to the bottom-right corner of an m x n grid. Only moves to the right or down are allowed.

Example:

Input: m = 2, n = 2
Output: 2

"""
class Solution:
    def count_paths(self, m: int, n: int) -> int:
        # Base case: if at last row or column, only one path is possible.
        if m == 1 or n == 1:
            return 1
        
        # Recursive case: add paths from right and below cells.
        return self.count_paths(m - 1, n) + self.count_paths(m, n - 1)

# Complexity:
# Time: O(2^(m+n)) - Each cell has two possible recursive paths.
# Space: O(m + n) - Recursion depth.
"""
10. Generate Parentheses
Given n pairs of parentheses, generate all valid combinations.

Example:

Input: n = 2
Output: ["(())", "()()"]
"""

class Solution:
    def generate_parentheses(self, n: int) -> list:
        def generate(p: str, left: int, right: int, result: list):
            # Base case: valid combination generated.
            if left == 0 and right == 0:
                result.append(p)
                return
            
            # Recursive case: add '(' if any left remaining.
            if left > 0:
                generate(p + "(", left - 1, right, result)
            
            # Add ')' if more ')' than '(' have been used.
            if right > left:
                generate(p + ")", left, right - 1, result)
        
        result = []
        generate("", n, n, result)
        return result

# Complexity:
# Time: O(4^n / √n) - Catalan number growth rate.
# Space: O(4^n / √n) - Result storage size.

"""
Each question explores a different recursion concept and is aimed at reinforcing an understanding of recursive calls, base cases, and the effects on space and time complexity. Let me know if you'd like more on any particular question or
"""