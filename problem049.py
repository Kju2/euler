"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways:

(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

from prime import Primes


def is_permutation(original, new):
    """is_permutation returns True if the two numbers are permutations of each
    other. That means they have the same digits in the same amount. Otherwise
    is_permutation returns False.

    >>> is_permutation(2392, 2239)
    True
    >>> is_permutation(2392, 239)
    False
    """
    original = list(str(original))
    original.sort()

    new = list(str(new))
    new.sort()

    return original == new


def main():
    """
    >>> main()
    296962999629
    148748178147
    """
    lower_limit = 1000
    upper_limit = 10000

    primes = Primes(lower_limit, upper_limit)

    candidates = set(primes)
    while len(candidates) > 0:
        prime = candidates.pop()
        num2 = prime + 3330
        num3 = num2 + 3330

        if (
            num2 in primes and is_permutation(prime, num2) and
            num3 in primes and is_permutation(prime, num3)
        ):
            print(str(prime) + str(num2) + str(num3))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
