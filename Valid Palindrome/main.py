# Author:      Eddie F. Carrizales
# Date:        07/16/2022

# Problem description:
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
# removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

# ---UMPIRE---

# Understand
# - A palindrome is basically a word or sentence that reads the same both forwards and backwards
#
# example:
# Input: string s = "A man, a plan, a canal: Panama"
# Output: True (it is a palindrome)
# explanation: "amanaplanacanalpanama" is a palindrome.

# Match
# - two pointer approach
# - recursive could also be done but two pointer is faster

# Plan
"""
1. process the string to make it all lowercase
2. process the string to remove all comas and spaces by putting it in an array
3. make two pointers, one on left an one on right
4. make a loop and every loop check whether the chars at the pointers match
5. if the match move both pointers forward
6. if the pointers eventually cross eachother then we have a palindrome
7. if the chars at the pointers do not match then simply return false since the word is not a palindrome

"""

# Implement
s = "A man, a plan, a canal: Panama"


def is_palindrome(given_string):
    arr = []
    given_string = given_string.lower() # make string lowercase

    # for loop takes O(N) time
    for char in given_string:
        if char.isalnum():
            arr.append(char) # append takes O(1)

    left = 0
    right = len(arr) - 1

    # while loop takes O(N/2)
    while left < right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

print(is_palindrome(s))

# Review
# The two pointer implementation worked correctly
# I could have done this problem without having to create another array and doing all the checking on the string
# this would have reduced my space complexity from O(N) to O(1)

# Evaluate
# time complexity: O(N)
# space complexity: O(N) since we created an array