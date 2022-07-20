#july18

# Problem Description: Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order

#-----UMPIRE-----

# Understand
"""
Examples:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

    Input: nums = [1]
    Output: [[1]] # lists of lists

Do I understand the problem?
-Yes, given an array of distinct integers, I have to return all of the possible combinations of those integers
- the answer can be returned in any order
- given an array of distinct 3 values, our output will have 3 x 2 x 1 = 6 possible permutations
- possible permutations = n!

Can you think of any Edge Cases?:
-when given a single value we must return as a list of lists [[]]
"""

# Match
# - math problem
# - recursion

# Plan
"""
1. We have to break up the problem into smaller and smaller parts
2. if we start with [1,2,3] we want to pop the first element and look at the permutations of [2,3] by doing a recursive call
3. then to get to the permutations of [2,3] we want to pop the first element and do a recursive call to look at the permutations of 2 and of 3
4. then we notice we have reached an array length of 1 for both 2 and 3, so this will be our base case
5. now we start working back up and we append the previous value we pop ed, giving us [2,3] and [3,2]
6. from there, we work our way up once more and for each permutation, append the one we removed before (1) to the end
7. this gives us [2,3,1] and [3,2,1]
8. this will be the main play, except that we will use a nested for loop repeat this for every permutation inside our initial array to get all possible permutations
"""

# Implement
input_nums = [1,2,3]

def permute(nums):
    result = []

    # base case
    if len(nums) == 1:
        return [nums.copy()]

    for i in range(len(nums)):
        n = nums.pop(0) # remove the first element in the array
        permutations = permute(nums) # recursive call to send the remaining array/ permutations further down until they reach the base case

        # for every single permutation in the permutations we have
        for perm in permutations:
            perm.append(n) # append at the end of each permutation the number we initially removed

        result.extend(permutations) # add our permutation to our result array
        nums.append(n) # add back the first element we initially removed

    return result

print(permute(input_nums))

# Review
# this problem was complicated in the sense that one must understand how to break the problem up into sub parts before building
# it back up piece by piece

# Evaluate
# time complexity: O(N*N!) because O(N) from the for loop and O(N!) for the nested for loop that appends to each permutation
# space complexity: O(N!) since we are storing n! permutations