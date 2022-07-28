# Author:      Eddie F. Carrizales
# Date:        07/28/2022
# Problem Description:
"""
Implement a method to find the number of occurrences of any given word in a book.
A word is represented as a string and a book is represented as an array / list of strings.

Optimize the method to be called multiple times.

Follow-up questions:
-Will the given string always be found in the given array?
A = There may be cases when it is not, if it is not, then return 0 or none.

- Are the words in the array case-sensitive? (Ex: is hi same as Hi?)
A = There may be words with different case, but you should still count them if they use the same letters (do not be case-sensitive)

- What if there are spaces in the string or between letters?
A = Ignore all leading or trailing spaces "   hi" == " Hi   "
"""
# ------UMPIRE------

# --Understand--
"""
Input: [" The", "dog", "jumped", "in", "the", "dog", "house"], "dog"
Output: 2
"""

# --Match--
# - hashtable problem

# --Plan--
"""
1. create an empty hashtable
2. iterate the given array and store the string in the dictionary and count
3. Used the given string as the key and return the vale in the dictionary for that given string.
"""

# --Implement--
# Leetcode input
given_arr = [" The", "dog", "jumped", "in", "the", "dog", "house"]
given_string = "dog"

def word_frequency(arr, s):
    word_dict = {} # create empty dictionary

    # process given string to remove empty spaces and to make it lowercase
    s = s.lower()
    s = s.strip()

    # process every word in the array to remove empty spaces and make them lowercase
    for i in range(0, len(arr)):
        arr[i] = arr[i].lower()
        arr[i] = arr[i].strip()
    print(arr)

    # add each word to the hashtable and increase the count if there are duplicates of the word
    for word in arr:
        if word not in word_dict:
            word_dict[word] = 1 # set initial count to 1
        else:
            word_dict[word] += 1 # increase count by 1

    # returns the value of the string in the dict (i.e, the count)
    if s in word_dict:
        return word_dict[s]
    else:
        return 0


print(word_frequency(given_arr, given_string))

# --Review--
# Simple to implement and works with edge cases where there are trailing spaces or different letter case words
# Also, if the word is not found, it will return 0

# --Evaluate--
# Time complexity: O(N)
# Space complexity: O(N)