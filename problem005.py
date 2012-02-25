from itertools import count
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# divisible by  2 if step is 2
# divisible by  3 if step is 3*2
# divisible by  4 if step is 3*2**2
# divisible by  5 if step is 5*3*2**2
# divisible by  6 because of 2 and 3
# divisible by  7 if step is 7*5*3*2**2
# divisible by  8 if step is 7*5*3*2**3
# divisible by  9 if step is 7*5*3*3*2**3
# divisible by 10 if step is 7*5*3*3*2**4
# divisible by 11 if step is 11*7*5*3*3*2**4
# divisible by 11 if step is 11*7*5*3*3*2**4
# divisible by 12 because of 2 and 6
# divisible by 13 if step is 13*11*7*5*3*3*2**4
# divisible by 12 because of 7 and 2
# divisible by 15 because of 5 and 3
# divisible by 16 because of 8 and 2
# divisible by 17 if step is 17*13*11*7*5*3*3*2**4
# divisible by 18 because of 9 and 2
# divisible by 19 if step is 19*17*13*11*7*5*3*3*2**4
# divisible by 20 because of 5 and 2

print 19*17*13*11*7*5*3*3*2**4
