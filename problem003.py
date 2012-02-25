from itertools import *

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

n = 600851475143

def last_factor_of(n):
    factors = chain([2], count(3,2))
    lastFactor = 1
    while n > 1:
        factor = factors.next()
        if n % factor == 0:
            lastFactor = factor
            n = n / factor
            while n % factor == 0:
                n = n / factor
                pass
            pass
        pass
    return lastFactor

print last_factor_of(n)
