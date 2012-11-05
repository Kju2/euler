"""
http://projecteuler.net/problem=92
"""

from collections import Counter
from itertools import combinations_with_replacement
from math import factorial
from operator import mul

from euler import int_to_list, list_to_int


def count_permutations_of(number):
    """
    >>> count_permutations_of("12345")
    120
    >>> count_permutations_of("1122345")
    1260
    """
    counted = Counter(number).most_common()

    numerator = factorial(sum([c[1] for c in counted]))
    denominator = reduce(mul, ([factorial(c[1]) for c in counted]), 1)

    return numerator // denominator


def main():
    """
    >>> main()
    8581146
    """
    chains_that_arrive_at_89 = 0
    for number in combinations_with_replacement(xrange(10), 7):
        n = list_to_int(number)
        while n != 1 and n != 89 and n != 0:
            n = sum([d ** 2 for d in int_to_list(n)])

        if n == 89:
            chains_that_arrive_at_89 += count_permutations_of(number)

    print(chains_that_arrive_at_89)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
