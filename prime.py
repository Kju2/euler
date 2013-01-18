"""
prime - a collection of prime number related functions
"""

from collections import Counter
from math import sqrt


class Primes(tuple):
    """Primes is a container class for prime numbers. It behaves like range in
    it construction.
    """

    __solts__ = ['primes_set']

    def __new__(cls, start, stop=None):
        if stop is None:
            stop = start
            start = 0

        instance = tuple.__new__(cls, cls.primes(start, stop))
        instance.primes_set = frozenset(instance)
        return instance

    @classmethod
    def primes(cls, start, stop):
        """primes returns a list of primes from the lower bound (start) to
        the upper bound (stop - exclusive) using the sieve of Eratosthenes.
        The result is sorted.

        >>> Primes.primes(0, 0)
        []
        >>> Primes.primes(0, 2)
        []
        >>> Primes.primes(0, 3)
        [2]
        >>> Primes.primes(3, 7)
        [3, 5]
        >>> Primes.primes(0, 42)
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
        """
        if stop <= 2 or start > stop:
            return []

        sieve_bound = int(stop // 2)
        sieve = list(range(sieve_bound))
        cross_limit = int((sqrt(stop) - 1) / 2)

        for i in range(cross_limit + 1):
            if sieve[i]:  # 2 * i + 1 is prime, mark multiples
                for j in range(2 * i * (i + 1), sieve_bound, 2 * i + 1):
                    sieve[j] = 0

        return [p for p in [2] + [2 * p + 1 for p in sieve if p] if p >= start]

    def __contains__(self, item):
        """__contains__ returns True if the number is a prime, False otherwise.

        >>> primes = Primes(42)
        >>> [n for n in range(42) if n in primes]
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
        """
        return item in self.primes_set

    def __delitem__(self, key):
        pass

    def  __setitem__(self, key, value):
        pass

    def factors_of(self, number):
        """factors_of calculates the prime factors of the given number. The
        square root of the number has to be less than the biggest prime number
        in the primes list. For a number less than 2 an empty list is returned.

        >>> primes = Primes(1000)
        >>> map(primes.factors_of, [1, 14, 644])
        [Counter(), Counter({2: 1, 7: 1}), Counter({2: 2, 23: 1, 7: 1})]
        >>> primes = Primes(10)
        >>> primes.factors_of(1234)
        Traceback (most recent call last):
            ...
        IndexError: not enough primes calculated
        """
        prime_factors = Counter([])

        if number < 2:
            return prime_factors

        if int(sqrt(number) + 1) > self[-1]:
            raise IndexError("not enough primes calculated")

        while number not in self.primes_set:
            for prime in self:
                if number % prime == 0:
                    number = number / prime
                    prime_factors[prime] += 1
                    break

        prime_factors[number] += 1
        return prime_factors


def is_prime(number):
    """
    is_prime returns True if the number is prime, False otherwise.

    >>> [n for n in range(42) if is_prime(n)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    """
    if number < 2:
        return False
    elif number < 4:  # 2, 3 are prime
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    elif number < 9:  # 5, 7 are prime
        return True
    else:
        for i in range(5, int(sqrt(number) + 1), 6):
            if number % i == 0 or number % (i + 2) == 0:
                return False

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
