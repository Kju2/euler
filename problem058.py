"""
http://projecteuler.net/problem=58
"""

from itertools import count

from prime import is_prime


def main():
    """
    >>> main()
    26241
    """
    i = 1
    primes = 0.0
    numbers = 1.0
    for layer in ([x] * 4 for x in count(2, 2)):
        for side in layer:
            i += side
            if is_prime(i):
                primes += 1

        numbers += 4
        if primes / numbers < 0.10:
            print(layer[0] + 1)
            return


if __name__ == "__main__":
    import doctest
    doctest.testmod()
