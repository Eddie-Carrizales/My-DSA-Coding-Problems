# Author:      Eddie F. Carrizales
# Date:        07/16/2022

# problem description: Given a string s, return true if the s can be palindrome after deleting at most one character from it.

#---UMPIRE---

# Understand
"""
Examples:
Input: s = "aba"
Output: True

Input: s = "abca"
Output: True
Explanation: You could delete the character 'c'.

Input: s = "abc"
Output: false
"""

# Match
# - Two pointer approach
# - or recursive

# Plan
"""
1. make string lowercase to account for any uppercase letter in the string
2. check string against alphanumeric characters to ignore them
3. make a left and right pointer and a loop to check whether the characters match
4. this is where it gets a bit tricky, if the characters do not match, move the right pointer once
5. if the match after moving the right pointer once, then can continue moving both pointer simultaneous until they cross 
7. if the pointers cross we have passed through the string and we return true
6. else it is not a palindrome since we had more non-matching characters
"""

# Implement
s = "abca"

def is_palindrome_2(given_string):
    given_string = given_string.lower()
    left = 0
    right = len(given_string) - 1
    while left < right:

        # check if a char is not alphanumeric, if it is not, we skip it
        if not given_string[left].isalnum():
            left += 1
        if not given_string[right].isalnum():
            right -=1

        if given_string[left] == given_string[right]:   # if the characters match we move both pointers
            left +=1
            right -=1
        else:
            skip_left = given_string[left + 1 : right + 1] # skip a char on the left (the right + 1 is used because the value current right value is not inclusive so we have to go back once)
            skip_right = given_string[left : right] # skip a char on the right (the right value is not inclusive so it is like doing right - 1)

            # if the reverse of the string skipping left is true or the reverse of the string skipping right is true, then we have a palindrome
            if skip_left == skip_left[::-1] or skip_right == skip_right[::-1]:
                return True
            else:
                return False
    return True

print(is_palindrome_2(s))

# Review
# I was able to make this palindrome better than the previous palindrome problem by avoiding the use of an array
# the only bug I encountered in this problem was with large strings, if we skip the left char or the right char
# since if we end up skipping the wrong side, everything else will not be detected as a palindrome
# to solve this bug we must check if skipping left is equal to its reverse or skipping right is equal to its reverse
# this way if either is true then we can say it is a palindrome

# Evaluate
# time complexity : O(N) we only used one while loop and the iterations will depend on size of string
# space complexity : O(1) we will have constant time since we performed all operations on the string