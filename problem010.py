"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from prime import Primes


def main():
    """
    >>> main()
    142913828922
    """
    limit = 2 * 10 ** 6
    primes = Primes(limit)
    print(sum(primes))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
