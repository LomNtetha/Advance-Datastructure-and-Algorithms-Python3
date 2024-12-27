"""
1. Inorder Traversal of a Binary Tree
Problem Statement:
Write a function to perform an inorder traversal (left, root, right) of a binary tree. Given the root of a binary tree,
return an array of node values in the inorder sequence. Assume the tree nodes have the structure:

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
        """
        This method performs an inorder traversal of a binary tree and returns a list of node values
        in the order they are visited.
        
        Parameters:
        root (TreeNode): The root node of the binary tree.
        
        Returns:
        list[int]: A list of node values in inorder traversal order.
        """
        
        # Helper function to perform the recursive DFS traversal
        def dfs(node):
            # Base case: If the current node is None, return an empty list (no node to visit)
            if not node:
                return []
            
            # Recursively traverse the left subtree, visit the current node, and then recursively traverse the right subtree
            # Inorder traversal: Left -> Node -> Right
            return dfs(node.left) + [node.val] + dfs(node.right)

        # Start the traversal from the root node and return the result
        return dfs(root)



# Complexity:
# Time: O(n) - Visits each node once.
# Space: O(h) - Call stack size proportional to tree height (h).
"""
2. Preorder Traversal of a Binary Tree
Problem Statement:
Write a function to perform a preorder traversal (root, left, right) of a binary tree. Given the root of the binary tree,
return the array of values in preorder sequence. Assume the tree nodes have the structure shown above.

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
        """
        This method performs a preorder traversal of a binary tree and returns a list of node values
        in the order they are visited.
        
        Parameters:
        root (TreeNode): The root node of the binary tree.
        
        Returns:
        list[int]: A list of node values in preorder traversal order.
        """
        
        # Helper function to perform the recursive DFS traversal
        def dfs(node):
            # Base case: If the current node is None, return an empty list (no node to visit)
            if not node:
                return []
            
            # Preorder traversal: Visit the current node, then recursively traverse the left and right subtrees
            # Order: Node -> Left -> Right
            return [node.val] + dfs(node.left) + dfs(node.right)

        # Start the traversal from the root node and return the result
        return dfs(root)


# Complexity:
# Time: O(n)
# Space: O(h)"
"""
3. Postorder Traversal of a Binary Tree
Problem Statement:
Write a function to perform a postorder traversal (left, right, root) of a binary tree. Given the root of the binary tree,
return the array of values in postorder sequence. Assume the same tree node structure.

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
        """
        This method performs a postorder traversal of a binary tree and returns a list of node values
        in the order they are visited.
        
        Parameters:
        root (TreeNode): The root node of the binary tree.
        
        Returns:
        list[int]: A list of node values in postorder traversal order.
        """
        
        # Helper function to perform the recursive DFS traversal
        def dfs(node):
            # Base case: If the current node is None, return an empty list (no node to visit)
            if not node:
                return []
            
            # Postorder traversal: Recursively traverse the left subtree, then the right subtree, 
            # and finally visit the current node.
            # Order: Left -> Right -> Node
            return dfs(node.left) + dfs(node.right) + [node.val]

        # Start the traversal from the root node and return the result
        return dfs(root)

# Complexity:
# Time: O(n)
# Space: O(h)

"""
4. Depth-First Search (DFS) Traversal
Problem Statement:
Implement a depth-first search (DFS) traversal for a binary tree. DFS explores as far as possible along each branch before backtracking.
Return the nodes' values in DFS order using an iterative approach.

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
        """
        This method performs a depth-first search (DFS) on a binary tree and returns a list of node values
        in the order they are visited (preorder traversal).
        
        Parameters:
        root (TreeNode): The root node of the binary tree.
        
        Returns:
        list[int]: A list of node values in the order of DFS traversal (preorder).
        """
        
        # Initialize the stack with the root node to start the DFS process
        # The stack will help us to explore nodes in depth-first order.
        stack, result = [root], []

        # Continue DFS traversal as long as there are nodes in the stack
        while stack:
            # Pop a node from the stack (last-in, first-out)
            node = stack.pop()
            
            # If the current node is not None, add it to the result
            if node:
                result.append(node.val)
                
                # Push the right child onto the stack (to visit it later)
                stack.append(node.right)
                
                # Push the left child onto the stack (to visit it first)
                stack.append(node.left)

        # Return the result list containing the values of nodes visited in DFS order
        return result


# Complexity:
# Time: O(n)
# Space: O(h)
"""
5. Breadth-First Search (BFS) Traversal
Problem Statement:
Implement a breadth-first search (BFS) traversal for a binary tree. BFS visits all the nodes at the current depth level before moving to nodes at 
the next depth level. Return the nodes' values in BFS order.

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
        """
        This method performs a breadth-first search (BFS) on a binary tree and returns a list of node values
        in the order they are visited (level-order traversal).
        
        Parameters:
        root (TreeNode): The root node of the binary tree.
        
        Returns:
        list[int]: A list of node values in the order of BFS traversal (level-order).
        """
        
        # Initialize the queue with the root node to start the BFS process
        # The queue will help us explore nodes level by level, starting from the root.
        queue, result = deque([root]), []

        # Continue BFS traversal as long as there are nodes in the queue
        while queue:
            # Pop a node from the front of the queue (first-in, first-out)
            node = queue.popleft()
            
            # If the current node is not None, process it by appending its value to the result list
            if node:
                result.append(node.val)
                
                # Add the left child of the current node to the queue (to be visited next)
                queue.append(node.left)
                
                # Add the right child of the current node to the queue (to be visited after the left)
                queue.append(node.right)

        # Return the result list containing the values of nodes visited in BFS order
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
        """
        This method inserts a new value into a binary search tree (BST) while maintaining its properties.
        
        Parameters:
        root (TreeNode): The root of the binary search tree.
        val (int): The value to be inserted into the tree.
        
        Returns:
        TreeNode: The root of the modified binary search tree after insertion.
        """
        
        # Base case: If the root is None, we create a new TreeNode with the value to be inserted.
        if not root:
            return TreeNode(val)
        
        # If the value to be inserted is smaller than the current node's value,
        # it should go to the left subtree.
        if val < root.val:
            # Recurse into the left subtree and insert the value there
            root.left = self.insertIntoBST(root.left, val)
        
        # If the value to be inserted is greater than or equal to the current node's value,
        # it should go to the right subtree.
        else:
            # Recurse into the right subtree and insert the value there
            root.right = self.insertIntoBST(root.right, val)
        
        # After inserting the value, return the root (unchanged) to maintain the tree structure.
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
        """
        This method deletes a node with a given key in a binary search tree (BST) while maintaining its properties.
        
        Parameters:
        root (TreeNode): The root of the binary search tree.
        key (int): The value of the node to be deleted.
        
        Returns:
        TreeNode: The root of the modified binary search tree after deletion.
        """
        
        # Base case: If the root is None, return None (node to delete is not found).
        if not root:
            return root
        
        # If the key to delete is smaller than the current node's value,
        # search for the key in the left subtree.
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        # If the key to delete is greater than the current node's value,
        # search for the key in the right subtree.
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        # If the key is equal to the current node's value, we've found the node to delete.
        else:
            # Case 1: The node has no left child, return the right subtree (which may be None).
            if not root.left:
                return root.right
            
            # Case 2: The node has no right child, return the left subtree.
            if not root.right:
                return root.left
            
            # Case 3: The node has both left and right children.
            # Find the minimum value node in the right subtree (the in-order successor).
            minLargerNode = root.right
            while minLargerNode.left:
                minLargerNode = minLargerNode.left
            
            # Replace the current node's value with the in-order successor's value.
            root.val = minLargerNode.val
            
            # Delete the in-order successor node in the right subtree.
            root.right = self.deleteNode(root.right, root.val)
        
        # Return the root after deletion (the tree is modified).
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
        """
        This method checks if a binary tree is a valid binary search tree (BST).
        
        Parameters:
        root (TreeNode): The root of the binary tree.
        low (float): The lower bound for the node value.
        high (float): The upper bound for the node value.
        
        Returns:
        bool: True if the tree is a valid BST, False otherwise.
        """
        
        # Base case: If the node is None, it is considered valid as it's an empty subtree.
        if not root:
            return True
        
        # Check if the current node's value is within the valid range (low < root.val < high).
        if not (low < root.val < high):
            return False
        
        # Recursively check the left subtree, ensuring all values are less than the current node's value.
        # Recursively check the right subtree, ensuring all values are greater than the current node's value.
        return self.isValidBST(root.left, low, root.val) and self.isValidBST(root.right, root.val, high)


# Complexity:
# Time: O(n)
# Space: O(h)
"""
9. Find the Lowest Common Ancestor (LCA) of Two Nodes in a BST
Problem Statement:
Given a binary search tree and two nodes, find their lowest common ancestor (LCA). The LCA of two nodes is the lowest node in the 
tree that has both nodes as descendants.

Example Input:
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
        """
        This method finds the lowest common ancestor (LCA) of two nodes in a Binary Search Tree (BST).
        
        Parameters:
        root (TreeNode): The root node of the BST.
        p (TreeNode): The first node for which we are finding the LCA.
        q (TreeNode): The second node for which we are finding the LCA.
        
        Returns:
        TreeNode: The lowest common ancestor of nodes p and q.
        """
        
        # Traverse the tree starting from the root
        while root:
            # If both p and q are smaller than the root, move to the left subtree
            if p.val < root.val and q.val < root.val:
                root = root.left
            # If both p and q are larger than the root, move to the right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # If p and q are on opposite sides of the root or one of them is the root,
            # this root is the lowest common ancestor (LCA)
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
        """
        This method calculates the maximum depth (or height) of a binary tree.
        The depth of a tree is the length of the longest path from the root node
        to any leaf node.

        Parameters:
        root (TreeNode): The root node of the binary tree.

        Returns:
        int: The maximum depth of the binary tree.
        """

        # Base case: If the root is None (empty tree), the depth is 0.
        if not root:
            return 0
        
        # Recursive case: The depth of the current tree is 1 (for the root) 
        # plus the maximum of the depths of the left and right subtrees.
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Complexity:
# Time: O(n)
# Space: O(h)