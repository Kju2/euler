"""
We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from itertools import permutations

from euler import list_to_int
from prime import is_prime


def main():
    """
    >>> main()
    7652413
    """
    # 8 and 9-pandigital numbers are devisable by 3 therefore aren't prime
    pandigital_numbers = [list_to_int(p) for p in permutations(xrange(1, 8))]

    print(max([p for p in pandigital_numbers if is_prime(p)]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
