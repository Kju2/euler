from itertools import count
from math import log10
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

base = frozenset(["1","2","3","4","5","6","7","8","9"])

def digitsIn(n):
    return int(log10(n)) + 1
    pass

products = set([])
for x in range(2, 80):
    for y in count(x+1):
        z = x * y
        
        # is the count of digits not above 9
        if digitsIn(x) + digitsIn(y) + digitsIn(z) > 9:
            # can't be 1 trough 9 pandigital with more than 9 digits
            break
            pass

        # is x, y and z combind pandigital
        if base.issubset(str(x) + str(y) + str(z)):
            products.add(z)
            pass
        pass
    pass

print sum(products)
