"""
We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from euler import is_int_pandigital, primes_up_to


# 8 and 9-pandigital numbers are devisable by 3 therefore aren't prime
print(max([p for p in primes_up_to(10 ** 7) if is_int_pandigital(p)]))
