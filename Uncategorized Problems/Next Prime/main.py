# Author:      Eddie F. Carrizales
# Date:        07/15/2022
# Problem description: Given a number, return the next smallest prime number
# Note: A prime number is greater than one and has no other factors other than 1 and itself.

#---UMPIRE---

# Understand
"""
Examples:
Input: 3
Output: 5

- edge cases: what happens if we are given a negative number?
In this case I am assuming that we return 2 since 2 is the smallest prime number
"""

# Match
"""
- math/formula problems
- prime numbers
"""

# Plan
"""
1. make a simple base case if we are given a number < 0 (a negative number), return 2
2. make a for loop where we will count up from the number given
3. as we are counting up from the given number we check each next number to see if it is prime
4. if the next number is prime we simply return it. 

NOTE: to solve this we must break up the problem into two parts
1. making the base case, loop, and counter
2. make a way to determine when a number is prime
"""

# Implement
input_number = 23

# Finds the next prime number
def next_prime(given_number):
    found_next_prime = False
    #base case
    if given_number < 0:
        return 2
    else:
        while not found_next_prime:
            given_number +=1
            if is_prime(given_number):
                return given_number

# helper function
def is_prime(number):
    if number < 2:
        return False
    if number < 4:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(next_prime(input_number))

# Review
# the most challenging part of this problem is to determine if a number is prime or not
# after figuring out that part I was able to find the next smallest prime after a given number

# Evaluate
"""
time complexity: will depend on the input value but I will say worst case O(N)
space complexity: O(1)
"""