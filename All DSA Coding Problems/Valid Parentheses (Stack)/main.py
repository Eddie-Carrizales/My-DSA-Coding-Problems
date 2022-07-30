# Author:      Eddie F. Carrizales
# Date:        07/30/2022
# Problem Description:
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
"""

# ------UMPIRE------

# --Understand--
"""
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Follow-up questions:
Can the symbols be nested? (For example: {()} return true ?)
-Yes, symbols can be nested

"""
# --Match--
# - Stack problem

# --Plan--
"""
1. create an empty stack
2. if the char/element is an opening brace, then append it to the stack
3. else then it must be a closing brace, so we check if it matches the one on the top of the stack (if so , then pop it off)
4. else if the closing brace does not match anything on the stack, then we have a mismatch so we return false (edge case: "{]" or ")" )
5. If we make it to the end of the string and our stack is empty, then we can return true. (our stack MUST be empty at the end)
6. else if we make it to the end of the string, but our stack has opening braces then we return false (edge case: "{{" )
"""

# --Implement--
# Leetcode input
given_string = "()[]{}"
# given_string = "[)"
# given_string = "{{"

# My solution
def isValid(s):
    stack = [] # create an empty stack

    for char in s:
        # If the character in the string is an opening brace, then we append it to the stack
        if char == "(" or char == "{" or char == "[":
            stack.append(char)
        else:
            # If it is not an opening brace, then it must be a closing brace, so while the stack is not empty we check
            # the type of element in the stack and if the current closing brace matches, then we pop the opening brace from the stack
            if stack and stack[-1] == "(" and char == ")":
                stack.pop()
            elif stack and stack[-1] == "{" and char == "}":
                stack.pop()
            elif stack and stack[-1] == "[" and char == "]":
                stack.pop()
            else:
                # If there is no match, this means we only have something like this {) and thus it is not valid, so we return false
                return False
    # In the edge case when we get something like this "{{"
    # Then, there wont be any matches or mismatches and so our stack will contain these two items
    # Thus, we can do a final check: if our stack is empty, then we matched everything and popped off everything, so we return true
    # else, there are still items left, and thus we return false
    if len(stack) == 0:
        return True
    else:
        return False

print(isValid(given_string))

# --Review--
# Solution ran perfectly on leetcode

# --Evaluate--
# Time Complexity: O(N) We only traversed the string using a single for loop
# Space Complexity: O(N) we used a stack which will grow up to N chars