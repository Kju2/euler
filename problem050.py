"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from prime import Primes


def main():
    """
    >>> main()
    997651
    """
    upper_bound = 10 ** 6
    primes = Primes(upper_bound)

    max_prime = 0
    longest_sequence = 1

    # first and last are the indices for the list of primes. They tell where
    # to start and stop to build the sum.
    for first in range(len(primes)):
        if sum(primes[first:(first + longest_sequence)]) > upper_bound:
            # it is no longer possible to get a sum with more primes and
            # stay below the upper bound
            break

        for last in range(first + longest_sequence, len(primes)):
            result = sum(primes[first:last])

            if result > upper_bound:
                break

            if result in primes:
                max_prime = result
                longest_sequence = last - first

    print(max_prime)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
