# Author:      Eddie F. Carrizales
# Date:        07/20/2022
# Problem Description: Given a roman numeral, convert it to an integer.
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four. The same principle applies to the number nine,
which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Constraints:
1 <= s.length <= 15

s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').

It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

# ------UMPIRE------

# --Understand--

# My insights: seems like a complex problem due to subtraction edge cases, so I will first try to break the problem into two pieces
# and solve each piece until I have covered both cases and solved it.
"""
Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

# --Match--
# - hashtable/dictionary problem (we will need fast access times)

# --Plan--
"""
1. initialize a hashtable/dictionary with the roman symbols as keys and equivalent numbers as values.
2. make sure to make the input string uppercase, in case the input string is entered in lower case
3. we will traverse the string one char at a time, but make sure to check the prev char in case it makes a subtraction
4. as we traverse/loop through the string, we will add or subtract the values to a result variable which will be the sum of all roman char values
5. we will then return that sum result
"""

# --Implement--
# My implementation:
def roman_to_integer(s):
    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0

    s = s.upper() # makes string all uppercase just in case the roman numeral was entered in lowercase (line not required on leetcode)

    for i in range(0, len(s)):
        # As we traverse from left to right we will check to see if the prev char value is less than our current char value,
        # if it is, then that means we must subtract that from our result. However, since we have already added that prev char value
        # we must subtract it twice, once for the previous addition and once for the current subtraction thus the multiplication * 2
        # Note: the and with the i-1 != -1 condition is to prevent wrapping to the end of string when we are in i = 0 (first char of string)
        if roman_numerals[s[i-1]] < roman_numerals[s[i]] and i-1 != -1:
            result += roman_numerals[s[i]] - 2 * roman_numerals[s[i-1]]
        else:
            result += roman_numerals[s[i]]

    return result

print(roman_to_integer("MCMXCIV"))

# --Review--
# -Initially struggled to implement this solution as I kept going out of bounds and the subtractions were
# confusing due to the positions of the roman symbols.
# -Eventually I was able to figure it out on my own, but I am sure that there are better/ easier to understand
# implementations online.
# -My solution also ran perfectly on leetcode and is faster than 73% in runtime time and better than 76% in memory.
# -Maybe a better way to implement it to avoid the multiplication would have been to traverse from right to left and
# starting at position i = -2 to avoid the extra i-1 != -1 condition

# --Evaluate--
# Time Complexity: As we can see in the given constrains for the problem, the maximum length given for the string can
# be of only 15 characters, thus we can argue that the for loop can only have a worst time complexity of O(15) which is
# basically O(1) time.

# Space Complexity: In terms of space complexity, we are using a hashtable/dictionary for the Roman symbols and their values
# However, since there are only 7 symbols the worst case is O{7} which is basically O(1) time.