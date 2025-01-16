"""
1. Subsets
Generate all possible subsets of a given set.

Example:

Input: nums = [1, 2, 3]
Output: [[ ], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]


"""
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def backtrack(start: int, current: list[int]):
            # Append the current subset to the result
            result.append(current[:])  # Make a copy of current
            
            # Explore further subsets
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                current.append(nums[i])
                # Recur to generate further subsets
                backtrack(i + 1, current)
                # Backtrack to explore the next subset
                current.pop()  # Remove the last element
        
        backtrack(0, [])
        return result

# Complexity:
# Time: O(2^n) - Each element can be included or excluded.
# Space: O(n) - Space for the recursion stack.
"""
2. Permutations
Generate all possible permutations of a given list.

Example:

Input: nums = [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


"""
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def backtrack(path: list[int], used: list[bool]):
            # If the path is equal to the length of nums, we found a permutation
            if len(path) == len(nums):
                result.append(path[:])  # Make a copy of the path
                return
            
            for i in range(len(nums)):
                if used[i]:  # Skip if the number is already used
                    continue
                # Include nums[i] in the current permutation
                used[i] = True
                path.append(nums[i])
                # Recur with the updated path
                backtrack(path, used)
                # Backtrack: remove the last element and mark it as unused
                path.pop()
                used[i] = False
        
        backtrack([], [False] * len(nums))
        return result

# Complexity:
# Time: O(n!) - There are n! permutations of n elements.
# Space: O(n) - Space for the recursion stack and the path.
"""
3. Combination Sum
Find all unique combinations of numbers that sum to a target.

Example:

Input: candidates = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]


"""
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        
        def backtrack(start: int, current: list[int], remaining: int):
            # Base case: if remaining sum is zero, we found a valid combination
            if remaining == 0:
                result.append(current[:])  # Make a copy of current
                return
            if remaining < 0:  # No valid combination
                return
            
            for i in range(start, len(candidates)):
                # Include candidates[i] in the current combination
                current.append(candidates[i])
                # Recur with the updated remaining sum (i can be reused)
                backtrack(i, current, remaining - candidates[i])
                # Backtrack: remove the last element
                current.pop()
        
        backtrack(0, [], target)
        return result

# Complexity:
# Time: O(2^t) - Where t is the target; in the worst case, we can explore each number multiple times.
# Space: O(t) - Space for the recursion stack.
"""
4. N-Queens
Solve the N-Queens puzzle, placing N queens on an N×N chessboard so that no two queens threaten each other.

Example:

Input: n = 4
Output: [[.Q.., ...Q, Q..., ..Q.], [..Q., Q..., ...Q, .Q..]]


"""
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        board = [["."] * n for _ in range(n)]  # Create an empty board
        
        def is_safe(row: int, col: int) -> bool:
            # Check the column and diagonals
            for i in range(row):
                if board[i][col] == "Q":  # Check column
                    return False
                if col - (row - i) >= 0 and board[i][col - (row - i)] == "Q":  # Check left diagonal
                    return False
                if col + (row - i) < n and board[i][col + (row - i)] == "Q":  # Check right diagonal
                    return False
            return True
        
        def backtrack(row: int):
            # Base case: if all queens are placed
            if row == n:
                result.append(["".join(r) for r in board])  # Convert to required format
                return
            
            for col in range(n):
                if is_safe(row, col):  # Check if it's safe to place queen
                    board[row][col] = "Q"  # Place queen
                    backtrack(row + 1)  # Recur to place the next queen
                    board[row][col] = "."  # Backtrack
        
        backtrack(0)
        return result

# Complexity:
# Time: O(N!) - Each row has N options and there are N rows.
# Space: O(N) - Space used for the recursion stack and the board.
"""
5. Letter Combinations of a Phone Number
Given a string containing digits, return all possible letter combinations that the number could represent.

Example:

Input: digits = "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


"""
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index: int, current: str):
            # Base case: if the current length equals the digits length
            if index == len(digits):
                result.append(current)  # Add the combination to the result
                return
            
            # Get the letters that the current digit can represent
            letters = phone_map[digits[index]]
            for letter in letters:
                # Include the letter in the current combination
                backtrack(index + 1, current + letter)  # Recur for the next digit
        
        backtrack(0, "")
        return result

# Complexity:
# Time: O(4^n) - Each digit can represent up to 4 letters.
# Space: O(n) - Space for the recursion stack.
"""
6. Combination Sum II
Find all unique combinations of numbers that sum to a target, avoiding duplicates.

Example:

Input: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
Output: [[1, 1, 6], [1, 2, 5], [2, 6], [7, 1]]

"""

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()  # Sort to handle duplicates
        
        def backtrack(start: int, current: list[int], remaining: int):
            # Base case: if remaining sum is zero, we found a valid combination
            if remaining == 0:
                result.append(current[:])  # Make a copy of current
                return
            if remaining < 0:  # No valid combination
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Include candidates[i] in the current combination
                current.append(candidates[i])
                # Recur with the updated remaining sum
                backtrack(i + 1, current, remaining - candidates[i])
                # Backtrack: remove the last element
                current.pop()
        
        backtrack(0, [], target)
        return result

# Complexity:
# Time: O(2^n) - Each element can be included or excluded, while avoiding duplicates.
# Space: O(n) - Space for the recursion stack.
"""
7. Word Search
Determine if a word exists in a 2D board of characters.

Example:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: True


"""
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def backtrack(r: int, c: int, index: int) -> bool:
            # Base case: if index reaches the length of word, we found a match
            if index == len(word):
                return True
            
            # Check boundaries and character match
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False
            
            # Mark the cell as visited
            temp = board[r][c]
            board[r][c] = "#"  # Use a special character to mark visited
            
            # Explore all directions
            found = (backtrack(r + 1, c, index + 1) or
                     backtrack(r - 1, c, index + 1) or
                     backtrack(r, c + 1, index + 1) or
                     backtrack(r, c - 1, index + 1))
            
            # Backtrack: unmark the cell
            board[r][c] = temp
            
            return found
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):  # Start searching from each cell
                    return True
        
        return False

# Complexity:
# Time: O(m * n * 4^k) - m: rows, n: cols, k: length of the word; exploring 4 directions.
# Space: O(k) - Space for the recursion stack.
"""
8. Palindrome Partitioning
Given a string, partition it such that every substring is a palindrome. Return all possible palindrome partitioning.

Example:

Input: s = "aab"
Output: [['a', 'a', 'b'], ['aa', 'b']]
"""


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]  # Check if the substring is a palindrome
        
        def backtrack(start: int, current: list[str]):
            # Base case: if we've reached the end of the string
            if start == len(s):
                result.append(current[:])  # Make a copy of current
                return
            
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):  # Check if the substring is a palindrome
                    current.append(s[start:end])  # Add to the current partition
                    backtrack(end, current)  # Recur for the next substring
                    current.pop()  # Backtrack: remove the last partition
        
        backtrack(0, [])
        return result

# Complexity:
# Time: O(2^n) - Each character can either be included or excluded in the partitioning.
# Space: O(n) - Space for the recursion stack.
"""
9. Combination Sum III
Find all possible combinations of k numbers that add up to a number n, with the numbers chosen from 1 to 9.

Example:

Input: k = 3, n = 7
Output: [[1, 2, 4]]

"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []
        
        def backtrack(start: int, current: list[int], remaining: int):
            # Base case: if k numbers are chosen and remaining sum is zero
            if len(current) == k and remaining == 0:
                result.append(current[:])  # Make a copy of current
                return
            if len(current) > k or remaining < 0:  # No valid combination
                return
            
            for i in range(start, 10):  # Numbers from 1 to 9
                current.append(i)  # Include number i
                # Recur with the next number
                backtrack(i + 1, current, remaining - i)
                current.pop()  # Backtrack: remove the last element
        
        backtrack(1, [], n)
        return result

# Complexity:
# Time: O(2^n) - Each number can either be included or excluded.
# Space: O(n) - Space for the recursion stack.
"""
10. Sudoku Solver
Write a program to solve a Sudoku puzzle by filling the empty cells.

Example:

Input:


board = [["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
Output: The completed board.

"""
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Solves a Sudoku puzzle by filling in the empty cells with valid digits (1-9).
        
        :param board: A 9x9 grid representing the Sudoku puzzle.
        """
        
        # Helper function to check if placing a number 'num' in (row, col) is valid
        def is_valid(row: int, col: int, num: str) -> bool:
            """
            Checks if placing 'num' at (row, col) is valid by ensuring it's not already
            in the current row, column, or 3x3 subgrid.
            
            :param row: The row index
            :param col: The column index
            :param num: The number to place at (row, col)
            :return: True if valid, False otherwise.
            """
            # Check if the number is already in the row
            for i in range(9):
                if board[row][i] == num:
                    return False
            
            # Check if the number is already in the column
            for i in range(9):
                if board[i][col] == num:
                    return False
            
            # Check if the number is already in the 3x3 subgrid
            for i in range(3):
                for j in range(3):
                    if board[3 * (row // 3) + i][3 * (col // 3) + j] == num:
                        return False
            
            return True
        
        # Backtracking function to try placing numbers in empty cells
        def backtrack():
            """
            Uses backtracking to try filling in the empty cells.
            """
            # Loop through each cell in the 9x9 board
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":  # Find an empty cell
                        # Try numbers from 1 to 9
                        for num in map(str, range(1, 10)):
                            if is_valid(i, j, num):
                                board[i][j] = num  # Place the number
                                
                                # Recur to try filling the next cell
                                if backtrack():
                                    return True
                                
                                # If no valid solution, backtrack by resetting the cell
                                board[i][j] = "."
                        return False  # If no valid number was found for this empty cell
            return True  # If the board is completely filled
        
        # Start the backtracking process
        backtrack()


# Example usage:
sol = Solution()

# Input Sudoku puzzle with empty cells represented as '.'
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

# Solve the Sudoku puzzle
sol.solveSudoku(board)

# Print the solved board
for row in board:
    print(row)


# Complexity:
# Time: O(9^(m*n)) - The maximum depth of the recursion can be up to 81 cells (9x9).
# Space: O(1) - The board size is fixed (9x9).
"""
These questions and solutions cover a range of common backtracking problems that you may encounter in coding interviews.
Each solution includes a detailed explanation, example inputs and outputs, and comments to help you understand the logic.
"""