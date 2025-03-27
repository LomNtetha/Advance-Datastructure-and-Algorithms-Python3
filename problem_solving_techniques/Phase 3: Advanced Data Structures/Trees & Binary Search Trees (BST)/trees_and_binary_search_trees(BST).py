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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

# Example Input
# Tree structure:
#     1
#      \
#       2
#      /
#     3
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Create an instance of Solution and call the method
solution = Solution()
output = solution.inorderTraversal(root)
print(output)  # Expected Output: [1, 3, 2]




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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

# Example Input 1
# Tree structure:
#     1
#      \
#       2
#      /
#     3
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

# Example Input 2
# Tree structure:
#       4
#      / \
#     2   5
#    / \
#   1   3
root2 = TreeNode(4)
root2.left = TreeNode(2)
root2.right = TreeNode(5)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(3)

# Create an instance of Solution and call the method
solution = Solution()

output1 = solution.preorderTraversal(root1)
print(output1)  # Expected Output: [1, 2, 3]

output2 = solution.preorderTraversal(root2)
print(output2)  # Expected Output: [4, 2, 1, 3, 5]


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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

# Example Input 1
# Tree structure:
#     1
#      \
#       2
#      /
#     3
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

# Example Input 2
# Tree structure:
#       4
#      / \
#     2   5
#    / \
#   1   3
root2 = TreeNode(4)
root2.left = TreeNode(2)
root2.right = TreeNode(5)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(3)

# Create an instance of Solution and call the method
solution = Solution()

output1 = solution.postorderTraversal(root1)
print(output1)  # Expected Output: [3, 2, 1]

output2 = solution.postorderTraversal(root2)
print(output2)  # Expected Output: [1, 3, 2, 5, 4]


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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
        if not root:
            return []
        
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

# Example Input 1
# Tree structure:
#     1
#    / \
#   2   3
#  / \
# 4   5
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

# Example Input 2
# Tree structure:
#        10
#       /  \
#      20   30
#     /  \
#    40   50
root2 = TreeNode(10)
root2.left = TreeNode(20)
root2.right = TreeNode(30)
root2.left.left = TreeNode(40)
root2.left.right = TreeNode(50)

# Create an instance of Solution and call the method
solution = Solution()

output1 = solution.depthFirstSearch(root1)
print(output1)  # Expected Output: [1, 2, 4, 5, 3]

output2 = solution.depthFirstSearch(root2)
print(output2)  # Expected Output: [10, 20, 40, 50, 30]



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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
        if not root:
            return []

        # Initialize the queue with the root node to start the BFS process
        queue, result = deque([root]), []

        # Continue BFS traversal as long as there are nodes in the queue
        while queue:
            # Pop a node from the front of the queue (first-in, first-out)
            node = queue.popleft()
            
            # If the current node is not None, process it by appending its value to the result list
            result.append(node.val)
            
            # Add the left child of the current node to the queue (to be visited next)
            if node.left:
                queue.append(node.left)
                
            # Add the right child of the current node to the queue (to be visited after the left)
            if node.right:
                queue.append(node.right)

        # Return the result list containing the values of nodes visited in BFS order
        return result

# Example Input 1
# Tree structure:
#     1
#    / \
#   2   3
#  / \
# 4   5
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

# Example Input 2
# Tree structure:
#        10
#       /  \
#      20   30
#     /  \
#    40   50
root2 = TreeNode(10)
root2.left = TreeNode(20)
root2.right = TreeNode(30)
root2.left.left = TreeNode(40)
root2.left.right = TreeNode(50)

# Create an instance of Solution and call the method
solution = Solution()

output1 = solution.breadthFirstSearch(root1)
print(output1)  # Expected Output: [1, 2, 3, 4, 5]

output2 = solution.breadthFirstSearch(root2)
print(output2)  # Expected Output: [10, 20, 30, 40, 50]


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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root, val):
        """
        Inserts a new value into a binary search tree (BST) while maintaining its properties.
        
        Parameters:
        root (TreeNode): The root of the binary search tree.
        val (int): The value to be inserted into the tree.
        
        Returns:
        TreeNode: The root of the modified binary search tree after insertion.
        """
        
        # Base case: If the root is None, create a new TreeNode with the value to be inserted.
        if not root:
            return TreeNode(val)
        
        # If the value to be inserted is smaller than the current node's value,
        # insert into the left subtree.
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:  # Otherwise, insert into the right subtree.
            root.right = self.insertIntoBST(root.right, val)
        
        return root

# Helper function to print the BST in level order for verification
from collections import deque

def level_order_traversal(root):
    if not root:
        return []
    
    queue, result = deque([root]), []
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    return result

# Example Input
# Tree structure before insertion:
#     4
#    / \
#   2   7
#  / \
# 1   3
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

# Insert value 5
solution = Solution()
new_root = solution.insertIntoBST(root, 5)

# Expected Output: [4, 2, 7, 1, 3, 5]
print(level_order_traversal(new_root))  # Output should reflect the updated tree structure


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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root, key):
        """
        Deletes a node with a given key in a binary search tree (BST) while maintaining its properties.
        
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
            # Case 1: The node has no left child, return the right subtree.
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
        
        return root

# Helper function to print the BST in level order for verification
from collections import deque

def level_order_traversal(root):
    if not root:
        return []
    
    queue, result = deque([root]), []
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Trim trailing None values for better representation
    while result and result[-1] is None:
        result.pop()
    
    return result

# Example Input:
# Tree structure before deletion:
#      5
#     / \
#    3   6
#   / \    \
#  2   4    7
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

# Delete node with key 3
solution = Solution()
new_root = solution.deleteNode(root, 3)

# Expected Output: [5, 4, 6, 2, None, None, 7]
print(level_order_traversal(new_root))  # Output should reflect the updated tree structure



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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

# Example Input:
# Tree structure:
#     2
#    / \
#   1   3
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

# Check if the tree is a valid BST
solution = Solution()
print(solution.isValidBST(root))  # Expected Output: True



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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

# Example Input:
# Tree structure:
#         6
#        / \
#       2   8
#      / \  / \
#     0   4 7  9
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

p = root.left  # Node with value 2
q = root.right  # Node with value 8

# Find the LCA
solution = Solution()
lca = solution.lowestCommonAncestor(root, p, q)

print(lca.val)  # Expected Output: 6


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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

# Example Input:
# Tree structure:
#         3
#        / \
#       9   20
#          /  \
#         15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Calculate the height (maximum depth) of the binary tree
solution = Solution()
height = solution.maxDepth(root)

print(height)  # Expected Output: 3

# Complexity:
# Time: O(n)
# Space: O(h)