# Author:      Eddie F. Carrizales
# Date:        07/26/2022
# Problem Description: Given the head of a linked list, and an integer val, remove all the nodes of the
# linked list that have node.val == val

# ------UMPIRE------

# --Understand--
"""
Example:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Follow-up questions:
What if the value is not present in the given linked list?
A = Return the linked list
"""

# --Match--
# - Linked list problem
# - Two pointers (prev and current) and dummy node

# --Plan--
"""
1. we can start by creating a reference pointer to the dummy node (which will point to the head) as well as two pointers
2. we will also create a dummy node that will point to the head
2. Then we will iterate the given linked list
3. The current pointer will be one node ahead of the prev pointer (current starts at head, prev starts at dummy node)
4. both pointers will move one node at a time
5. if the current node's value is == given value, then set prev.next = current.next
6. else keep moving through the list
7. return the reference head pointer
"""

# --Implement--
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def iterate_linked_list(node):
    list_arr = []
    while node:
        list_arr.append(node.val)
        node = node.next
    print(list_arr)

# Leetcode input
#given_head = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
given_head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
given_val = 6

def remove_val_node(head, val):
    # create a dummy node and set its next pointer to the head (to append the given list to it)
    dummy_node = ListNode(0)
    dummy_node.next = head

    # create head reference to the dummy_node as well as create the prev node and current node
    head_reference = dummy_node
    prev_node = dummy_node
    current_node = head

    while current_node:
        # if current node's val == val, then we set the previous node = current node's next (i.e we remove the current node)
        iterate_linked_list(head_reference)
        print(f"{prev_node.val}   {current_node.val}")
        if current_node.val == val:
            prev_node.next = current_node.next
            # after removing the node in the line above, we must then move to the next node otherwise both pointers will now
            # point to the same node
            current_node = current_node.next
        # if the current node is not none and the current_node.val != val, then we move both the prev_node and current_node forward,
        # else we don't move at all, and we repeat the deletion condition above
        if current_node is not None and current_node.val != val:
            prev_node = prev_node.next
            current_node = current_node.next

    return head_reference.next # return head_reference.next to avoid the dummy.val 0

iterate_linked_list(remove_val_node(given_head, given_val))

# --Review--
# There was a bug in the code where it would skip values if all the values were the same (i.e [7,7,7,7])
# To fix this I added a condition where we would not move forward in the list after one deletion, unless we are certain the current value != val
# after adding this condition, the pointers would not move and would repeat another deletion until there were no values left
# This implementation worked perfectly on leetcode

# --Evaluate--
# Time complexity: O(N) since we only used a loop to traverse the array
# Space complexity: O(1) since all we did was change pointer in the linked list