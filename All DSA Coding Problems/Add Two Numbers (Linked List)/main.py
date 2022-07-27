# Author:      Eddie F. Carrizales
# Date:        07/27/2022
# Problem Description:
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# ------UMPIRE------
# --Understand--
"""
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# --Match--
# - Linked list
# - array, string, int

# --Plan--
"""
1. initialize a carry = 0 , a curr1_val = 0 , and a curr2_val = 0
2. initialize a dummy node which will be our head for the new linked list we will create
3. create a while loop that traverses the linked lists while they have nodes and while the carry is not 0 (while it has a previous value)
4. now we will create a variable that will be our new_value, this will be the sum of the values in the linked list + prev carry (if there is one)
5. Next we check this new value with a condition, if this new value is greater than 9, then we will update carry to 1 and subtract 10 to get remainder
6. else if it is not greater than 9, set carry back to 0 because it means we already used it (we dont want to carry it over to every single number after using it)
7. After we have our new value and setting the carry for the next loop, we will create a new node using that new value and add the node to our dummy head
8. finally we create a condition to keep traversing the linked lists while one of them still has elements in it
9. return the head.next of our dummy node (we return head.next, since head is -1 and is not part of our answer)

"""

# --Implement--
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# Not part of solution (just used to print our linked lists)
def iterate_linked_list(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    print(arr)

# Leetcode input
#l1 = ListNode(2, ListNode(4, ListNode(3)))
#l2 = ListNode(5, ListNode(6, ListNode(4)))

l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

def addTwoNumbers(l1, l2):
    curr1 = l1
    curr2 = l2
    carry = 0

    # our dummy node that will be the new head and will point to the old head
    new_head = ListNode(-1)
    new_curr = new_head

    while curr1 is not None or curr2 is not None or carry != 0:
        #The starting values will be 0
        curr1_val = 0
        curr2_val = 0

        # If the current node in each list is not none, that means it has a value, so we will set the starting value
        # to that value it has, else it will stay with its starting value which is zero
        if curr1 is not None:
            curr1_val = curr1.val
        if curr2 is not None:
            curr2_val = curr2.val

        # This is where we add both values and the previous carry
        new_value = curr1_val + curr2_val + carry
        # If the new_value (i.e sum of both values + carry) is greater than 9, that means it will carry over 1
        if new_value > 9:
            carry = 1
            new_value -= 10
        else:
            # if the new_value is not greater than 9, then we reset the carry back to 0 to avoid carrying over again
            # if we already used the carry once
            carry = 0

        # Then we will create a new node with the new value and move one node forward so that we don't keep appending at the place every loop
        new_node = ListNode(new_value)
        new_curr.next = new_node
        new_curr = new_curr.next

        # conditionals to account for different list sizes, once we reach the end of one list, we still want to keep moving
        # on the other list that still has numbers.
        # if the curr1 is not none, we move to the next node
        if curr1 is not None:
            curr1 = curr1.next
        # if the curr2 is not none, we move to the next node
        if curr2 is not None:
            curr2 = curr2.next

    return new_head.next

iterate_linked_list(addTwoNumbers(l1, l2))

# --Review--
# My implementation initially worked with most edge cases, but there were some issues with different size lists
# I was able to solve the issue with different size lists by making the value 0 if the next element was none
# However, one last bug arose for one particular case: if we had 999 + 9999, or something similar, all the additionas
# and carry's would work, but the last node was missing. The code would stop one node short.
# After debugging the code for potential issues I decided to add a condition to the while loop to check for the carry value
# while the carry value still had a "carry" and was != 0, then we needed to add one more node to include it.
# After adding this additional condition the solution ran perfectly on leetcode

# --Evaluate--
# Time complexity: O(N+M) where N is the length of list1 and M is the length of list2
# Space complexity: O(N+M) since we are creating a whole new linked list of size N+M where N is size of list1 and M size of list2