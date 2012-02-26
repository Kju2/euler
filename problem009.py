from math import sqrt
from itertools import dropwhile
"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def pythagorean_triplets():
    c = 4
    while True:
        c += 1
        minA = int(sqrt(2*c -1))
        maxA = int(c / sqrt(2))+1

        for a in range(minA, maxA):
            b = int(sqrt(c*c - a*a))
            if a**2 + b**2 == c**2:
                yield (a, b, c)
                pass
            pass
        pass
    pass

(a, b, c) = next(dropwhile(lambda (a, b, c): a+b+c != 1000, pythagorean_triplets()))
print a * b * c
