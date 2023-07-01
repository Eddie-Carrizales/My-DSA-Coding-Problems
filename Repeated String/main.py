# Author:      Eddie F. Carrizales
# Date:        07/12/2022

#----UMPIRE----
#Understand
"""
-string s repeated infinitely many times
- find and print the number of letter a's in the first n letters of the infinite string

"""

#Match
"""
-string
-array/list
"""

#Plan
"""
1. get the ratio of a's to b's
2. multiply that number by the number of characters
3. round the number

"""

#Implement
s = "aba"
n = 10

count_a = 0

# counts the number of a's in our given string
for char in s:
    if char == "a":
        count_a += 1

# the whole number of chars from the string that fit into the available number of chars n
whole_num_of_chars = n // len(s) # divides n by len(s) and truncates any decimals
total_a = count_a * whole_num_of_chars

# the number of characters that where cut off and did not fit into the available number of chars n
remainder_of_chars = n % len(s)

additional_a = 0
# will count the number of chars in the remainder part of the string
for char in range(0, remainder_of_chars):
    if s[char] == "a":
        additional_a += 1

print(total_a + additional_a)

#Review
# Struggled to pass all test cases due to the decimals in some numbers rounding up.
# I had to review my approach and instead of doing a simple rounding, actually count the number of a's in the decimal part
# to do this I had to implement modulo and count the number of a's in the string from 0 to the remaining characters of the string
# to determine if there was an "a" in that section of the string or not.

#Evaluate
"""
time complexity: O(N) due to for loops

space complexity: O(1)
"""







