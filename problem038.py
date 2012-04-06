from itertools import count
from math import log10
"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192  1 = 192
192  2 = 384
192  3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


base = frozenset(["1", "2", "3", "4", "5", "6", "7", "8", "9"])


def is_pandigital(n):
    """ n is a number as a string """
    if len(n) != len(base):
        return False
        pass

    if not base.issubset(str(n)):
        return False
        pass

    return True
    pass


max_pandigital_number = 0

for multiplicand in count(2):
    #  since the multiplier must be at least 2 we can stop when the
    #  multiplicand * 1 and multiplicand * 2 together have more than 9 numbers
    if int(log10(multiplicand)) + int(log10(2 * multiplicand)) + 2 > len(base):
        break
        pass

    product = str(multiplicand)
    for multiplier in count(2):
        product += str(multiplicand * multiplier)

        if is_pandigital(product) and max_pandigital_number < product:
            max_pandigital_number = product
            pass
        elif len(product) > len(base):
            break
            pass
        pass
    pass

print max_pandigital_number
