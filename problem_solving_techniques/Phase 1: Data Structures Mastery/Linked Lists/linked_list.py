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
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        return prev

# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()
reversed_head = sol.reverseList(head)

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
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False

# Example usage:
head = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
head.next.next.next.next = head.next  # Create cycle at node 2
sol = Solution()
print(sol.hasCycle(head))  # Output: True
"""
Time Complexity:

O(n), where n is the number of nodes. The slow and fast pointers traverse the list once.
Space Complexity:

O(1). We use only two extra pointers, so space complexity is constant.
"""


"""
3. Merge Two Sorted Linked Lists
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
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        current.next = l1 if l1 else l2
        return dummy.next

# Example usage:
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
sol = Solution()
merged_head = sol.mergeTwoLists(l1, l2)

# Output merged list
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
4. Remove N-th Node From End of List
Problem Statement:
Given the head of a linked list, remove the  n-th node from the end of the list and return its head.

Example:

Input: Linked list: 1 -> 2 -> 3 -> 4 -> 5, 
n=2

Output: Modified linked list: 1 -> 2 -> 3 -> 5
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        
        for _ in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head

# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2
sol = Solution()
new_head = sol.removeNthFromEnd(head, n)

# Output the modified list
while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next
# Output: 1 -> 2 -> 3 -> 5
"""
Time Complexity:

O(n), where n is the number of nodes in the list. We traverse the list twice.
Space Complexity:

O(1). We use a constant amount of space.
"""


"""
5. Find the Middle of a Linked List
Problem Statement:
Given the head of a linked list, return the middle node of the list. If there are two middle nodes, return the second one.

Example:

Input: Linked list: 1 -> 2 -> 3 -> 4 -> 5

Output: Middle node: 3
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow

# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()
middle = sol.middleNode(head)

# Output the middle node
print(middle.val)  # Output: 3
"""
Time Complexity:

O(n), where  n is the number of nodes in the linked list. We only need to traverse the list once.
Space Complexity:

O(1). We use only a constant amount of extra space.
"""

"""
6. Remove Duplicates from Sorted Linked List
Problem Statement:
Given a sorted linked list, remove the duplicates such that each element appears only once.

Example:

Input: Linked list: 1 -> 1 -> 2 -> 3 -> 3

Output: Modified linked list: 1 -> 2 -> 3
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
                
        return head

# Example usage:
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
sol = Solution()
new_head = sol.deleteDuplicates(head)

# Output the modified list
while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next
# Output: 1 -> 2 -> 3
"""
Time Complexity:

O(n), where 
𝑛
n is the number of nodes in the linked list.
Space Complexity:

O(1). We use constant space.

"""
"""

7. Detect Cycle in a Doubly Linked List
Problem Statement:
Given a doubly linked list, determine if it has a cycle in it.
A doubly linked list has a prev and next pointer for each node. Use the Floyd's Tortoise and Hare algorithm to detect the cycle.

Example:

Input: Doubly Linked List: 3 <-> 2 <-> 0 <-> -4, with a cycle starting at node 2.

Output: True (The list contains a cycle)
"""

class DoublyListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def hasCycle(self, head: DoublyListNode) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False

# Example usage:
head = DoublyListNode(3)
head.next = DoublyListNode(2)
head.next.prev = head
head.next.next = DoublyListNode(0)
head.next.next.prev = head.next
head.next.next.next = DoublyListNode(-4)
head.next.next.next.prev = head.next.next
head.next.next.next.next = head.next  # Create cycle at node 2
sol = Solution()
print(sol.hasCycle(head))  # Output: True
"""
Time Complexity:

O(n), where n is the number of nodes in the doubly linked list. We traverse the list once with two pointers.
Space Complexity:

O(1). We use constant space with two pointers.
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
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        ptrA, ptrB = headA, headB
        
        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA
        
        return ptrA

# Example usage:
# Create intersection at node with value 3
headA = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
headB = ListNode(6, ListNode(7, ListNode(8, headA.next.next)))  # Intersection at node 3
sol = Solution()
intersection = sol.getIntersectionNode(headA, headB)
print(intersection.val if intersection else "No intersection")  # Output: 3
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
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        heap = []
        
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode()
        current = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next

# Example usage:
lists = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
]
sol = Solution()
merged_head = sol.mergeKLists(lists)

# Output the merged list
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
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode()
        current = dummy
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next

# Example usage:
l1 = ListNode(2, ListNode(4, ListNode(3)))  # 342
l2 = ListNode(5, ListNode(6, ListNode(4)))  # 465
sol = Solution()
result = sol.addTwoNumbers(l1, l2)

# Output the result
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
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()
middle = sol.middleNode(head)
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
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

# Example usage:
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
sol = Solution()
result = sol.deleteDuplicates(head)

# Output the modified list
while result:
    print(result.val, end=" -> ")
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
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def reverseDoublyLinkedList(self, head: DoublyListNode) -> DoublyListNode:
        current = head
        while current:
            # Swap the next and prev pointers
            current.prev, current.next = current.next, current.prev
            # Move to the next node in the original list, which is now the prev pointer
            current = current.prev
        return head.prev if head else None

# Example usage:
head = DoublyListNode(1)
head.next = DoublyListNode(2, head)
head.next.next = DoublyListNode(3, head.next)
head.next.next.next = DoublyListNode(4, head.next.next)

sol = Solution()
reversed_head = sol.reverseDoublyLinkedList(head)

# Output the reversed list
while reversed_head:
    print(reversed_head.val, end=" <-> ")
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
        self.val = val
        self.next = next
        self.prev = prev
        self.child = child

class Solution:
    def flatten(self, head: Node) -> Node:
        if not head:
            return None
        
        dummy = Node(0)
        prev = dummy
        stack = [head]
        
        while stack:
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev
            prev = curr
            
            if curr.next:
                stack.append(curr.next)
            
            if curr.child:
                stack.append(curr.child)
                curr.child = None
        
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
        self.val = val
        self.next = next

class Solution:
    def addNodeAtEnd(self, head: ListNode, value: int) -> ListNode:
        new_node = ListNode(value)
        if not head:
            return new_node
        
        current = head
        while current.next:
            current = current.next
        current.next = new_node
        return head

# Example usage:
head = ListNode(1, ListNode(2, ListNode(3)))
sol = Solution()
new_head = sol.addNodeAtEnd(head, 4)

# Output the modified list
while new_head:
    print(new_head.val, end=" -> ")
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
        self.val = val
        self.next = next
        self.prev = prev
        self.child = child

class Solution:
    def flatten(self, head: Node) -> Node:
        if not head:
            return None
        
        dummy = Node(0)
        prev = dummy
        stack = [head]
        
        while stack:
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev
            prev = curr
            
            if curr.next:
                stack.append(curr.next)
            
            if curr.child:
                stack.append(curr.child)
                curr.child = None
        
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

O(n), where 
𝑛
n is the total number of nodes in the list (including child nodes).
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
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Check if the list is empty or k is 1 (no need to reverse)
        if not head or k == 1:
            return head
        
        # Function to reverse a segment of the list
        def reverseLinkedList(start, end):
            prev, curr = None, start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        # Create a dummy node
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        while True:
            kth_node = group_prev
            # Find the kth node
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return dummy.next
            group_next = kth_node.next
            # Reverse the group
            group_start = group_prev.next
            group_prev.next = reverseLinkedList(group_start, kth_node.next)
            group_start.next = group_next
            group_prev = group_start
        
        return dummy.next

# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 3
sol = Solution()
result = sol.reverseKGroup(head, k)

# Output the modified list
while result:
    print(result.val, end=" -> ")
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
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x):
        if not head:
            return None
        
        # Create two dummy heads for partitions
        smaller_head = ListNode(0)
        greater_head = ListNode(0)
        smaller = smaller_head
        greater = greater_head
        
        current = head
        while current:
            if current.val < x:
                smaller.next = current
                smaller = smaller.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        
        # Link the two partitions
        greater.next = None
        smaller.next = greater_head.next
        
        return smaller_head.next

# Example
head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
x = 3
sol = Solution()
partitioned_head = sol.partition(head, x)

# Output partitioned list
while partitioned_head:
    print(partitioned_head.val, end=" -> ")
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