# Author:      Eddie F. Carrizales
# Date:        07/27/2022
# Problem Description: Given the head of a linked list, rotate the list to the right by k places.

# ------UMPIRE------

# --Understand--
"""
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""
# --Match--
# - Linked lists

# --Plan--
"""
mod len list to determine how many rotations we've done (use counter)

1. Find the length of the list
2. point the last node of the linked list to the head to make it a circular linked list
3. reset the current node to the head
4. instead of rotating k times, we want to find the node we will end up at starting from the head
    a. to do this we will do: stop_index = list_length - k % list_length
5. then we will create a while loop with an index starting from 0 and up to that stop index
    a. inside the while loop we will move one node forward
6. once we exit the while loop we will point the prev pointer to None
7. and set current to head
8. return the head
"""

# --Implement--
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def show_list(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    print(arr)

# Leetcode input
given_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
given_k = 2
# given_head = ListNode(0, ListNode(1, ListNode(2)))
# given_k = 4

def rotateRight(head, k):
    list_length = 1 # set to 1 since we will stop at curr_head.next instead of curr_head
    curr_head = head

    # If the linked list is empty, just return the empty list
    if curr_head is None:
        return curr_head

    # Get the length of the linked list and leave curr_head at the last node
    while curr_head.next:
        list_length += 1
        curr_head = curr_head.next

    curr_head.next = head # points the last node to the head to make the linked list circular

    curr_head = head # resets current_head to the head of the list

    # Rotate the list
    stop_index = list_length - k % list_length
    i = 0
    while i < stop_index:
        # Move both forward once
        prev = curr_head
        curr_head = curr_head.next

        i += 1

    # After we finish rotating, we set the previous node's next to None so that we don't have a cycle in the linked list
    prev.next = None
    new_head = curr_head # set the new_head

    return new_head

show_list(rotateRight(given_head, given_k))

# --Review--
# This was a medium leetcode problem and while I had the correct logic of creating a cycle and stopping,
# I was having issues implementing the solution and had to look up hints.
# Finally, the solution ran successfully on leetcode

# --Evaluate--
# Time complexity: O(N)
# Space complexity: O(1)