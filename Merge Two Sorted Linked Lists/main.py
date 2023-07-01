# Author:      Eddie F. Carrizales
# Date:        07/24/2022
# Problem Description:
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# ------UMPIRE------

# --Understand--
"""
Example1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example2:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

# --Match--
# - Linked lists

# --Plan--
"""
There are various plans we can use to solve this problem:
Plan 1:
- Iterate through each linked list. Store their values into an array. 
  Sort the array, and rebuild the linked list with the values in the array.
  
Plan 2: (in this plan we are creating a new node every time and appending it)
- Build a new linked list. In each iteration, compare the head of the two linked lists.
  whichever head is the smaller values is the one that gets added to the new linked list we're building.
  Continue iterating until one is null and then add the rest of the other list to our newly built linked list.
  
Plan 3: (most efficient in terms of time complexity and space complexity, the one I will implement)
- Similar to plan 2, except that instead of building a new linked list we only create a new node (dummy node) 
  and change all the pointers of the other lists based on which value is smaller.
  So, We will create a dummy head, and starting from there, the dummy heads next will be whichever is the smaller head of the two linked lists.
  We continue repeating this step until one of the list's head is null. At which point we point it to the rest of the other linked list.
"""

# --Implement--
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def iterate_linked_list(node):
    arr = []
    while node:
        arr.append(node.val)
        arr.append(" ")
        node = node.next
    print(arr)

list1 = ListNode(1, ListNode(2, ListNode(4, ListNode(5, ListNode(7, ListNode(10))))))
list2 = ListNode(1, ListNode(3, ListNode(4)))

def mergeTwoLists(list1, list2):
    dummy_node = ListNode(0) # Creates new node with a value of 0

    dummy_head = dummy_node # keep reference of the head for when we are done and want to return it

    # tail initialization to keep track of the tail of the linked list (this is the pointer we will be working with)
    # We will append after this pointer, and the move the pointer forward once after appending so it will always point to the tail
    tail = dummy_node

    head1 = list1
    head2 = list2

    # while head1 and head2 are not none we iterate
    while head1 and head2:
        # if the value at head1 is less than head2, then we set head1 as the tail and move to the next element in head1 (in list1)
        if head1.val <= head2.val:
            tail.next = head1
            head1 = head1.next
        else:
            #else then head2 is smaller than head1, so we will set head2 as the tail and move to the next element in head2 (in list2)
            tail.next = head2
            head2 = head2.next
        # after adding a new node we want to make sure to move the tail to none again so none can be replaced with
        # another node, and we don't replace the node we just added
        tail = tail.next

    # If one of the linked list's node is none, that means we reached the end of that list, so we append
    # the tails.next to the head of the other list (which may still have elements)
    # if both are the same size, the tail.next will simply point to none since the other linked list will be none
    if head1 is None:
        tail.next = head2
    else:
        tail.next = head1

    # dummy head is the reference we saved, but it has the dummy node which is 0,
    # so we return its next which points to the first element we set as the tail, and so on until
    return dummy_head.next

iterate_linked_list(mergeTwoLists(list1, list2))

# --Review--
# Plan 3's implementation ran perfectly on leetcode.

# --Evaluate--
"""
Although there were 3 different plans/ ways to implement this problem not all of them are efficient:
Time complexity for plan 3 (our implementation): O(N) for one loop
Space complexity: O(1) since we did not use any extra space other than 1 new node. We reused the nodes we were given by repointing them

-------------
Time and space complexity for plan 2: O(N) time and O(N+M) space (since we are creating N + M nodes) (N is size of list1 and M size of list2) 

Time and space complexity for plan 1: O(NLogN) for the sorting of the array, and O(N+M) for rebuilding new linked list

"""