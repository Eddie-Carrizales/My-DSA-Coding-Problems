# Author:      Eddie F. Carrizales
# Date:        07/26/2022
# Problem Description:
# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only
# distinct numbers from the original list. Return the linked list sorted as well.

# ------UMPIRE------

# --Understand--
"""
Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

# The list is guaranteed to be sorted in ascending order.
"""
# --Match--
# - Linked list, dummy node, and hashtable

# --Plan--
"""
1. Create a new empty hashtable and create a current node that points to the head
2. using a while loop and the hashtable count all of the values in the given linked list that are duplicates
3. The way we will do this: if not in hashtable, initialize to 1, else increase count +1
4. Then we will create a dummy node and a dummy reference node
5. Using another while loop, if the value in our hashtable, is 1, then we can append it to our dummy node since 
   we know there is only one of that value in the linkedlist.
6. Also we must make sure to keep moving the dummy head so that we dont keep appending to the head
7. finally we reach the end of the given linked list we are traversing and the loop ends
8. We return the dummy_node reference.next (the .next is important so that we dont include the 0 value of the dummy node)

"""

# --Implement--
class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# print linked list (not part of problem solution)
def iterate_list(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    print(arr)

# Leetcode input
given_list = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(3, LinkedList(4, LinkedList(4, LinkedList(5)))))))
#given_list = LinkedList(1, LinkedList(1, LinkedList(2)))
def remove_duplicates(head):
    current_node = head
    hash_table = {}

    # Loop to count the number of repeating values in our linked list (will be stored as {value: count})
    while current_node:
        # if the value is not in our hashtable then add it to the hash table with a count of 1, else increase its count
        if current_node.val not in hash_table:
            hash_table[current_node.val] = 1
        else:
            hash_table[current_node.val] +=1

        current_node = current_node.next # move to the next node in the linked list

    # create dummy node
    dummy_node = LinkedList(0)
    dummy_head = dummy_node
    dummy_head_reference = dummy_node

    current_node = head # reset the current node to the head, so we can loop again through the linked list

    # loop to check if the count of the value is 1, and if so, then append it to our dummy node since it is not a repeating number
    while current_node:
        if hash_table[current_node.val] == 1:
            # Create a new node with the value stored in our hashtable and set the dummy_head.next pointer to that new node
            new_node = LinkedList(current_node.val)
            dummy_head.next = new_node

            dummy_head = dummy_head.next # move to the next element in the new linked list so that we don't append to the same node

        current_node = current_node.next # move to the next element in the main linked list
    return dummy_head_reference.next # return the reference to the head of the dummy linked

iterate_list(remove_duplicates(given_list))

# --Review--
# Although there are several (more space efficient) ways to solve this problem, I was able to solve it using a hashtable and a dummy node
# The code ran perfectly on leetcode and passed every test case

# --Evaluate--
# Time complexity: O(N) since we only iterated the linked list using loops
# Space complexity:
# We could argue that creating the dictionary storage is O(1) since it will only ever store values from 0-9
# However, since we are creating new nodes (i.e a whole new linked list), this will take O(N)
# Thus in total we will have O(N) + O(1) = basically O(N)

