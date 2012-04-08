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


def is_prime(number):
    """
    is_prime returns True if the number is prime, False otherwise.

    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(36)
    False
    >>> is_prime(41)
    True
    >>> [n for n in range(42) if is_prime(n)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    """
    if number < 2:
        return False

    for i in range(2, int(sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


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
    >>> all(filter(is_prime, primes_up_to(10 ** 5)))
    True
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


def list_to_int(digits):
    """
    list_to_int - joins a list of digits to an integer. The digits can be
    strings or ints. For base 10 numbers. Efficient up to 30 digits, then
    a map-approach is faster.

    >>> list_to_int('0')
    0
    >>> list_to_int([0])
    0
    >>> list_to_int('2904234')
    2904234
    >>> list_to_int([2, 9, 0, 4, 2, 3, 4])
    2904234
    >>> list_to_int((2, 9, 0, 4, 2, 3, 4))
    2904234
    >>> list_to_int((2, 9)) == int(''.join(map(str, (2, 9))))
    True
    >>> list_to_int((4, 2)) == int(''.join(('4', '2')))
    True
    """
    number = 0

    for digit in digits:
        number *= 10
        number += int(digit)

    return number


if __name__ == "__main__":
    import doctest
    doctest.testmod()
