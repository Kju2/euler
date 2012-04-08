"""
euler - a collection of functions useful in more than one euler problem
"""

from math import log10, sqrt


def is_int_pandigital(number):
    """
    is_int_pandigital tests if a int number is pandigital. A pandigital number
    uses numbers 1 trough to the count of adigits of the number.

    >>> is_int_pandigital(1)
    True
    >>> is_int_pandigital(4)
    False
    >>> is_int_pandigital(1234)
    True
    >>> is_int_pandigital(36932)
    False
    """
    digits = int(log10(number) + 1)
    if digits > 9:
        return False

    base = [False] * digits

    while number > 0:
        number, rest = divmod(number, 10)
        if rest > digits:
            return False
        base[rest - 1] = True

    return all(base)


def primes_up_to(limit):
    """
    primes_up_to returns a list of primes up to the given limit using
    the sieve of Eratosthenes.

    >>> primes_up_to(0)
    []
    >>> primes_up_to(2)
    []
    >>> primes_up_to(3)
    [2]
    >>> primes_up_to(7)
    [2, 3, 5]
    >>> primes_up_to(42)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    """

    if limit <= 2:
        return []

    sieve_bound = limit // 2
    sieve = list(range(sieve_bound))
    cross_limit = int((sqrt(limit) - 1) / 2)

    for i in range(cross_limit + 1):
        if sieve[i]:  # 2 * i + 1 is prime, mark multiples
            for j in range(2 * i * (i + 1), sieve_bound, 2 * i + 1):
                sieve[j] = 0

    return [2] + [2 * p + 1 for p in sieve if p]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
