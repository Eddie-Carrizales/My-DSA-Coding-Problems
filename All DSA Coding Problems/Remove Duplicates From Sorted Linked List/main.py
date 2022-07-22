# Author:      Eddie F. Carrizales
# Date:        07/21/2022
# Problem Description: Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

# ------UMPIRE------

# --Understand--
"""
-What if the linked list input is empty?
-Then return the empty head

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
"""

# --Match--
# - LinkedList problem

# --Plan--
"""
1. create two new variable a current_node and a next_node each pointing to head and head.next respectively
2. traverse the linked list with a loop, if the current_node.next is none then break the loop and return the head
3. if the current node and the next node have the same value then remove the next node 
4. if they do not have the same value then just move the head node forward
5. finally take care of edge case, if linked list is empty return none (i.e. current_node)
"""

# --Implement--
# Definition for singly-linked list.
class LinkedList:
    # constructor
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# Used to print the values for every node in the given linked list to visualize better (not part of the solution for the problem)
def iterate_linked_list(node):
    while node:
        print(node.val)
        node = node.next

# linked list input from leetcode
head = LinkedList(1, LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(3)))))
#head = LinkedList(1, LinkedList(1, LinkedList(2)))

# My solution
def remove_duplicates(head):
    current_node = head

    # edge case, if the linked list is empty return the current_node,  else we create the next_node
    if current_node is None:
        return current_node
    else:
        next_node = head.next

    # Using a while loop to traverse the linked list
    while current_node:
        # If the current_node.next is none that means we reached the end so we break (also takes care of edge cases)
        if current_node.next is None:
            break
        # if the current node's value is the same as the next node's value then we delete the next node
        if current_node.val == next_node.val:
            current_node.next = current_node.next.next # deletes a node by setting its previous pointer to its next
        else:
            current_node = current_node.next # if the next node's value is not equal to the current then we move the current forward

        next_node = next_node.next # we always move the next node forward
    return head

iterate_linked_list(remove_duplicates(head)) # calls remove duplicates and prints every value at every node

# --Review--
"""
Although my solution was correct and worked on leetcode perfectly, there is a much simpler way to write the code that is still O(N)
NOTE: The code below is not my own but I will put it here for reference:

def delete_duplicates(head):
    current = head
    
    while current:
        while current.next and current.next.val == current.val:
            current.next = current.next.next
        current = current.next
    return head
    
NOTE: just because there is a nested loop does not mean its O(N^2) because if you notice, it is only traversing the linked list once
"""

# --Evaluate--
# Time complexity: O(N) looping through linked list once
# Space complexity: O(1) Assuming the linked list we used was the input from leetcode
# NOTE: If the input did not come from leetcode it would be O(N) since we would create and use the linked list


