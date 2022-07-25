# Author:      Eddie F. Carrizales
# Date:        07/24/2022
# Problem Description: Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
# following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer
# is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# ------UMPIRE------

# --Understand--
"""
- Can there be duplicate values? YES

Example 1:
Input: 3->2->0->4, and then the last node 4, points back to node 2 creating a cycle
Output: True (since there is a cycle we return True)

Example 2:
Input: 1
Output: False, since there is only one node and no cycle
"""
# --Match--
# - Linked list
# - fast and slow pointer technique to solve it

# --Plan--
"""
1. Initialize two pointers, a slow and a fast
2. Using a loop, while none of the pointers are None, we will keep moving them to traverse the linked list
3. The fast pointer will move twice as fast as the slow pointer and they will basically play "catch-up"
4. If the linked list has a cycle, the fast pointer will go back through the cycle and get behind the slow pointer
5. Eventually since its moving twice as fast it will catch up to it. Thus, if they are equal we return True (cycle found)
6. However, If any of the pointers are none, then we reached the end of the linked list and we found no cycle.
"""

# --Implement--
# Definition for singly-linked list. (From leetcode)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Leetcode Linked List Input (I usually implement it in a single line but leetcode's class constructor was oddly made, so it did not let me)
# Anyhow, this is how correct linked list initialization should be made even if it's long
head = ListNode(3)
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(-4)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node1

# Problem solution
def hasCycle(head):
    slow_node = head
    fast_node = head

    # We basically have two pointers, a fast and a slow pointer that both start at the head.
    # While none of them are None, nor fast.next is none, we will keep traversing the linked list with them
    # If the fast pointer "magically" becomes equal to the slow pointer, that means there was a cycle since it went back
    # through the cycle and then caught up to the slow pointer.
    while slow_node is not None and fast_node is not None and fast_node.next is not None:
        slow_node = slow_node.next # moves one node at a time through the list
        fast_node = fast_node.next.next # moves two nodes at a time through the list

        # If they become equal then return true since there is a cycle
        # Note that this conditional is placed here and not in the beginning of the loop, since they both start at the head.
        if slow_node == fast_node:
            return True

    # If the slow pointer or fast pointer or fast.next are None, this means that we reached the end of the list
    # If we reached the end this means there was no cycle and there for not an infinite loop through the linked list
    # Thus, we can return False
    return False

print(hasCycle(head))

# --Review--
# It was tricky dealing with the edge cases since there could be lists with only one or two nodes that would cause "out of bounds" referencing issues

# --Evaluate--
# Although the pointers chasing each other through the linked list may be confusing to understand in terms of
# time complexity, it will basically just be O(N) since we still only have one loop through the list
# The space complexity using the slow and fast pointer technique is O(1)