"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes factors.
What is the first of these numbers?
"""

from itertools import count

from prime import Primes


def main():
    """
    >>> main()
    134043
    """
    primes = Primes(10 ** 6)

    min_consecutive_valid_numbers = 4
    distinct_prime_factors = 4

    # next number after lower bound has to have at least distinct_prime_factors
    # of odd primes as prime factors
    lower_bound = (3 * 5 * 7 * 11) - 1

    number = 0
    consecutive_valid_numbers_count = 0

    for number in count(lower_bound):
        if consecutive_valid_numbers_count == min_consecutive_valid_numbers:
            break

        if len(set(primes.factors_of(number))) == distinct_prime_factors:
            consecutive_valid_numbers_count += 1
        else:
            consecutive_valid_numbers_count = 0

    # print first number of the consecutive numbers
    print(number - distinct_prime_factors)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
