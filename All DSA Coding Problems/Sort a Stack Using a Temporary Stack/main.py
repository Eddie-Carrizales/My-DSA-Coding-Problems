# Author:      Eddie F. Carrizales
# Date:        07/30/2022
# Problem Description:
"""
Write a program to sort a stack such that the smallest items are on top.
-You can use an additional temporary stack, but you may not copy elements into any other data structure (such as an array).
-The stack supports the following operations : push, pop, peek, isEmpty.
"""

# ------UMPIRE------

# --Understand--
"""
- Input and output are both stacks

Example1:
Input : [34, 3, 31, 98, 92, 23]
Output : [3, 23, 31, 34, 92, 98]

Example2:
Input : [3, 5, 1, 4, 2, 8]
Output : [1, 2, 3, 4, 5, 8]

"""

# --Match--
# - Stack problem

# --Plan--
"""
1. create a temp stack
2. grab the first element of the given stack and store it temporarily
3. compare that element to the temp stack, 
    if there are any elements less than it then pop them and put them in the given stack 
    then place that temp element into the temp stack
4. repeat (note that we will repeat with the same elements since they are now in the given stack)
5. this will repeat until we run out of elements in the given stack
5. return the temp stack
"""

# --Implement--
# input
given_stack = [3, 5, 1, 4, 2, 8]
# Input : [34, 3, 31, 98, 92, 23]

# My solution
def sort_stack(stack):
    temp_stack = [] # create empty stack

    while stack:
        temp_val = stack.pop() # pop a value of the given stack and store it in a temporary value

        # while the elements in the temporary stack are greater than our temp value, we will pop them and put them back
        # into the given stack
        while temp_stack and temp_stack[-1] > temp_val:
            stack.append(temp_stack.pop()) # pop from temp stack and put into given stack

        # once we popped enough elements so that the rest of the elements in the temp stack are smaller than our temp value
        # then we can append the temp value to the temp stack and repeat previous process
        temp_stack.append(temp_val)

    return temp_stack # At the end, our temp stack will have all the elements from least to greatest, so return temp stack

print(sort_stack(given_stack))

# --Review--
# This problem was a bit challenging as I did not want to do an O(N^2) solution, and thus I was stuck trying to find an O(N)
# However, after trying a lot of approaches I looked up hints and realized there was only O(N^2) solution

# --Evaluate--
# Time complexity: O(N^2)
# Space complexity: O(N)

