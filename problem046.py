"""
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""

from math import sqrt
from itertools import count

from euler import is_even, is_integer, is_odd, is_prime, primes_up_to


def is_goldbach_number(number):
    """
    >>> is_goldbach_number(9)
    True
    >>> is_goldbach_number(15)
    True
    >>> is_goldbach_number(5777)
    False
    """
    for prime in primes_up_to(number):
        step = number - prime
        if is_even(step):
            step = sqrt(step / 2)
            if is_integer(step):
                return True

    return False


def main():
    """
    cn = p + 2 * s ^ 2 is transformed to s = sqrt((cn - p) / 2) and if s is
    an integer and p a prime, then cn is buildable by the formula, otherwise
    not.
    >>> main()
    5777
    """
    composite_number = (n for n in count(9) if is_odd(n) and not is_prime(n))
    counter_example = (cn for cn in composite_number
                            if not is_goldbach_number(cn))
    print((next(counter_example)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
