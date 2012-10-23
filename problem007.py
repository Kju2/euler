"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""

from prime import Primes


def main():
    """
    >>> main()
    104743
    """
    index = 10001
    print(Primes(10 ** 6)[index - 1])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
