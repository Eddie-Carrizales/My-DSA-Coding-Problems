# Author:      Eddie F. Carrizales
# Date:        08/01/2022
# Problem Description:
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""
# ------UMPIRE------

# --Understand--
"""
Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

# --Match--
# - Stack problem

# --Plan--
"""
- The push, pop, top methods are easy to implement in the class (using regular python array/list)

- The first instinct to create the getmin method would be to keep track of the smallest number as we are pushing 
  the numbers into the stack. However, this will cause a problem because when we pop, there wont be any way to 
  keep track of what is not in the stack anymore an thus it could cause issues.
- Thus, the second approach to implement the getmin method will require an extra temporary stack to compare all
  the values in the stack and put them back

Plan:
- 1. create an new empty temp stack called the min_stack = []
- 2. in the push method, add a conditional to check if the min_stack is empty or if there is a value smaller than the
     one we are going to append in the regular stack. If so, then we will also append this value to the min stack since
     it is the smallest value we currently have. NOTE: If a value greater than min_stack[-1] is being added, we only add
     it to the regular stack since we only want smaller values in the min stack
- 3. In the pop method, if the value we are going to pop == top value in our min stack, then we have to pop from both.
     We do this because that small value in our min stack wont exist in our regular stack so we have to remove from both
     Note: if they dont match, then we can just remove it from our regular stack since it is a big number and we dont care about it.
-4.  Finally, in our get min method, we can simply return the top of the min stack since it will contain the smallest value at the top
"""

# --Implement--
# --Leetcode starting code--
# class MinStack:
#
#     def __init__(self):
#
#     def push(self, val: int) -> None:
#
#     def pop(self) -> None:
#
#     def top(self) -> int:
#
#     def getMin(self) -> int:

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Leetcode input
#["MinStack","push","push","push","getMin","pop","top","getMin"]
#[[],[-2],[0],[-3],[],[],[],[]]

# My solution
class MinStack:

    def __init__(self):
        self.stack = [] # initializes an empty stack
        self.min_stack = [] # create the min_stack (stack that will hold the min values) (temporary stack)

    def push(self, val: int) -> None:
        self.stack.append(val) # adds a value to top of the stack

        # If the min_stack is empty or the value is less than the current value in the min_stack, then we will append
        # the small value, else we dont do anything since the value is bigger that any current value in the min_Stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # When we are removing a value, if the value in the real stack == to the value in the min stack
        # Then we will remove the value in both stacks. (since that small value is gone)
        # else the value is greater than the current value in our min stack, and thus we dont care about it so we pop it off regular stack
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        self.stack.pop() # pop off regular stack

    def top(self) -> int:
        return self.stack[-1] # returns the top value from the stack

    def getMin(self) -> int:
        return self.min_stack[-1] # peek at the last value in our min stack since that is the smallest value we have added

# testing our class using leetcode instantiation
minStack = MinStack()
minStack.push(-2),
minStack.push(0),
minStack.push(-3),
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())

# --Review--
# It is simple to implement. However, it is also easy to create a solution that is not very efficient.
# In this particular problem we wanted a solution that was O(1) time since O(N) was too slow for large amounts of data

# --Evaluate--
# Time complexity: O(1) since we did not use any loops
# Space complexity: O(N) since we created an additional stack to keep track of the min numbers