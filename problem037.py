"""
The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain prime at
each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from math import log10

from prime import Primes


def truncate_from_right(number):
    """
    >>> list(truncate_from_right(1234))
    [123, 12, 1]
    """
    while number > 10:
        number = number / 10
        yield number


def truncate_from_left(number):
    """
    >>> list(truncate_from_left(1234))
    [234, 34, 4]
    """
    while number > 10:
        number = number % (10 ** int(log10(number)))
        yield number


def main():
    """
    >>> main()
    748317
    """
    primes = Primes(10 ** 6)

    truncatable_prime = []
    for prime in primes:
        if not all([n in primes for n in truncate_from_right(prime)]):
            continue

        if not all([n in primes for n in truncate_from_left(prime)]):
            continue

        truncatable_prime.append(prime)

    print(sum(truncatable_prime) - sum([2, 3, 5, 7]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
