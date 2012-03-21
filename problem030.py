from itertools import count, ifilter
"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

power = 5
limit = ifilter(lambda i: 10**i > i*(9**power), count(1)).next() * 9**power + 1

def sum_of_X_powers_of_the_digits_of(n):
    return reduce(lambda x, y: x + int(y)**power, str(n), 0)
    pass

print sum(filter(lambda n: n == sum_of_X_powers_of_the_digits_of(n), range(2, limit)))
