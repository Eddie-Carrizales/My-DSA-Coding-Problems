# Author:      Eddie F. Carrizales
# Date:        07/20/2022
# Problem Description: Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# ------UMPIRE------

# --Understand--
"""
My understanding: if an element appears in more than half the size of the array, then it is the majority element
(since it appears the most times)

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""
# --Match--
# - hashtable

# --Plan--
"""
1. create an empty hashtable
2. using a for loop add all the elements into the hashtable initialize with a count of 1
3. if any of the elements appears again increase the count
4. using another for loop check the value of each element
5. if the value if > len(arr)/2 set the key equal to the majority_element
6. finally, return the majority element
"""

# --Implement--

def majority_element(arr):
    value_dict = {}
    major_ele = -1

    # loop to add the array values into our dictionary/hashtable and keep count of how many elements we have
    for num in arr:
        if num not in value_dict:
            value_dict[num] = 1
        else:
            value_dict[num] += 1

    # loop to determine which of our elements in the hashtable is the majority element
    # from the problem description it is assumed that there will always be a majority element, but in the case that there is not, the function will return -1
    for key in value_dict:
        if value_dict[key] > len(arr) / 2:
            major_ele = key

    return major_ele

print(majority_element([2,2,1,1,1,2,2]))

# --Review--
# Code ran perfect on leetcode on the first run (even I am was impressed lol)

# --Evaluate--
# time complexity: O(N) insertion and retrieval for hashtable is O(1), traversing the array to put elements into hashtable O(N)
# space complexity: O(N) since we created a hashtable