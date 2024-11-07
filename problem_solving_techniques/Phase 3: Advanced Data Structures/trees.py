"""
1. Binary Tree Inorder Traversal
Problem Statement:
Given the root of a binary tree, return its inorder traversal.

Example:
Input:
root = [1, null, 2, 3]  # Represents the tree: 1 -> (null, 2 -> (3, null))
Output: [1, 3, 2]

Technique Used: Inorder Traversal (DFS)
Time Complexity: O(n) (Visit each node once)
Space Complexity: O(n) (Space used for recursion stack)
"""
from typing import List
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Value of the node
        self.left = left  # Left child
        self.right = right  # Right child
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def inorder(node):
            if node:
                inorder(node.left)  # Visit left subtree
                res.append(node.val)  # Visit node
                inorder(node.right)  # Visit right subtree
        
        inorder(root)
        return res
"""
2. Binary Tree Preorder Traversal
Problem Statement:
Given the root of a binary tree, return its preorder traversal.

Example:
Input:
root = [1, null, 2, 3]  # Represents the tree: 1 -> (null, 2 -> (3, null))
Output: [1, 2, 3]

Technique Used: Preorder Traversal (DFS)
Time Complexity: O(n)
Space Complexity: O(n)

"""
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def preorder(node):
            if node:
                res.append(node.val)  # Visit node
                preorder(node.left)  # Visit left subtree
                preorder(node.right)  # Visit right subtree
        
        preorder(root)
        return res
"""
3. Binary Tree Postorder Traversal
Problem Statement:
Given the root of a binary tree, return its postorder traversal.

Example:
Input:

root = [1, null, 2, 3]  # Representssolution = Solution() the tree: 1 -> (null, 2 -> (3, null))
Output: [3, 2, 1]

Technique Used: Postorder Traversal (DFS)
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def postorder(node):
            if node:
                postorder(node.left)  # Visit left subtree
                postorder(node.right)  # Visit right subtree
                res.append(node.val)  # Visit node
        
        postorder(root)
        return res
"""
4. Maximum Depth of Binary Tree
Problem Statement:
Given the root of a binary tree, return its maximum depth.

Example:
Input:

root = [3, 9, 20, null, null, 15, 7]
Output: 3

Technique Used: DFS
Time Complexity: O(n)
Space Complexity: O(n) (due to recursion stack)

"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # Return the maximum depth between left and right subtree plus one for the current node
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
"""
5. Validate Binary Search Tree
Problem Statement:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

Example:
Input:

root = [2, 1, 3]
Output: True

Technique Used: DFS with bounds
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            # Check if the node value is within the valid range
            if not (low < node.val < high):
                return False
            # Recursively validate the left and right subtree
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        
        return validate(root)
"""6. Symmetric Tree
Problem Statement:
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example:
Input:


root = [1, 2, 2, 3, 4, 4, 3]
Output: True

Technique Used: DFS
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            # Compare current nodes and recursively check their children
            return (t1.val == t2.val and
                    isMirror(t1.left, t2.right) and
                    isMirror(t1.right, t2.left))
        
        return isMirror(root, root)
"""
7. Binary Tree Level Order Traversal
Problem Statement:
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example:
Input:

root = [3, 9, 20, null, null, 15, 7]
Output: [[3], [9, 20], [15, 7]]

Technique Used: BFS (Breadth-First Search)
Time Complexity: O(n)
Space Complexity: O(n)

"""
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        # Initialize a queue with the root node
        queue = deque([root])
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                # Add left and right children if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res
"""
8. Balanced Binary Tree
Problem Statement:
Given the root of a binary tree, determine if it is height-balanced (i.e., for every node, the left and right subtrees differ in height by no more than 1).

Example:
Input:

root = [3, 9, 20, null, null, 15, 7]
Output: True

Technique Used: DFS
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def checkHeight(node):
            if not node:
                return 0
            left = checkHeight(node.left)
            right = checkHeight(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        
        return checkHeight(root) != -1
"""
9. Lowest Common Ancestor of a Binary Tree
Problem Statement:
Given a binary tree and two nodes, find the lowest common ancestor (LCA) of the two nodes.

Example:
Input:

root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]
p = 5, q = 1
Output: 3

Technique Used: DFS
Time Complexity: O(n)
Space Complexity: O(n)

"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
"""
10. Convert Sorted Array to Binary Search Tree
Problem Statement:
Given an array where elements are sorted in ascending order, convert it into a height-balanced binary search tree.

Example:
Input:

nums = [-10, -3, 0, 5, 9]
Output: [0, -3, 9, -10, null, 5]

Technique Used: Divide and Conquer
Time Complexity: O(n)
Space Complexity: O(log n)

"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node
"""
11. Same Tree
Problem Statement:
Given two binary trees, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example:
Input:

python
Copy code
p = [1, 2, 3]
q = [1, 2, 3]
Output: True

Technique Used: DFS
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
"""
12. Invert Binary Tree
Problem Statement:
Invert a binary tree.

Example:
Input:
root = [4, 2, 7, 1, 3, 6, 9]
Output: [4, 7, 2, 9, 6, 3, 1]

Technique Used: DFS
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
"""
13. Path Sum
Problem Statement:
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

Example:
Input:
root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1]

targetSum = 22
Output: True

Technique Used: DFS
Time Complexity: O(n)
Space Complexity: O(n)

"""
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and targetSum == root.val:
            return True
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))
"""
14. Construct Binary Tree from Preorder and Inorder Traversal
Problem Statement:
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal, construct the binary tree.

Example:
Input:
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
Output: [3, 9, 20, null, null, 15, 7]

Technique Used: Recursion
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder.pop(0))  # The first element in preorder is the root
        inorder_index = inorder.index(root.val)
        root.left = self.buildTree(preorder, inorder[:inorder_index])
        root.right = self.buildTree(preorder, inorder[inorder_index + 1:])
        return root
"""
15. Binary Tree Right Side View
Problem Statement:
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:
Input:
root = [1, 2, 3, null, 5, null, 4]
Output: [1, 3, 4]

Technique Used: BFS
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            rightmost = None
            for i in range(len(queue)):
                node = queue.popleft()
                rightmost = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(rightmost.val)
        return res
"""
16. Kth Smallest Element in a BST
Problem Statement:
Given the root of a binary search tree, and an integer k, return the k-th smallest element in the tree.

Example:
Input:
root = [3, 1, 4, null, 2]
k = 1
Output: 1

Technique Used: Inorder Traversal (DFS)
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        return inorder(root)[k - 1]
