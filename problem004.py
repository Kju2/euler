from itertools import *
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrom(n):
    n_str = str(n)
    return n_str == n_str[::-1]
    pass

maxPalindrom = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        product = i * j
        if is_palindrom(product) and product > maxPalindrom:
            maxPalindrom = product
            pass
        pass
    pass
print maxPalindrom
