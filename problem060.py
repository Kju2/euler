"""
http://projecteuler.net/problem=60
"""
import sys

from euler import list_to_int
from prime import Primes

PRIME_INDEX_LIMIT = 1250  # limit primes to 4 digits, arbitrary limit
LEN_PRIME_SET = 5


def main():
    """
    >>> main()
    26033
    """
    primes = Primes(10 ** 8)

    remarkable_primes = []
    remarkable_primes_min_sum = sys.maxsize

    i = 0
    while True:
        if i > PRIME_INDEX_LIMIT:
            last_added_prime = list_to_int(remarkable_primes.pop())
            i = primes.index(last_added_prime) + 1
            if len(remarkable_primes) == 0 and i == PRIME_INDEX_LIMIT:
                break

        new_prime = str(primes[i])
        new_prime_is_remarkable = True
        for prime in remarkable_primes:
            if list_to_int(new_prime + prime) not in primes:
                new_prime_is_remarkable = False
                break

            if list_to_int(prime + new_prime) not in primes:
                new_prime_is_remarkable = False
                break

        if new_prime_is_remarkable:
            remarkable_primes.append(new_prime)
            if len(remarkable_primes) == LEN_PRIME_SET:
                primes_sum = sum((int(p) for p in remarkable_primes))
                if primes_sum < remarkable_primes_min_sum:
                    remarkable_primes_min_sum = primes_sum

        i += 1

    print(remarkable_primes_min_sum)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
