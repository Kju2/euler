"""
The number, 197, is called a circular prime because all rotations of
the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from euler import int_to_list, list_to_int
from prime import Primes


def rotate(number):
    """ return all rotations of this number"""
    digits = int_to_list(number)
    for _ in range(len(digits)):
        yield list_to_int(digits)
        digits.append(digits.pop(0))


def main():
    """
    >>> main()
    55
    """
    even_digits = frozenset([d for d in range(0, 10, 2)])

    primes = Primes(10 ** 6)

    count = 1  # for the prime 2
    for prime in primes:
        # Exculde all primes that have an even digit in it.
        if not even_digits.isdisjoint(int_to_list(prime)):
            continue

        if all((rotated_prime in primes for rotated_prime in rotate(prime))):
            count += 1

    print(count)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
