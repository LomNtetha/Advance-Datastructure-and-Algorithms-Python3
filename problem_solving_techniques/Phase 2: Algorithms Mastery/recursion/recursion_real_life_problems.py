
# ✅ Notes
# Recursion always requires a base case (when to stop).

# Without a base case, recursion leads to infinite loops and stack overflow errors.

# Recursion often involves breaking a problem into smaller identical subproblems.
"""
1. Climbing Stairs (Recursive Steps)
Problem:
Imagine you are climbing a staircase. You can either climb 1 step or 2 steps at a time. How many distinct ways can you climb to the top 
if the staircase has n steps?
"""
def climb_stairs(n):
    # Base case: 0 or 1 step => only 1 way
    if n <= 1:
        return 1
    # Recursive case: either climb 1 step or 2 steps
    return climb_stairs(n-1) + climb_stairs(n-2)

print(climb_stairs(5))  # Output: 8

# Time Complexity: O(2^n) — because we branch into two recursive calls each time.

# Space Complexity: O(n) — the recursion depth is n (maximum).

"""
2. File System Navigation
Problem:
You're designing a program that needs to search all files in a directory (folder) and its subdirectories. Use recursion to simulate searching files.

"""
def search_files(directory):
    # Simulate: Each directory is a dictionary
    for name, content in directory.items():
        if isinstance(content, dict):
            # It's a folder => recursive call
            search_files(content)
        else:
            # It's a file => print it
            print(f"Found file: {name}")

# Example file system
filesystem = {
    'folder1': {
        'file1.txt': None,
        'file2.txt': None,
        'subfolder': {
            'file3.txt': None
        }
    },
    'file4.txt': None
}

search_files(filesystem)

# Time Complexity: O(N) — where N is total number of files + folders.

# Space Complexity: O(D) — where D is the maximum depth of nested folders (due to recursion stack).

"""
3. Calculate Factorial (with real-world meaning)
Problem:
You need to calculate the number of ways to arrange n people in a line (Factorial n!).
                                                                        
 """                                                                       

def factorial(n):
    # Base case: 0! = 1
    if n == 0:
        return 1
    # Recursive case: n * (n-1)!
    return n * factorial(n-1)

print(factorial(5))  # Output: 120
# Time Complexity: O(n) — one call for each decrement from n to 0.

# Space Complexity: O(n) — recursion depth is n.

"""
4. Sum of Digits of a Credit Card
Problem:
Given a credit card number, recursively find the sum of its digits.
"""

def sum_of_digits(n):
    # Base case: single digit number
    if n < 10:
        return n
    # Recursive case: last digit + sum of remaining digits
    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(12345))  # Output: 15
# Time Complexity: O(d) — where d is the number of digits in n.

# Space Complexity: O(d) — depth equals the number of digits.

"""
5. Robot Paths on a Grid
Problem:
A robot can move either right or down on a grid. How many paths are there from (0,0) to (m,n)?
"""
def robot_paths(m, n):
    # Base case: if either row or column is 0, only 1 path
    if m == 0 or n == 0:
        return 1
    # Recursive case: sum of paths from top and left cells
    return robot_paths(m-1, n) + robot_paths(m, n-1)

print(robot_paths(2, 2))  # Output: 6

# Time Complexity: O(2^(m+n)) — at each cell, two recursive calls.

# Space Complexity: O(m+n) — recursion stack height.

"""
6. Recursive Binary Search
Problem:
Find if a name exists in a sorted guest list using recursive binary search.
"""
def binary_search(arr, target, low, high):
    if low > high:
        return False  # Base case: not found
    mid = (low + high) // 2
    if arr[mid] == target:
        return True
    elif target < arr[mid]:
        # Search in left half
        return binary_search(arr, target, low, mid-1)
    else:
        # Search in right half
        return binary_search(arr, target, mid+1, high)

guests = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(binary_search(guests, "Charlie", 0, len(guests)-1))  # Output: True

# Time Complexity: O(log n) — list size halves each time.

# Space Complexity: O(log n) — due to recursion stack.

"""
7. Palindrome Checker
Problem:
Check if a given string is a palindrome (reads same forward and backward) recursively.
"""
def is_palindrome(s):
    # Base case: Empty string or 1 char string is palindrome
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    # Check middle substring
    return is_palindrome(s[1:-1])

print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False

# Time Complexity: O(n) — n comparisons for n characters.

# Space Complexity: O(n) — because slicing creates new substrings (inefficient).

"""
8. Tower of Hanoi
Problem:
Move n disks from source rod to target rod following the rules of Tower of Hanoi.
"""
def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        # Move one disk directly
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move n-1 disks to auxiliary
    tower_of_hanoi(n-1, source, target, auxiliary)
    # Move the largest disk to target
    print(f"Move disk {n} from {source} to {target}")
    # Move n-1 disks from auxiliary to target
    tower_of_hanoi(n-1, auxiliary, source, target)

tower_of_hanoi(3, 'A', 'B', 'C')

# Time Complexity: O(2^n) — each move doubles with each additional disk.

# Space Complexity: O(n) — depth of recursive calls is n.

"""
9. Recursive String Reversal
Problem:
Reverse a string recursively without using loops.
"""
def reverse_string(s):
    if len(s) == 0:
        return s  # Base case: empty string
    return reverse_string(s[1:]) + s[0]  # Reverse substring then add first character

print(reverse_string("Python"))  # Output: "nohtyP"

# Time Complexity: O(n^2) — because strings are immutable in Python and slicing takes O(n).

# Space Complexity: O(n) — recursion depth is n.
"""
10. Calculate Total Cost with Tax
Problem:
You buy items one by one. Each item's price increases the total cost recursively after adding tax.
"""
def total_cost(prices, tax_rate, index=0):
    if index == len(prices):
        return 0  # Base case: no more items
    # Cost of current item with tax + cost of rest
    current_cost = prices[index] * (1 + tax_rate)
    return current_cost + total_cost(prices, tax_rate, index+1)

prices = [100, 200, 300]  # Prices of items
tax_rate = 0.1  # 10% tax
print(total_cost(prices, tax_rate))  # Output: 660.0

# Time Complexity: O(n) — loop over each item once.

# Space Complexity: O(n) — recursion stack holds n calls.

"""
11. Decode Ways (Message Decoding)
In a secret agent system, a message is encoded where '1' = 'A', '2' = 'B', ..., '26' = 'Z'.
Given a digit string, how many ways can you decode it?

Example: "12" → could be "AB" (1 and 2) or "L" (12) → 2 ways.
"""
def num_decodings(s):
    # Base case: empty string means 1 valid way
    if not s:
        return 1
    # If starts with '0', invalid
    if s[0] == '0':
        return 0
    # Only 1 character left
    if len(s) == 1:
        return 1

    # Decode single character + decode double character if valid
    ways = num_decodings(s[1:])
    if int(s[:2]) <= 26:
        ways += num_decodings(s[2:])
    
    return ways

print(num_decodings("226"))  # Output: 3
# Time Complexity: O(2^n) — two choices at each character (split 1 or 2 digits).

# Space Complexity: O(n) — recursion depth.
"""
12. Word Break (Check Dictionary Words)
Given a string and a dictionary of words, determine if the string can be segmented into a space-separated sequence of one or more dictionary words.

Example:
"applepenapple" with dictionary ["apple", "pen"] → True

"""
def word_break(s, word_dict):
    if not s:
        return True
    
    for word in word_dict:
        # If s starts with a word
        if s.startswith(word):
            # Recursively check the rest
            if word_break(s[len(word):], word_dict):
                return True
    return False

print(word_break("applepenapple", ["apple", "pen"]))  # Output: True

# Time Complexity: O(2^n) — each letter can create multiple splits.

# Space Complexity: O(n) — maximum call stack depth.

"""
13. Unique Binary Search Trees (Number of Structures)
Given n, how many unique binary search trees can you form with values 1..n?

Example:
n = 3 → 5 unique BSTs

"""
def num_trees(n):
    # Base case: 0 or 1 node → 1 structure
    if n <= 1:
        return 1
    total = 0
    # Each number as root
    for i in range(n):
        # Number of left subtrees * number of right subtrees
        left = num_trees(i)
        right = num_trees(n-1-i)
        total += left * right
    return total

print(num_trees(3))  # Output: 5
# Time Complexity: O(2^n) — exponentially growing splits.

# Space Complexity: O(n) — depth of recursion.
"""
14. Minimum Path Sum in a Grid
Given a m x n grid filled with non-negative numbers,
find a path from top-left to bottom-right which minimizes the sum of all numbers along its path.
You can only move right or down.
"""

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])

    def dfs(x, y):
        # Base case: out of bounds
        if x >= m or y >= n:
            return float('inf')
        # Base case: reach end
        if x == m-1 and y == n-1:
            return grid[x][y]
        # Recurse by moving right or down
        return grid[x][y] + min(dfs(x+1, y), dfs(x, y+1))
    
    return dfs(0, 0)

grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]
print(min_path_sum(grid))
# Time Complexity: O(2^(m+n)) — two options at each cell.

# Space Complexity: O(m+n) — recursion depth.








