from itertools import *
from math import factorial
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
digits = map(str, range(10))
factorials = map(factorial, range(0, 10))

summe = -3  # 1 && 2 which are not counted
for num_digits in range(1, 8):  # upper limit: 7 * 9! < 10**7
    for number in combinations_with_replacement(digits, num_digits):
        factorial_sum = sum(map(lambda x: factorials[int(x)], number))
        if sorted(str(factorial_sum)) == list(number):
            summe += factorial_sum
            pass
        pass
    pass

print summe
