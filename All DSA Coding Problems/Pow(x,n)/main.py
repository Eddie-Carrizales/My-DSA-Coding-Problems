# july 18

# Problem description: Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# ---UMPIRE---

# Understand
"""
example:
Input: x = 2.00000, n = 10
Output: 1024.00000

Can you think of any edge cases?
- when n is negative or when x is negative
- not really edge cases, but I noticed that they have up to 5 values after the decimal,
so we have to consider that in our code.
"""

# Match
# -math problem
# -recursion

# Plan
#implementation 2 since it is the most efficient
"""
1. For this problem we will use recursion
2. the way we will do this to make it more efficient is to use a divide and conquer approach
3. for example:
    if we have 2^10 = same as 2*2*2*2*2*2*2*2*2*2
4. However, we can cut all of this work in half by doing 2*2*2*2*2 = 2^5 and just multiplying by itself
5. likewise, instead of doing 2^5 we can instead do 2^2 and multiply by itself = 2^4 then since 5 is odd we multiply by 1 more 2 giving us 2^4 * 2^4 * 2 = 2^5
6. Thus to solve this problem with the least amount of work possible we will use this implementation
7. first we need a base case since this is a recursive solution
8. our base case will be if n == 0 we simply return 1 since everything to the power of 0 is 1
9. also if n == 1, we simply return that number since anything to the power of 1 is itself
10. next we will use floor division and divide n by 2 this essentially halfs our work
11. then if n is odd we will multiply by 1 more x, if it is even, then just by 1 (meaning no change)
12. all of this will be returned and be recursively called until n reaches the base case
13. the only edge case we must account is when n or x is negative.
14. when x is negative we dont have to do anything since the math will eliminate the sign
15. when n is negative we must put our x in the denominator since this is an algebra rule
16. so we just add one more case where we set x = 1/x when n == -1
"""

#-------Implement-------
given_x = 2
given_n = 5

# Implementation 1
# (works for smaller numbers but exceeds recursion depth with larger numbers since its inefficient)
def power(x: float, n: int) -> float:
    if n == 0:
        return 1

    if n < 0:
        return 1/x

    return x * power(x, n - 1)

print(format(power(given_x, given_n), ".5f"))

# Implementation 2 (does less work than implementation1 and does not exceed recursion depth)
def myPow(x, n):
   if n == 0:
       return 1

   if n == 1:
       return x

   if n == -1:
       return 1 / x

                # 2, 5//2   n will become 2
   result = myPow(x, n // 2)

        #  2^2  *    2^2  *        2              give us 2*2  2*2  *2  = 2^5
   return result * result * (x if n % 2 else 1)

print(format(myPow(given_x, given_n), ".5f"))

# Review
# implementation 2 worked better than implementation 1
# it was important to understand and view the pattern of repeated work to find a better solution


# Evaluate
# implementation 2
# time complexity: O(log N) since we are seeing how many times n is divided by x until it became 1
# space complexity: O(1) no additional data structures were used only a single variable