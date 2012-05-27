"""
prime - a collection of prime number related functions
"""

from math import sqrt

_PRIMES_MAX = 2
_PRIMES_CACHE = [2]
_PRIMES_SET_CACHE = set(_PRIMES_CACHE)


def _ensure_primes_up_to(limit):
    """ _ensure_primes_up_to is a helper function ensure the prime number
    caches are initalized.
    """
    global _PRIMES_MAX
    global _PRIMES_CACHE
    global _PRIMES_SET_CACHE
    if _PRIMES_MAX < limit:
        _PRIMES_CACHE = primes_up_to(limit * 10)
        _PRIMES_SET_CACHE = set(_PRIMES_CACHE)
        _PRIMES_MAX = max(_PRIMES_CACHE)


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


def prime_factors_of(number):
    """
    >>> prime_factors_of(0)
    []
    >>> prime_factors_of(1)
    []
    >>> prime_factors_of(2)
    [2]
    >>> prime_factors_of(14)
    [2, 7]
    >>> prime_factors_of(644)
    [2, 2, 7, 23]
    """

    prime_factors = []

    if number < 2:
        return prime_factors

    _ensure_primes_up_to(number)

    while number not in _PRIMES_SET_CACHE:
        for prime in _PRIMES_CACHE:
            if number % prime == 0:
                number = number / prime
                prime_factors.append(prime)
                break

    prime_factors.append(number)
    return prime_factors


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

    sieve_bound = int(limit // 2)
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
