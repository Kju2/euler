"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from prime import Primes


def main():
    """
    >>> main()
    6857
    """
    number = 600851475143

    primes = Primes(10 ** 6)

    print(max(primes.factors_of(number)))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
