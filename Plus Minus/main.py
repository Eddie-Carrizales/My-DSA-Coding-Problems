# Author:      Eddie F. Carrizales
# Date:        07/09/2022

#----UMPIRE----
# Understand
"""
- We are given an array with positive numbers, negative numbers, and zeros

- We have to count the number of each of the values in the array and divide how many they are by the total numbers in the array
- Then we will print that division/ration for those positive, negative, and zero numbers up to 6 decimals

"""

# Match
"""
-iterating array
-hashtable (does not create much more space, only 3 things to store, for positive, negative, and zero)
"""

# Plan
"""
we will go with the hashtable as without it we still would need to create variables to keep track of positive, negatives, and zero

1. create a hashtable
2. use conditional to add elements to the hashtable if they are positive, negative or zero (this is how we keep count)
3. divide the value count of each by the length of the array
4. print the result of the division/ratio we got to 6 decimal places

"""

# Implement
arr = [1,1,0,-1,-1]

# initialize dict
values_dict = {"positive":0, "negative":0, "zero":0}

for value in arr:
    if value > 0:
        values_dict["positive"] += 1
    elif value < 0:
        values_dict["negative"] += 1
    else:
        values_dict["zero"] += 1

print("{:.6f}".format(values_dict["positive"]/len(arr)))
print("{:.6f}".format(values_dict["negative"]/len(arr)))
print("{:.6f}".format(values_dict["zero"]/len(arr)))

# Review
# code ran perfectly on hackerrank

# Evaluate
"""
Time complexity:
dictionary retrieval O(1)
The for loop will be O(N) depending on how many elements in the array

Thus our time complexity is O(N)

Space complexity:
The only space we have to create is for the dictionary
but since we only have three elements (positive, negative, and zero), this will be O(1) constant space

"""