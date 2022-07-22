# Author:      Eddie F. Carrizales
# Date:        07/21/2022
# Problem Description: Given the head of a linked list, remove the nth node from the end of the list and return its head.

# ------UMPIRE------

# --Understand--
"""
My understanding: we have to remove the node at position n, counting/starting the position from the end of the list.

What if n > length of the linked list? I will assume that will never happen

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

"""
# --Match--
# - linked list problem

# --Plan--
"""
1. Iterate through the linked list to count the number of nodes
2. get the index of the node we need to remove (number of nodes - n)
3. using another loop iterate through the linked list to find the index to remove and remove it by setting
    the current_node.next = current_node.next.next
4. finally take care of special edge cases (add a condition where if linked list only had one node, then return None (i.e head.next))
"""

# --Implement--

# Definition for singly-linked list
class ListNode:
    # constructor
    def __init__(self, val= 0, next= None):
        self.val = val
        self.next = next

# Input from leetcode (not the most fancy initialization of a linked list, but gets the job done)
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2

# created just to help me visualize the output values from our linked list (not part of the problem or solution)
def iterate_linked_list(node):
    while node:
        print(node.val)
        node = node.next

# My solution
def remove_nth_pointer(head, n):
    current_node = head

    num_nodes = 0
    # loop to count the number of nodes in the linked list
    while current_node:
        num_nodes +=1
        current_node = current_node.next

    # get the index of the node we need to remove
    index_to_remove = num_nodes - n

    # Edge case when only one node (i.e. the head)
    if index_to_remove == 0:
        return head.next # returns None since the .next is none

    index = 0
    current_node = head # reset current_node position back to the head
    # loop to look for the node to remove in the linked list
    while True:
        if index == index_to_remove -1:
            current_node.next = current_node.next.next
            break # breaks out of the while loop, since nothing will stop the loop from going forever
        index += 1
        current_node = current_node.next # used to traverse the linked list
    return head

iterate_linked_list(remove_nth_pointer(head, n)) # is sent to iterate linked list to receive our printed output

# --Review--
# Code worked, but went back and added the conditional to check for the edge case when there was only one node in our linked list

# --Evaluate--
# Time complexity: O(N) to count the number of nodes in the linked list + O(N) to find the node to remove
# which is O(N+N) = O(2N) = simply O(N)

# space complexity: O(1) since the linked list is given to us from leetcode
# Note: if we were to create the linked list ourselves in another situation, it would be O(N) since the amount of data 
# stored increases linearly with the number of nodes in the linked list
