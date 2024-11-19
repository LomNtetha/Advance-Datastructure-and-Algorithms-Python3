"""
1. Inorder Traversal of a Binary Tree
Problem Statement:
Write a function to perform an inorder traversal (left, root, right) of a binary tree. Given the root of a binary tree, return an array of node values in the inorder sequence. Assume the tree nodes have the structure:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
Example Input:
root = [1, None, 2, 3]
The tree structure:

    1
     \
      2
     /
    3
Example Output:
[1, 3, 2]
"""
class Solution:
    def inorderTraversal(self, root):
        def dfs(node):
            if not node:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        
        return dfs(root)

# Complexity:
# Time: O(n) - Visits each node once.
# Space: O(h) - Call stack size proportional to tree height (h).
"""
2. Preorder Traversal of a Binary Tree
Problem Statement:
Write a function to perform a preorder traversal (root, left, right) of a binary tree. Given the root of the binary tree, return the array of values in preorder sequence. Assume the tree nodes have the structure shown above.

Example Input:
root = [1, None, 2, 3]
Tree structure:
    1
     \
      2
     /
    3
Example Output:
[1, 2, 3]
"""
class Solution:
    def preorderTraversal(self, root):
        def dfs(node):
            if not node:
                return []
            return [node.val] + dfs(node.left) + dfs(node.right)
        
        return dfs(root)

# Complexity:
# Time: O(n)
# Space: O(h)"
"""
3. Postorder Traversal of a Binary Tree
Problem Statement:
Write a function to perform a postorder traversal (left, right, root) of a binary tree. Given the root of the binary tree, return the array of values in postorder sequence. Assume the same tree node structure.

Example Input:
root = [1, None, 2, 3]
Tree structure:
    1
     \
      2
     /
    3
Example Output:
[3, 2, 1]
"""
class Solution:
    def postorderTraversal(self, root):
        def dfs(node):
            if not node:
                return []
            return dfs(node.left) + dfs(node.right) + [node.val]
        
        return dfs(root)

# Complexity:
# Time: O(n)
# Space: O(h)

"""
4. Depth-First Search (DFS) Traversal
Problem Statement:
Implement a depth-first search (DFS) traversal for a binary tree. DFS explores as far as possible along each branch before backtracking. Return the nodes' values in DFS order using an iterative approach.

Example Input:
root = [1, 2, 3, 4, 5]
Tree structure:
    1
   / \
  2   3
 / \
4   5
Example Output:
[1, 2, 4, 5, 3]

"""
class Solution:
    def depthFirstSearch(self, root):
        stack, result = [root], []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result

# Complexity:
# Time: O(n)
# Space: O(h)
"""
5. Breadth-First Search (BFS) Traversal
Problem Statement:
Implement a breadth-first search (BFS) traversal for a binary tree. BFS visits all the nodes at the current depth level before moving to nodes at the next depth level. Return the nodes' values in BFS order.

Example Input:
root = [1, 2, 3, 4, 5]
Tree structure:
    1
   / \
  2   3
 / \
4   5
Example Output:
[1, 2, 3, 4, 5]

"""
from collections import deque

class Solution:
    def breadthFirstSearch(self, root):
        queue, result = deque([root]), []
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return result

# Complexity:
# Time: O(n)
# Space: O(w) - Maximum width of the tree (number of nodes at the largest level).
"""
6. Insert a Node in a Binary Search Tree (BST)
Problem Statement:
Write a function to insert a given value into a binary search tree (BST). The BST property ensures that for every node:

The left subtree contains only nodes with values less than the node's value.
The right subtree contains only nodes with values greater than the node's value.
Return the root of the updated BST.

Example Input:
root = [4, 2, 7, 1, 3], val = 5
Tree structure before insertion:
    4
   / \
  2   7
 / \
1   3
Example Output:

[4, 2, 7, 1, 3, 5]
Tree structure after insertion:

    4
   / \
  2   7
 / \  /
1   3 5

"""
class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

# Complexity:
# Time: O(h)
# Space: O(h)
"""
7. Delete a Node from a Binary Search Tree
Problem Statement:
Write a function to delete a node with a given key from a binary search tree. Ensure the BST remains valid after deletion. Use the following rules:

If the node has no children, delete it directly.
If the node has one child, replace it with its child.
If the node has two children, replace it with the inorder successor (smallest node in its right subtree).
Example Input:
root = [5, 3, 6, 2, 4, None, 7], key = 3
Tree structure before deletion:
      5
     / \
    3   6
   / \    \
  2   4    7
Example Output:

[5, 4, 6, 2, None, None, 7]
Tree structure after deletion:
      5
     / \
    4   6
   /      \
  2        7
"""
class Solution:
    def deleteNode(self, root, key):
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            minLargerNode = root.right
            while minLargerNode.left:
                minLargerNode = minLargerNode.left
            root.val = minLargerNode.val
            root.right = self.deleteNode(root.right, root.val)
        return root

# Complexity:
# Time: O(h)
# Space: O(h)
"""
8. Check if a Binary Tree is a Valid BST
Problem Statement:
Write a function to check whether a binary tree is a valid binary search tree (BST). A binary tree is a BST if:

All nodes in the left subtree are smaller than the root.
All nodes in the right subtree are larger than the root.
Both left and right subtrees are also BSTs.
Example Input:

plaintext
Copy code
root = [2, 1, 3]
Tree structure:

    2
   / \
  1   3
Example Output:
True
"""
class Solution:
    def isValidBST(self, root, low=float('-inf'), high=float('inf')):
        if not root:
            return True
        if not (low < root.val < high):
            return False
        return self.isValidBST(root.left, low, root.val) and self.isValidBST(root.right, root.val, high)

# Complexity:
# Time: O(n)
# Space: O(h)
"""
9. Find the Lowest Common Ancestor (LCA) of Two Nodes in a BST
Problem Statement:
Given a binary search tree and two nodes, find their lowest common ancestor (LCA). The LCA of two nodes is the lowest node in the tree that has both nodes as descendants.

Example Input:

plaintext
Copy code
root = [6, 2, 8, 0, 4, 7, 9], p = 2, q = 8
Tree structure:
        6
       / \
      2   8
     / \  / \
    0  4 7   9
Example Output:
6
"""
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root

# Complexity:
# Time: O(h)
# Space: O(1)

"""
10. Find the Height of a Binary Tree
Problem Statement:
Write a function to calculate the height of a binary tree. The height of a tree is the number of edges on the longest path from the root to a leaf.

Example Input:
root = [3, 9, 20, None, None, 15, 7]
Tree structure:
        3
       / \
      9   20
         /  \
        15   7
Example Output:
3
"""

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Complexity:
# Time: O(n)
# Space: O(h)