# Author:      Eddie F. Carrizales
# Date:        07/19/2022
# Problem Description: Given an unsorted array of integers, we want to find the length of the longest subsequence such
# that elements in the subsequence are consecutive integers. The consecutive numbers can be in any order.

# ------UMPIRE------

# --Understand--
"""
My understanding: We are given an array of unsorted integers, we have to find the longest subsequence of numbers that are
consecutive in this given array. As we can see in the example below, in the given array we have:
-[9, 10] since they are consecutive (the length of this subsequence is 2; only two numbers)
-[1,2,3,4] since they are consecutive (the length of this subsequence is 4; we have 4 numbers)
and that is it, all the other numbers are not consecutive

-Also I will assume that I must only return the length of the LCS since the problem only shows the length as the output.

Input: [1, 9, 3, 10, 4, 20 , 2]
Output: 4
[1, 3, 4, 2] is the longest subsequence of consecutive elements.

Edge cases:
Can we have consecutive numbers going in reverse?
-Yes, but the logic will be essentially the same, thus I will simply return them from least to greatest

What happens if there are any duplicates in the given array?
-We only count a number once, so in the case of the example above, if there were another 4 in the given array, we would
still only return a length of 4 since it only counts once.
"""

# --Match--
# - can be solved using a set (most efficient solution, what I will use)
# - can also be solved using sort and adding values into another array if the next consecutive value is found

# --Plan--
"""
1. create an empty set
2. add all of the elements from the given array into our set
3. create a for loop to go through all of the values in the given array
4. Then if the current value in the array-1 is not in our set, this mean that there is no number previous to it that is consecutive
5. this means, that it is the starting position for a consecutive subsequence
6. Thus, we will start at each starting position of a consecutive subsequence and add +1 in a while loop until the subsequence ends
7. the while loop/subsequence will end if the element+1 is not in the set s.
8. Once it ends, we subtract our original number to get the resulting length of the subsequence and we set that number as the max length of subsequence
9. after repeating steps 5-8 for all starting positions we will have the max longest consecutive subsequence since it will only update if it found a longer subsequence
"""

# --Implement--
def longest_consecutive_subsequence(arr):

    s = set()
    longest_subsequence = 0

    for num in arr:
        s.add(num)

    for i in range(len(arr)):
        # if the current number in the array decreased by 1 is not in our set, this mean that it is the starting
        # element of a subsequence because there are no numbers in our set that are previous to it.
        # so once this condition is true we start counting the length of the subsequence starting at these positions.
        if arr[i]-1 not in s:

            elem = arr[i] # we set our element to one of the staring positions of one subsequence

            # we walk through the array from our starting position.
            # Ex: if 1 is our starting position we move to 2, then 3, then 4 until there is no other consecutive number
            while elem in s:
                elem += 1

            # once we traversed the while loop and kept adding 1 until the element was not in s, this means the while
            # loop ends, and we have found the length of our subsequence.

            # How it works:             (starting element + added positions in while loop)   -   starting element
            #                                   \                           /                          |
            # longest_subsequence =                        elem                              -      arr[i]
            if elem-arr[i] > longest_subsequence:
                longest_subsequence = elem-arr[i]

        return longest_subsequence

print(longest_consecutive_subsequence([1, 9, 3, 10, 4, 20, 2]))

# --Review--
# If anyone else reads this code beside me, I apologize for the long explanation.

# --Evaluate--
# Time complexity: O(N) since we only traverse an array of size N
# Space complexity: O(N) since we create a set of size N

