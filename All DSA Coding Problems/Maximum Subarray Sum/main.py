# Author:      Eddie F. Carrizales
# Date:        07/19/2022
# Problem description: Given an array of positive numbers and a positive number "k",
# find the maximum sum of any subarray of size "k"

# ---UMPIRE---
# Understand
"""
Example 1:
Input : [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: subarray with maximum sum is [5, 1, 3] because 5 + 1 + 3 = 9

edge cases: what happens if the value of k is larger than our array?
- In this case we will return -1

Example 2:
Input: [2, 3, 4, 1, 5], k = 6
Output: -1
"""

# --Match--
# I believe there are several ways to solve this problem, I will use sliding window method

# --Plan--
"""
1. create an empty list and a max_sum variable equal to 0
2. create the special condition where if k is greater than the length of our array, then simply return -1
3. Now, we will create a for loop that will iterate through each number in the given array
4. We will begin appending each of the numbers into our new list
5. if the length of our new list becomes greater than our sliding window (i.e greater than k), then we remove the first element of our list
6. this will allow us to keep sliding through our list with a window of size k until we reach the end
7. finally, as we will add all of the elements present inside our window and compare them to max_sum variable
8. if the sum of all the elements present inside our window is greater than sum we simply continue, else we set max_sum equal to that sum.
9. at the end we return that max_sum
"""

# --Implement--
def getMaxSum(arr, k):
    # Write your code here
    max_sum = 0
    list = []

    # edge case when the value of k is greater than the length of our array
    if k > len(arr):
        return -1

    for num in arr:
        # add values to our list
        list.append(num)

        # if the length of our current list is greater than our sliding window we remove the front element to keep sliding
        if len(list) > k:
            list.pop(0)

        # if the sum of our window is greater, we make that our max_sum
        if sum(list) > max_sum:
            max_sum = sum(list)

    return max_sum

print(getMaxSum([2, 3, 4, 1, 5], 2))

# --Review--
# Initially I wanted to use a hashtable to keep track of the elements, but realized it was simpler and faster
# to implement a sliding window approach

# --Evaluate--
# time complexity: O(N*M), where N is for traversing the for loop
# and M is for the sum of the elements in the list, the number of M elements will depend on the value of k
# Space complexity: O(N), since we are creating a list/array to store the values

# Overall, I am sure there is a way to optimize this code to sum as we loop making the time complexity O(N) or
# to avoid creating another array making the space complexity O(1)
