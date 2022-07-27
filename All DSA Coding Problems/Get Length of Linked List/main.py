# Author:      Eddie F. Carrizales
# Date:        07/27/2022
# Problem Description: Given a singly linked list, return its length

# ------UMPIRE------

# --Understand--
"""
Example 1:
Input:  1->2->3->4
Output: 4

Follow-up questions:
What if linked list is empty?
A = Return 0
"""
# --Match--
# linked list problem

# --Plan--
"""
1. create a counter variable
2. traverse the linked list using a while loop
3. while the node is not none we keep traversing and increasing the counter by one
4. return the counter
"""

# --Implement--
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# Input:
given_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

# solution
def get_linkedlist_length(head):
    list_length = 0

    #Iterate the given linked list
    while head:
        list_length +=1 # increase the length count
        head = head.next # goes to the next node in the list (basically used to iterate)
    return list_length

print(get_linkedlist_length(given_list))

# --Review--
# Simple to implement and pretty basic exercise

# --Evaluate--
# Time complexity: O(N) where N is the size of the given linked list
# Space complexity: O(1) since we operated on the given linked list and did not create anything else
