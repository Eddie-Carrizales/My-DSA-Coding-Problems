# Author:      Eddie F. Carrizales
# Date:        08/29/2022
# Problem Description:
"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation (Evaluate Postfix Expression).
- Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
- Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid.
That means the expression would always evaluate to a result, and there will not be any division by zero operation.
"""
# ------UMPIRE------

# --Understand--

"""
Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Follow-up Questions or Observations:
- The given array has the values in type string, so we must convert them to int
- the result of the division must also be converted to type int to keep integer and remove all decimals
- the division and subtraction operations must be flipped since order matters for those
"""
# --Match--
# -Stack problem

# --Plan--
"""
1. create a stack
2. traverse the array from left to right 
3. add elements to the stack
4. if we see an operation symbol, pop the previous elements and perform the operation
5. put the result of the operation back into the stack and continue traversing the array
6. at the end return the value in our stack (there should only be one value left)
"""

# --Implement--
# leetcode inputs:
#given_tokens = ["2","1","+","3","*"]
given_tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#given_tokens = ["4","-2","/","2","-3","-","-"]

def evalPostfixExpr(tokens):
    stack = []

    #traverse the array and add elements to the stack
    for element in tokens:
        if element == "+":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 + num2)
        elif element == "-":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2 - num1)
        elif element == "/":
            num1 = stack.pop()
            num2 = stack.pop()
            result = num2 / num1
            stack.append(int(result)) # convert result to integer to truncate remaining values
        elif element == "*":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 * num2)
        else:
            # NOTE: Really important to append as integers here
            # The elements in the stack are type string, if we cast here, we don't have to convert every time we pop in the other conditionals
            stack.append(int(element))
    return stack[-1] # return the last element in the stack (i.e the top element)

print(evalPostfixExpr(given_tokens))

# --Review--
# Code ran perfectly on leet code, the only bug I faced had to do with the division.
# I did not realize I was converting the nums to int and not the result of their division, but it was a quick fix

# --Evaluate--
# Time complexity: O(N) since we only went through every value in the array
# Space complexity: O(N) since we are using a stack, and it will grow up to N elements before shrinking down to 1