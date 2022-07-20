# Author:      Eddie F. Carrizales
# Date:        07/10/2022

#----UMPIRE----

# Understand
"""
-input: we are given a number n that represents the height and width of a staircase
-output: we are to print a staircase of the size of the given n
"""

# Match
"""
-2D array or single array(printed multiple times)
-Iterative
-string
-Queue
"""

# Plan
"""
1. we could create an array that starts with a n-1 spaces and a # at the end
2. then in a for loop we print the array, and then replace the rightmost space with #
3. we repeat the process until we reach the front of the array

"""
n = 7
arr = [" "] * n

# Implement
for i in range(0,n):
    arr.pop(0)
    arr.append("#")

    full_string = ""
    for k in arr:
        full_string += k

    print(full_string)

# Review
# passed all test cases in hackerrank, but I am not totally happy with the solution due to nested loop

# Evaluate
"""
time complexity: O(N^2)

space complexity: O(N)
"""

########## Stack overflow solution ##########
# This solution from stackoverflow uses only one for loop reducing the time complexity to O(N) and space to O(1)
"""
def staircase(num_stairs):
    for stairs in range(1, num_stairs + 1):
        print(' ' * (num_stairs - stairs) + '#' * stairs)
"""