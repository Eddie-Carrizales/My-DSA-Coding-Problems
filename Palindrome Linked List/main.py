# Author:      Eddie F. Carrizales
# Date:        07/27/2022
# Problem Description: Given the head of a singly linked list, return true if it is a palindrome.

# ------UMPIRE------

# --Understand--
"""
Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
"""

# --Match--
# - linked list and two pointers

# --Plan--
# There are two ways to implement this:
# 1. put everything from the linked list into an array and solve using two pointers in the array (Will take O(N) space)
# 2. Reverse the second half of the linked list and attach it to a dummy node, then compare both linked lists to see if they match
"""
I will implement plan 2 since it has O(1) space: (Plan below)
1. find the length of the given linked list
2. split the linked list in half (at node length_found/2)
3. Reverse the second half of the linked list
4. Iterate both linked lists starting at the head of each
5. As we are iterating if we find any mismatch return False, else if we reach the end in both without a mismatch return True
"""

# --Implement--
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# prints the given linked list (not part of solution)
def show_list(node):
    arr = []

    while node:
        arr.append(node.val)
        node = node.next
    print(arr)

# Leetcode input
given_head = ListNode(1, ListNode(1, ListNode(0, ListNode(0, ListNode(1)))))

# My solution
def isPalindrome(head):
    head1 = head
    curr1 = head
    head2 = None # will later point to the head of our second linked list

    # find the length of the linked list
    list_length = 0
    while curr1:
        list_length +=1
        curr1 = curr1.next
    curr1 = head

    # Split the list in half
    index = 1
    while curr1 is not None:
        # If the index is greate than the list_length/2, then that is where we split our linked list
        if index >= list_length/2:
            temp = curr1.next
            curr1.next = None
            head2 = temp

        index +=1
        if curr1:
            curr1 = curr1.next # used to keep iterating curr1

    # Reverse the second half of the linked list (In simple word, we do this by flipping all the pointers in our list)
    # At the end after flipping all pointers, the new head will be the prev pointer
    prev = None
    curr2 = head2
    while curr2 is not None:
        next_node = curr2.next
        curr2.next = prev
        prev = curr2
        curr2 = next_node

    head2 = prev # make head2 our head since prev is now the head after reversing the list

    # Iterate through both linked lists while the nodes are not null, if there is a mismatch return False
    # If we make it through to the end of the list, return True since there was no mismatch
    while head1 is not None and head2 is not None:
        if head1.val != head2.val:
            return False

        # used to keep iterating the lists
        head1 = head1.next
        head2 = head2.next
    return True

print(isPalindrome(given_head))

# --Review--
# The code ran perfectly on leetcode, this problem was a bit hard to implement in O(N) time and O(1) space
# However, I was able to solve it by breaking down the problem into parts

# --Evaluate--
# Time complexity: O(N) since we only use single loops that traversed the given linked list
# Space complexity: O(1) since we did all operations on the given linked list by moving pointers around
