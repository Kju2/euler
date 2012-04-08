"""
We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from euler import is_prime, list_to_int
from itertools import permutations

# 8 and 9-pandigital numbers are devisable by 3 therefore aren't prime
SEVEN_DIGIT_PANDIGITAL = [list_to_int(p) for p in permutations(range(1, 8))]

print(max([p for p in SEVEN_DIGIT_PANDIGITAL if is_prime(p)]))
# 7652413
