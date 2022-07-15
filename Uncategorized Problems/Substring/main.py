# Author:      Eddie F. Carrizales
# Date:        07/15/2022
# Problem description: Write a function that takes in two strings and returns true if
# the second string is substring of the first, and false otherwise.

# ---UMPIRE Method---

# Understand
"""
Input: We are given two string, if the second string is a substring of the first
meaning that it appears inside the first string, then we will return true
else if the second string does not appear inside the first then we return false

Output: true or false

edge case questions:
1. what if the first string is capitalized and the second string is the same but in lowercase?
should I return true?
A = In this case I will assume that they are different strings. However, a quick solution to this
would be to use .lower function to make the strings always lowercase and therefore match them
"""

# Match
"""
-Every time we see the word "substring" it is most likely a set or sliding window problem
-can also be a two pointer
"""

# Plan
"""
1. create a for loop to go through the string
2. we create a sliding window of size of our substring
3. if we see our substring in the string we return true
4. else if we have reached the end and there is no substring we return false
"""

# Implementation 1
string1 = "laboratory"
string2 = "rat"

def has_substring(input_string, substring):
    point_input_string = 0
    point_substring = 0

    # since the empty string is in every string
    if len(substring) < 1:
        return True

    while input_string:
        if point_input_string == len(input_string): # if we reach the end of our string1
            return False
        elif input_string[point_input_string] == substring[point_substring]: # if a char in string1 matches a char in string2
            point_substring += 1
            if point_substring == len(substring): # if we reach the end of string2 (meaning we found every character therefore finding it as substring in string1)
                return True
        point_input_string += 1

print(has_substring(string1, string2))

# Review
# there were some problems with index out of bounds when our potential substring was an empty string
# to solve this a base case was set to return true since every string will contain the empty string as substring

# Evaluate
# time complexity: O(N) where n is the length of the first string
# Space complexity: O(1)