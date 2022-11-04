# Author:      Eddie F. Carrizales
# Date:        07/15/2022
# Problem description: Write a function that reverses a string.

#---UMPIRE---

# Understand
"""
Input: "hello"
Output: "olleh"

-We have to reverse a string
-What happens if the string is empty?
-return empty string
"""

# Match (ways we could solve the problem)
"""
-traversing the string with a sliding window
-two pointer approach
-storing the characters in hashmap
"""

# --Plan--
# Plan 1 - sliding window

"""
1. create a new empty string called reversed_string = ""
2. create a for loop
3. as we loop starting from the end of our given string, we add each char to our new string
4. print the new revered string
"""

# Plan 2 - two pointer
"""
1. create a new array
2. store the string in the array
3. create two pointers one on left side and one on right side
4. swap the characters at the two ends
5. once the pointers reach same position or cross, stop
6. make array into the new reversed string
7. return new reversed string
"""

# --Implement--
starting_input = "42 Wallaby Way, Sydney"

# implementation 1 using sliding window
def reverse_a_string1(given_string:str) -> str:
    reversed_string = ""

    for char in given_string[::-1]:     #for loop takes O(N)
        reversed_string += char # string concatenation take O(N)

    return reversed_string

print("Implementation 1: " + reverse_a_string1(starting_input))

# implementation 2 using two pointer
def reverse_a_string2(the_string:str) -> str:
    arr = []

    for char in the_string: # for loop takes O(N)
        arr.append(char) # append is constant time O(1)

    left = 0
    right = len(arr)-1

    while left < right:    # while loop takes O(N)
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

    return "".join(arr) # joins the array chars into a string takes O(1) time


print("Implementation 2: " + reverse_a_string2(starting_input))

# Review
# implementation 1 worked correctly
# implementation 2 worked correctly using two pointer approach

# Evaluate
#implementation 1
"""
time complexity: O(N) since there is one loop that will iterate through n characters
space complexity: O(N) since we will store a string of size n
"""

#implementation 2
"""
time complexity: O(N)
space complexity: O(N) since we will store a string of size n in an array
"""
