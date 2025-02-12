"""
1. Reverse a Singly Linked List
Problem Statement:
Given the head of a singly linked list, reverse the list and return its head.
You should not use any additional data structures.

Example:

Input: Linked list: 1 -> 2 -> 3 -> 4 -> 5

Output: Reversed linked list: 5 -> 4 -> 3 -> 2 -> 1

"""
class ListNode:
    def __init__(self, val=0, next=None):
        # Initialize the node with a value and a reference to the next node
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Initialize two pointers:
        # 'prev' will hold the reversed part of the list (starting as None)
        prev = None
        # 'current' will traverse through the original list
        current = head
        
        # Traverse the list until all nodes are reversed
        while current:
            # Save the next node to move the 'current' pointer later
            next_node = current.next
            # Reverse the current node's pointer to point to the previous node
            current.next = prev
            # Move 'prev' to the current node (this node is now part of the reversed list)
            prev = current
            # Move to the next node in the original list
            current = next_node
            
        # At the end, 'prev' will be the new head of the reversed list
        return prev

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Create an instance of the Solution class and reverse the linked list
sol = Solution()
reversed_head = sol.reverseList(head)

# 'reversed_head' now points to the head of the reversed list: 5 -> 4 -> 3 -> 2 -> 1

# Output the reversed list
while reversed_head:
    print(reversed_head.val, end=" -> ")
    reversed_head = reversed_head.next
# Output: 5 -> 4 -> 3 -> 2 -> 1
"""
Time Complexity:
O(n), where n is the number of nodes in the linked list. We traverse the list once.

Space Complexity:
O(1). We only use a few extra pointers, so the space complexity is constant.
"""


"""
2. Detect Cycle in a Linked List (Floyd's Tortoise and Hare)
Problem Statement:
Given the head of a linked list, determine if it has a cycle in it.
Use Floyd’s Tortoise and Hare algorithm, which uses two pointers moving at different speeds.

Example:

Input: Linked list: 3 -> 2 -> 0 -> -4
Cycle starts at node with value 2.

Output: True (The list contains a cycle)
"""
class ListNode:
    def __init__(self, val=0, next=None):
        # Initialize a node with a value and a reference to the next node
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Use two pointers, 'slow' and 'fast', both starting at the head of the list
        slow = head
        fast = head
        
        # Traverse the list until 'fast' or 'fast.next' is None
        while fast and fast.next:
            # Move 'slow' one step forward
            slow = slow.next
            # Move 'fast' two steps forward
            fast = fast.next.next
            
            # If 'slow' and 'fast' meet, a cycle exists in the list
            if slow == fast:
                return True
        
        # If we exit the loop, no cycle was detected
        return False

# Example usage:
# Creating a linked list: 3 -> 2 -> 0 -> -4
head = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
# Creating a cycle: Connecting the last node (-4) to the second node (2)
head.next.next.next.next = head.next

# Create an instance of the Solution class and check for a cycle
sol = Solution()
print(sol.hasCycle(head))  # Output: True

"""
Time Complexity:

O(n), where n is the number of nodes. The slow and fast pointers traverse the list once.
Space Complexity:

O(1). We use only two extra pointers, so space complexity is constant.
"""

"""

3. Detect Cycle in a Doubly Linked List
Problem Statement:
Given a doubly linked list, determine if it has a cycle in it.
A doubly linked list has a prev and next pointer for each node. Use the Floyd's Tortoise and Hare algorithm to detect the cycle.

Example:

Input: Doubly Linked List: 3 <-> 2 <-> 0 <-> -4, with a cycle starting at node 2.

Output: True (The list contains a cycle)
"""
class DoublyListNode:
    def __init__(self, val=0, prev=None, next=None):
        # Initialize a node with a value, a reference to the previous node, and a reference to the next node
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def hasCycle(self, head: DoublyListNode) -> bool:
        # Use two pointers: 'slow' moves one step at a time, 'fast' moves two steps at a time
        slow = head
        fast = head
        
        # Traverse the list until 'fast' or 'fast.next' is None (indicating no cycle)
        while fast and fast.next:
            # Move 'slow' one step forward
            slow = slow.next
            # Move 'fast' two steps forward
            fast = fast.next.next
            
            # If 'slow' and 'fast' meet, a cycle exists in the list
            if slow == fast:
                return True
        
        # If the loop ends, no cycle was found
        return False

# Example usage:
# Create a doubly linked list: 3 <-> 2 <-> 0 <-> -4
head = DoublyListNode(3)
head.next = DoublyListNode(2)
head.next.prev = head
head.next.next = DoublyListNode(0)
head.next.next.prev = head.next
head.next.next.next = DoublyListNode(-4)
head.next.next.next.prev = head.next.next

# Create a cycle by linking the last node back to the second node
head.next.next.next.next = head.next  # Cycle at node with value 2

# Create an instance of the Solution class and check for a cycle
sol = Solution()
print(sol.hasCycle(head))  # Expected output: True

"""
Time Complexity:

O(n), where n is the number of nodes in the doubly linked list. We traverse the list once with two pointers.
Space Complexity:

O(1). We use constant space with two pointers.
"""


"""
4. Merge Two Sorted Linked Lists
Problem Statement:
Given the heads of two sorted linked lists, merge them into one sorted list. The list should be sorted in ascending order.

Example:

Input:
List 1: 1 -> 2 -> 4
List 2: 1 -> 3 -> 4

Output: Merged List: 1 -> 1 -> 2 -> 3 -> 4 -> 4
"""

class ListNode:
    def __init__(self, val=0, next=None):
        # Initialize a node with a value and a reference to the next node
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to simplify the merging process
        dummy = ListNode()
        # Use 'current' to build the merged list
        current = dummy
        
        # Traverse both lists while neither is exhausted
        while l1 and l2:
            # Compare the values of the current nodes in l1 and l2
            if l1.val < l2.val:
                # Attach the smaller node (l1) to the merged list
                current.next = l1
                # Move to the next node in l1
                l1 = l1.next
            else:
                # Attach the smaller node (l2) to the merged list
                current.next = l2
                # Move to the next node in l2
                l2 = l2.next
            # Move 'current' to the newly added node
            current = current.next
        
        # Attach the remaining nodes of the non-exhausted list
        current.next = l1 if l1 else l2
        
        # Return the merged list starting from the node after 'dummy'
        return dummy.next

# Example usage:
# Creating two sorted linked lists:
# l1: 1 -> 2 -> 4
# l2: 1 -> 3 -> 4
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

# Create an instance of the Solution class and merge the two lists
sol = Solution()
merged_head = sol.mergeTwoLists(l1, l2)

# Output the merged linked list
# Expected output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
while merged_head:
    print(merged_head.val, end=" -> ")
    merged_head = merged_head.next

# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
"""
Time Complexity:
O(n + m), where 𝑛 and 𝑚 are the lengths of the two linked lists.

Space Complexity:
O(1). We merge the lists in place without using any extra space for the new list.
"""


"""
5. Remove N-th Node From End of List
Problem Statement:
Given the head of a linked list, remove the  n-th node from the end of the list and return its head.

Example:

Input: Linked list: 1 -> 2 -> 3 -> 4 -> 5, 
n=2

Output: Modified linked list: 1 -> 2 -> 3 -> 5
"""

class ListNode:
    def __init__(self, val=0, next=None):
        # Initialize a node with a value and a reference to the next node
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Initialize two pointers, 'fast' and 'slow', both starting at the head
        fast = slow = head
        
        # Move 'fast' n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # If 'fast' is None, it means we need to remove the first node
        if not fast:
            return head.next
        
        # Move both 'fast' and 'slow' until 'fast' reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # 'slow.next' is the node to be removed; update the pointer to skip it
        slow.next = slow.next.next
        
        # Return the modified list starting from the head
        return head

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2  # Remove the 2nd node from the end

# Create an instance of the Solution class and remove the nth node from the end
sol = Solution()
new_head = sol.removeNthFromEnd(head, n)

# Output the modified list
# Expected output: 1 -> 2 -> 3 -> 5
while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next

"""
Time Complexity:

O(n), where n is the number of nodes in the list. We traverse the list twice.
Space Complexity:

O(1). We use a constant amount of space.
"""


"""
6. Find the Middle of a Linked List
Problem Statement:
Given the head of a linked list, return the middle node of the list. If there are two middle nodes, return the second one.

Example:

Input: Linked list: 1 -> 2 -> 3 -> 4 -> 5

Output: Middle node: 3
"""

class ListNode:
    def __init__(self, val=0, next=None):
        # Initialize a node with a value and a reference to the next node
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # Initialize two pointers, 'slow' and 'fast', both starting at the head of the list
        slow = fast = head
        
        # Traverse the list with 'fast' moving twice as fast as 'slow'
        while fast and fast.next:
            # Move 'slow' one step forward
            slow = slow.next
            # Move 'fast' two steps forward
            fast = fast.next.next
        
        # When 'fast' reaches the end, 'slow' will be at the middle
        return slow

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Create an instance of the Solution class and find the middle node
sol = Solution()
middle = sol.middleNode(head)

# Output the value of the middle node
# Expected output: 3
print(middle.val)

"""
Time Complexity:

O(n), where  n is the number of nodes in the linked list. We only need to traverse the list once.
Space Complexity:

O(1). We use only a constant amount of extra space.
"""

"""
7. Remove Duplicates from Sorted Linked List
Problem Statement:
Given a sorted linked list, remove the duplicates such that each element appears only once.

Example:

Input: Linked list: 1 -> 1 -> 2 -> 3 -> 3

Output: Modified linked list: 1 -> 2 -> 3
"""

class ListNode:
    def __init__(self, val=0, next=None):
        # Initialize a node with a value and a reference to the next node
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Initialize a pointer to traverse the linked list
        current = head
        
        # Traverse the list while 'current' and 'current.next' are not None
        while current and current.next:
            # Check if the current node's value is the same as the next node's value
            if current.val == current.next.val:
                # Skip the next node by updating the 'next' pointer to point to the node after the next
                current.next = current.next.next
            else:
                # Move to the next node if no duplicate is found
                current = current.next
                
        # Return the modified list starting from the head
        return head

# Example usage:
# Creating a linked list: 1 -> 1 -> 2 -> 3 -> 3
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))

# Create an instance of the Solution class and remove duplicates
sol = Solution()
new_head = sol.deleteDuplicates(head)

# Output the modified list
# Expected output: 1 -> 2 -> 3
while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next

# Output: 1 -> 2 -> 3
"""
Time Complexity:

O(n), where n is the number of nodes in the linked list.
Space Complexity:
O(1). We use constant space.

"""

"""
8. Find the Intersection Node of Two Linked Lists
Problem Statement:
Given the heads of two singly linked lists, return the node where they intersect. If they do not intersect, return null.
You must solve it in O(n) time complexity without using extra space.

Example:

Input: List 1: 1 -> 2 -> 3 -> 4 -> 5 List 2: 6 -> 7 -> 8 -> 3 -> 4 -> 5 (Intersection at node with value 3)

Output: Intersection node: 3
"""

class ListNode:
    def __init__(self, val=0, next=None):
        # Initialize a singly linked list node with a value and a reference to the next node
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # If either list is empty, there can't be an intersection
        if not headA or not headB:
            return None
        
        # Initialize two pointers, one for each list
        ptrA, ptrB = headA, headB
        
        # Traverse both lists; if one pointer reaches the end, redirect it to the other list
        while ptrA != ptrB:
            # Move pointer A to the next node or to the head of list B if it reaches the end
            ptrA = ptrA.next if ptrA else headB
            # Move pointer B to the next node or to the head of list A if it reaches the end
            ptrB = ptrB.next if ptrB else headA
        
        # The intersection node (if any) is where ptrA == ptrB
        return ptrA

# Example usage:
# Create two linked lists with an intersection:
# List A: 1 -> 2 -> 3 -> 4 -> 5
# List B: 6 -> 7 -> 8 \
#                     \
#                      -> 3 -> 4 -> 5
headA = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
headB = ListNode(6, ListNode(7, ListNode(8, headA.next.next)))  # Intersection at node with value 3

# Create an instance of the Solution class and find the intersection
sol = Solution()
intersection = sol.getIntersectionNode(headA, headB)

# Output the value of the intersection node or "No intersection" if there isn't one
print(intersection.val if intersection else "No intersection")  # Expected output: 3

"""
Time Complexity:

O(n + m), where n and m are the lengths of the two linked lists.
Space Complexity:

O(1). We only use two pointers, so no extra space is used.
"""


"""
9. Merge K Sorted Linked Lists
Problem Statement:
Given 
k sorted singly linked lists, merge them into a single sorted linked list.
Assume that each of the lists is already sorted.

Example:

Input: List 1: 1 -> 4 -> 5 List 2: 1 -> 3 -> 4 List 3: 2 -> 6

Output: Merged list: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6"""

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        # Initialize a singly linked list node with a value and a reference to the next node
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        # Initialize a min-heap to help with sorting the nodes
        heap = []
        
        # Push the first node of each list into the heap
        # Use (node value, index of list, node) as the heap elements
        # Index is added to break ties in case two nodes have the same value
        for i, node in enumerate(lists):
            if node:  # Only push non-empty lists
                heapq.heappush(heap, (node.val, i, node))
        
        # Create a dummy node to simplify list construction
        dummy = ListNode()
        current = dummy  # This pointer will help build the merged list
        
        # Continue until the heap is empty
        while heap:
            # Pop the smallest element (node) from the heap
            val, i, node = heapq.heappop(heap)
            # Add the node to the merged list
            current.next = node
            current = current.next
            # If the popped node has a next node, push it into the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        # Return the merged list, starting from the first real node (dummy.next)
        return dummy.next

# Example usage:
# Create k sorted linked lists:
# List 1: 1 -> 4 -> 5
# List 2: 1 -> 3 -> 4
# List 3: 2 -> 6
lists = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
]

# Merge all the k sorted lists
sol = Solution()
merged_head = sol.mergeKLists(lists)

# Output the merged sorted list:
while merged_head:
    print(merged_head.val, end=" -> ")
    merged_head = merged_head.next

# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
"""
Time Complexity:

O(N log k), where N is the total number of nodes across all lists and 
k is the number of lists. We are using a heap to merge the lists.
Space Complexity:

O(k), because we store up to 
k nodes in the heap at any point in time.
"""

"""
10. Add Two Numbers Represented by Linked Lists
Problem Statement:
Given two non-empty linked lists representing two non-negative integers, where the digits are stored in reverse order,
add the two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: List 1: 2 -> 4 -> 3 (represents 342) List 2: 5 -> 6 -> 4 (represents 465)

Output: Sum: 7 -> 0 -> 8 (represents 807)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        # Initialize a singly linked list node with a value and a reference to the next node
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize carry to handle values greater than 9
        carry = 0
        # Create a dummy node to simplify list construction
        dummy = ListNode()
        # Pointer to track the current position in the result list
        current = dummy
        
        # Loop through both lists until no nodes remain and there is no carry
        while l1 or l2 or carry:
            # Extract values from l1 and l2, or use 0 if the list has ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            # Calculate the sum of the current digits plus the carry
            total = val1 + val2 + carry
            # Update the carry for the next iteration
            carry = total // 10
            # Create a new node with the single-digit result and append it
            current.next = ListNode(total % 10)
            # Move the current pointer forward
            current = current.next
            
            # Move to the next nodes in l1 and l2 if available
            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next
        
        # Return the resulting list, starting from the first real node
        return dummy.next

# Example usage:
# Create two numbers represented by linked lists:
# l1: 2 -> 4 -> 3 (represents the number 342)
# l2: 5 -> 6 -> 4 (represents the number 465)
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

# Add the two numbers
sol = Solution()
result = sol.addTwoNumbers(l1, l2)

# Output the result as a linked list:
# The result represents 807, so it should output: 7 -> 0 -> 8
while result:
    print(result.val, end=" -> ")
    result = result.next

# Output: 7 -> 0 -> 8
"""
Time Complexity:

O(n), where n is the maximum length of the two linked lists.
Space Complexity:

O(n), where n is the maximum length of the two linked lists.
This concludes the next set of detailed questions and code examples. Let me know if you'd like further clarification or additional questions!

"""


"""
11. Find the Middle of a Linked List
Problem Statement:
Given a singly linked list, find the middle node. If there are two middle nodes, return the second middle node.
You should solve it in one pass (O(n) time complexity).

Example:

Input: List: 1 -> 2 -> 3 -> 4 -> 5

Output: Middle node: 3

"""
class ListNode:
    def __init__(self, val=0, next=None):
        # Initialize a node in the linked list with a value and a reference to the next node
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # Initialize two pointers: slow and fast, both starting at the head
        slow, fast = head, head
        
        # Traverse the list: fast moves two steps at a time, slow moves one step at a time
        while fast and fast.next:
            slow = slow.next      # Move slow pointer one step
            fast = fast.next.next # Move fast pointer two steps
        
        # When fast reaches the end of the list, slow will be at the middle
        return slow

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# Initialize the Solution object
sol = Solution()
# Get the middle node of the linked list
middle = sol.middleNode(head)
# Output the value of the middle node, which should be 3
print(middle.val)  # Output: 3

"""
Time Complexity:

O(n), where n is the number of nodes in the linked list. We traverse the list once with two pointers.
Space Complexity:
O(1). We use constant space with two pointers.
"""

"""
12. Remove Duplicates from a Sorted Linked List
Problem Statement:
Given a sorted linked list, delete all duplicates such that each element appears only once.

Example:

Input: List: 1 -> 1 -> 2 -> 3 -> 3

Output: Modified list: 1 -> 2 -> 3
"""

class ListNode:
    def __init__(self, val=0, next=None):
        # Initialize a node with a value (val) and a reference to the next node (next)
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Initialize a pointer 'current' that starts at the head of the list
        current = head
        
        # Traverse the list until we reach the end
        while current and current.next:
            # If the current node's value is equal to the next node's value
            if current.val == current.next.val:
                # Skip the next node by linking to the next of the next node
                current.next = current.next.next
            else:
                # Otherwise, move the current pointer to the next node
                current = current.next
        
        # Return the modified list (head remains the same, only next nodes are modified)
        return head

# Example usage:
# Create a linked list: 1 -> 1 -> 2 -> 3 -> 3
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
# Initialize the Solution object
sol = Solution()
# Call deleteDuplicates to remove duplicates from the list
result = sol.deleteDuplicates(head)

# Output the modified list after removing duplicates
# Expected output: 1 -> 2 -> 3
while result:
    print(result.val, end=" -> " if result.next else "")
    result = result.next

# Output: 1 -> 2 -> 3
"""
Time Complexity:

O(n), where n is the number of nodes in the linked list. We traverse the list once.
Space Complexity:

O(1). We use constant space, modifying the list in-place.
"""


"""
13. Reverse a Doubly Linked List
Problem Statement:
Given a doubly linked list, reverse the linked list and return the new head.

Example:

Input: List: 1 <-> 2 <-> 3 <-> 4

Output: Reversed list: 4 <-> 3 <-> 2 <-> 1
"""

class DoublyListNode:
    def __init__(self, val=0, prev=None, next=None):
        # Initialize a node with a value (val), a reference to the previous node (prev), and a reference to the next node (next)
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def reverseDoublyLinkedList(self, head: DoublyListNode) -> DoublyListNode:
        # Start with the head of the list
        current = head
        
        # Traverse the list and swap the prev and next pointers for each node
        while current:
            # Swap the next and prev pointers
            current.prev, current.next = current.next, current.prev
            
            # Move to the next node in the original list, which is now the prev pointer
            current = current.prev
        
        # After the loop, 'current' will be None, so return the new head, which is the last node we processed (previous head's prev)
        return head.prev if head else None

# Example usage:
# Create a doubly linked list: 1 <-> 2 <-> 3 <-> 4
head = DoublyListNode(1)
head.next = DoublyListNode(2, head)
head.next.next = DoublyListNode(3, head.next)
head.next.next.next = DoublyListNode(4, head.next.next)

# Initialize the Solution object
sol = Solution()
# Reverse the doubly linked list
reversed_head = sol.reverseDoublyLinkedList(head)

# Output the reversed list
# Expected output: 4 <-> 3 <-> 2 <-> 1
while reversed_head:
    print(reversed_head.val, end=" <-> " if reversed_head.next else "")
    reversed_head = reversed_head.next

# Output: 4 <-> 3 <-> 2 <-> 1

"""
Time Complexity:

O(n), where n is the number of nodes in the doubly linked list. We traverse the list once.
Space Complexity:

O(1). We use constant space, modifying the list in-place.
"""
""""
14. Flatten a Multilevel Doubly Linked List
Problem Statement:
Given a doubly linked list where in addition to the next and prev pointers, each node has a child pointer, flatten the list such that 
all the nodes appear in a single level doubly linked list.

Example:

Input: List: 1 <-> 2 <-> 3 -> child -> 4 <-> 5

Output: Flattened list: 1 <-> 2 <-> 3 <-> 4 <-> 5
"""
class Node:
    def __init__(self, val=0, next=None, prev=None, child=None):
        # Initialize a node with value 'val', next node pointer 'next', previous node pointer 'prev', and child node pointer 'child'.
        self.val = val
        self.next = next
        self.prev = prev
        self.child = child

class Solution:
    def flatten(self, head: Node) -> Node:
        # If the head of the list is None (empty), return None
        if not head:
            return None
        
        # Create a dummy node to simplify the handling of the first node and return the result later
        dummy = Node(0)
        prev = dummy  # 'prev' will track the previous node in the flattened list
        stack = [head]  # Stack to keep track of nodes that need to be processed
        
        # Traverse the list using the stack
        while stack:
            curr = stack.pop()  # Get the next node to process
            prev.next = curr  # Attach the current node to the flattened list
            curr.prev = prev  # Set the previous pointer of the current node
            prev = curr  # Move the 'prev' pointer to the current node
            
            # If the current node has a next node, push it to the stack to process later
            if curr.next:
                stack.append(curr.next)
            
            # If the current node has a child, push the child node to the stack to process it next
            # Then set the current node's child pointer to None because the child is now part of the flattened list
            if curr.child:
                stack.append(curr.child)
                curr.child = None
        
        # Return the flattened list starting from the next node of the dummy (since dummy is just a placeholder)
        return dummy.next

# Example usage:
# Create a list: 1 <-> 2 <-> 3 with a child for node 3 (4 -> 5)
head = Node(1)
head.next = Node(2, prev=head)
head.next.next = Node(3, prev=head.next)
head.next.next.child = Node(4)  # Node 3 has a child node 4
head.next.next.child.next = Node(5, prev=head.next.next.child)  # Node 4 has a next node 5

# Create a Solution object and flatten the list
sol = Solution()
flattened_head = sol.flatten(head)

# Output the flattened list:
# The expected output is: 1 <-> 2 <-> 3 <-> 4 <-> 5
while flattened_head:
    print(flattened_head.val, end=" <-> " if flattened_head.next else "")
    flattened_head = flattened_head.next

# Output: 1 <-> 2 <-> 3 <-> 4 <-> 5
"""
Time Complexity:

O(n), where n is the total number of nodes (including both regular and child nodes).
Space Complexity:

O(n), for the stack used to keep track of nodes.
"""


"""
15. Add a Node at the End of a Linked List
Problem Statement:
Given a singly linked list, add a new node with a given value at the end of the list.

Example:

Input: List: 1 -> 2 -> 3 Value to add: 4

Output: Modified list: 1 -> 2 -> 3 -> 4
"""

class ListNode:
    def __init__(self, val=0, next=None):
        # Initialize the node with a value and a pointer to the next node
        self.val = val
        self.next = next

class Solution:
    def addNodeAtEnd(self, head: ListNode, value: int) -> ListNode:
        # Create a new node with the given value
        new_node = ListNode(value)
        
        # If the list is empty, return the new node as the new head of the list
        if not head:
            return new_node
        
        # Traverse the list to find the last node
        current = head
        while current.next:  # Iterate until we find the last node (i.e., current.next is None)
            current = current.next
        
        # Attach the new node at the end of the list
        current.next = new_node
        
        # Return the original head, as it hasn't changed
        return head

# Example usage:
# Create an initial list: 1 -> 2 -> 3
head = ListNode(1, ListNode(2, ListNode(3)))

# Create an instance of Solution
sol = Solution()

# Add a new node with value 4 at the end of the list
new_head = sol.addNodeAtEnd(head, 4)

# Output the modified list:
# The expected output is: 1 -> 2 -> 3 -> 4
while new_head:
    print(new_head.val, end=" -> " if new_head.next else "")
    new_head = new_head.next

# Output: 1 -> 2 -> 3 -> 4
"""
Time Complexity:

O(n), where n is the number of nodes in the linked list. We traverse to the end of the list to insert the new node.
Space Complexity:

O(1). We only use constant space for the new node.

"""


"""
16. Find the Intersection Point of Two Linked Lists
Problem Statement:
Given two singly linked lists, determine if they intersect. If they do, return the intersection node; otherwise, return None.
The intersection is defined by the fact that the two lists share a common node (i.e., they merge at a specific node).

Example:

Input:
List A: 4 -> 1 -> 8 -> 4 -> 5
List B: 5 -> 0 -> 1 -> 8 -> 4 -> 5
Output: Intersection node: 8
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # If either of the lists is empty, return None
        if not headA or not headB:
            return None
        
        # Use two pointers, one for each list
        pointerA, pointerB = headA, headB
        
        # Traverse through the lists
        while pointerA != pointerB:
            # Move each pointer to the next node, or to the start of the other list when they reach the end
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        
        return pointerA  # Either the intersection node or None if no intersection

# Example usage:
headA = ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))
headB = ListNode(5, ListNode(0, ListNode(1, ListNode(8, ListNode(4, ListNode(5))))))

sol = Solution()
intersection_node = sol.getIntersectionNode(headA, headB)
print(intersection_node.val if intersection_node else None)  # Output: 8
"""
Time Complexity:

O(n + m), where n is the length of List A and m is the length of List B. We traverse both lists once.
Space Complexity:

O(1). We use constant space with two pointers.
"""

"""
17. Flatten a Linked List with Next, Child Pointers
Problem Statement:
Given a doubly linked list where each node has a next pointer and a child pointer, flatten the list such that all the child nodes appear 
after the parent node but in a single level list.

Example:

Input: List: 1 -> 2 -> 3 -> child -> 4 -> 5

Output: Flattened list: 1 -> 2 -> 3 -> 4 -> 5
"""
class Node:
    def __init__(self, val=0, next=None, prev=None, child=None):
        # Initialize a node with value, next pointer, prev pointer, and child pointer
        self.val = val
        self.next = next
        self.prev = prev
        self.child = child

class Solution:
    def flatten(self, head: Node) -> Node:
        # Return None if the head is empty
        if not head:
            return None
        
        # Create a dummy node to serve as a placeholder for the new flattened list
        dummy = Node(0)
        prev = dummy  # Pointer to the previous node in the flattened list
        stack = [head]  # Stack to manage nodes during depth-first traversal
        
        while stack:
            # Pop the current node from the stack
            curr = stack.pop()
            
            # Link the current node to the flattened list
            prev.next = curr
            curr.prev = prev
            prev = curr  # Move the prev pointer forward
            
            # If the current node has a next node, push it onto the stack
            if curr.next:
                stack.append(curr.next)
            
            # If the current node has a child, push the child onto the stack
            # Also, detach the child pointer after processing
            if curr.child:
                stack.append(curr.child)
                curr.child = None
        
        # Detach the dummy node's next pointer from the dummy node
        dummy.next.prev = None
        return dummy.next

# Example usage:
head = Node(1)
head.next = Node(2, prev=head)
head.next.next = Node(3, prev=head.next)
head.next.next.child = Node(4)
head.next.next.child.next = Node(5, prev=head.next.next.child)

sol = Solution()
flattened_head = sol.flatten(head)

# Output the flattened list
while flattened_head:
    print(flattened_head.val, end=" <-> ")
    flattened_head = flattened_head.next

# Output: 1 <-> 2 <-> 3 <-> 4 <-> 5
"""
Time Complexity:

O(n), where n is the total number of nodes in the list (including child nodes).
Space Complexity:

O(n), for the stack used to traverse the list.
"""

"""
18. Reverse a Linked List in Groups of K
Problem Statement:
Given a linked list, reverse the nodes of the list in groups of size k. If the number of nodes is not a multiple of k,
leave the last group as it is.

Example:

Input: List: 1 -> 2 -> 3 -> 4 -> 5, 
k=3

Output: Reversed in groups: 3 -> 2 -> 1 -> 4 -> 5
"""
class ListNode:
    def __init__(self, val=0, next=None):
        # Initialize a node with a given value and a pointer to the next node
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Check if the list is empty or k is 1 (no need to reverse the list)
        if not head or k == 1:
            return head
        
        # Function to reverse a segment of the linked list between start and end nodes
        def reverseLinkedList(start, end):
            # Initialize previous and current pointers
            prev, curr = None, start
            # Reverse the list between start and end nodes
            while curr != end:
                next_node = curr.next  # Save the next node
                curr.next = prev       # Reverse the current node's next pointer
                prev = curr            # Move prev and curr one step forward
                curr = next_node
            return prev  # Return the new head of the reversed segment
        
        # Create a dummy node to simplify edge cases (like reversing the first group)
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        # Loop through the list and reverse every k nodes
        while True:
            # Find the kth node from the current group_prev node
            kth_node = group_prev
            for _ in range(k):
                kth_node = kth_node.next
                # If we don't have enough nodes for another group, return the modified list
                if not kth_node:
                    return dummy.next
            
            # Save the next node after the kth node, which will be the start of the next group
            group_next = kth_node.next
            # Reverse the group of k nodes
            group_start = group_prev.next
            group_prev.next = reverseLinkedList(group_start, kth_node.next)
            group_start.next = group_next
            # Move group_prev pointer to the end of the reversed group
            group_prev = group_start
        
        return dummy.next  # Return the new head of the modified list

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 3  # We want to reverse nodes in groups of 3
sol = Solution()
result = sol.reverseKGroup(head, k)

# Output the modified list: 3 -> 2 -> 1 -> 4 -> 5
while result:
    print(result.val, end=" -> " if result.next else "")
    result = result.next

# Output: 3 -> 2 -> 1 -> 4 -> 5
"""
Time Complexity:

O(n), where n is the number of nodes in the list. We traverse each group once and reverse them in constant time.
Space Complexity:

O(1). We only use constant space for the operations.
"""


"""
19. Partition a Linked List
Problem Statement:
Given a linked list and a value  x, partition the linked list such that all nodes with values less than  x come before nodes
with values greater than or equal to x. The relative order of the nodes should be preserved.
Your task is to implement a function that rearranges the linked list based on this condition.

Example:

Input: A linked list: 1 -> 4 -> 3 -> 2 -> 5 -> 2 Partition value: 3

Output: Partitioned linked list: 1 -> 2 -> 2 -> 4 -> 3 -> 5

Explanation: After partitioning around the value 3, the list becomes 1 -> 2 -> 2 -> 4 -> 3 -> 5. The relative order within the partitions is preserved.

"""
class ListNode:
    def __init__(self, val=0, next=None):
        # Initialize a node with a value and a pointer to the next node
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x):
        # If the head of the list is empty, return None (no partitioning needed)
        if not head:
            return None
        
        # Create two dummy nodes to act as the start of two separate partitions:
        # one for values less than x and one for values greater than or equal to x
        smaller_head = ListNode(0)  # Dummy node for the "smaller" partition
        greater_head = ListNode(0)  # Dummy node for the "greater" partition
        
        # Pointers to the current node in each partition
        smaller = smaller_head
        greater = greater_head
        
        # Pointer to traverse the original linked list
        current = head
        
        # Traverse the original list and partition the nodes
        while current:
            if current.val < x:
                # If the current value is smaller than x, add it to the smaller partition
                smaller.next = current
                smaller = smaller.next  # Move the smaller pointer forward
            else:
                # If the current value is greater than or equal to x, add it to the greater partition
                greater.next = current
                greater = greater.next  # Move the greater pointer forward
            # Move to the next node in the original list
            current = current.next
        
        # After processing all nodes, ensure the "greater" partition ends by setting its next pointer to None
        greater.next = None
        
        # Link the end of the smaller partition to the head of the greater partition
        smaller.next = greater_head.next
        
        # Return the start of the smaller partition, which is after the dummy node
        return smaller_head.next

# Example usage:
# Create a linked list: 1 -> 4 -> 3 -> 2 -> 5 -> 2
head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))

x = 3  # The value to partition the list around
sol = Solution()
partitioned_head = sol.partition(head, x)

# Output the partitioned list
# The output should be: 1 -> 2 -> 2 -> 4 -> 3 -> 5
while partitioned_head:
    print(partitioned_head.val, end=" -> " if partitioned_head.next else "")
    partitioned_head = partitioned_head.next

# Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5 ->
"""
Input:

A linked list: 1 -> 4 -> 3 -> 2 -> 5 -> 2
Partition value: 3
Output:

Partitioned linked list: 1 -> 2 -> 2 -> 4 -> 3 -> 5
Time Complexity:

O(n), where n is the number of nodes in the linked list. We traverse through the list once to rearrange the nodes.
Space Complexity:

O(1). The solution uses only a constant amount of extra space, as we are rearranging the nodes in place.
"""


"""
20. LRU Cache Implementation
Problem Statement:
Design and implement an LRU (Least Recently Used) Cache. It should support the following operations:

get(key): Returns the value of the key if the key exists in the cache. Otherwise, returns -1.
put(key, value): Inserts the value if the key is not already present. If the cache reaches its capacity, it should evict the least recently used key.
The cache should use OrderDict (or equivalent) to maintain the order of access for efficient retrieval of the least recently used item.

Example:

Input:

Cache capacity: 2
Operations:
put(1, 1)
put(2, 2)
get(1)
put(3, 3)
get(2)
put(4, 4)
get(1)
get(3)
get(4)
Output:

get(1) returns 1
get(2) returns -1
get(3) returns 3
get(4) returns 4
"""

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed item to the end to mark it as recently used
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Move the key to the end to mark it as recently used
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Evict the first (least recently used) item
            self.cache.popitem(last=False)

# Example
cache = LRUCache(2)
cache.put(1, 1)  # Cache: {1: 1}
cache.put(2, 2)  # Cache: {1: 1, 2: 2}
print(cache.get(1))  # Output: 1, Cache: {2: 2, 1: 1}
cache.put(3, 3)  # Evicts key 2, Cache: {1: 1, 3: 3}
print(cache.get(2))  # Output: -1
cache.put(4, 4)  # Evicts key 1, Cache: {3: 3, 4: 4}
print(cache.get(1))  # Output: -1
print(cache.get(3))  # Output: 3
print(cache.get(4))  # Output: 4

"""
Input:

Cache capacity: 2
Operations:
put(1, 1)
put(2, 2)
get(1)
put(3, 3)
get(2)
put(4, 4)
get(1)
get(3)
get(4)
Output:

get(1) returns 1
get(2) returns -1
get(3) returns 3
get(4) returns 4
Time Complexity:

get operation: O(1) due to the constant time lookup and moving the accessed item to the end of the OrderedDict.
put operation: O(1) for insertion and evicting the least recently used item.
Space Complexity:

O(capacity), as the space used by the cache is proportional to the number of items stored.
"""