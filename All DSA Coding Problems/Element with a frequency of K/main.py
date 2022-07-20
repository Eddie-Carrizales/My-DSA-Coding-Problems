# Author:      Eddie F. Carrizales
# Date:        07/19/2022
# Problem Description: Find the element that appears k number of times in an array.

# ---UMPIRE---

# --Understand--
"""
-We must find the element that appears k number of times in the array meaning if k = 2 we must find the element that
appears 2 times in the array and return that element

Example:
Input: [8, 7, 9, 6, 7, 5, 1], k = 2
Output: 7

- Edge cases questions:
- what happens if k is a number n but none of the elements appear that number of times in the array?
-A = In this case I will assume that I must return None, if the array is also empty or nothing matches the k value, I will also return None

- What happens if there are multiple values that appear k number of times in the array? example if 7 appears twice and 4 also appears twice?
-A =  I will assume that there will only be one value that appears k number of times, but there could also be a simple modification
to this question in which I can return every element that appears k number of times
"""

# --Match--
# - can be solved using Hashtable/dictionary

# --Plan--
"""
1. We will create an empty hashtable
2. we will create a for loop that will loop through each number in the given array
3. As we loop through the array, we will insert each element into our hashtable/dictionary and initialize it with a count of 1
4. if the element/number is already present in our hashtable then we will add 1 to its count
5. we will return the key that has the highest count in our hashtable
"""


# --Implement--

def find_k_number(arr, k):
    value_table = {}

    # loop to add values into the hashtable and count how many there are in the given array
    for num in arr:
        if num not in value_table:
            value_table[num] = 1  # adding value to table and initializing count to 1 if not in table
        else:
            value_table[num] += 1  # increasing the count of the value if already in the table

    # loop to return the value that has a count equal to k
    for key in value_table:
        if value_table[key] == k:
            return key


print(find_k_number([8, 7, 9, 6, 7, 5, 1], 2))

# --Review--
# The problem was straight forward and the code worked well.
# At the end for the edge cases for when k was larger than array the code will return None or
# when no values present k times to also returns None

# --Evaluate--
# Time complexity: O(N) since we have for loops operating on the given array
# Space complexity: O(N) since we created a hashtable to add the values and find the one with k appearances
