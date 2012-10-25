"""
Euler published the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n**2  79n + 1601 was discovered, which
produces 80 primes for the consecutive values n = 0 to 79. The product of the
coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n**2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
"""

from itertools import count, product

from prime import Primes


def consecutive_primes_for(coefficient_a, coefficient_b, primes):
    """
    Comuptes the number of consecutive primes for the coefficients a and b.
    """
    count_consecutive_primes = 0
    for n in count(0):
        if (n ** 2 + coefficient_a * n + coefficient_b) not in primes:
            break
        count_consecutive_primes += 1
    return count_consecutive_primes


def main():
    """
    >>> main()
    -59231
    """
    primes = Primes(10 ** 6)
    # 'a' needs to be odd, otherwise for every odd 'n', the result is even
    a = xrange(-999, 1000, 2)
    # 'b' needs to be prime, otherwise for n=0 the formula won't give a prime
    b = (b for b in range(-999, 1000, 2) if b in primes)

    max_consecutive_primes = 0
    for (a, b) in product(a, b):
        consecutive_primes = consecutive_primes_for(a, b, primes)
        if consecutive_primes > max_consecutive_primes:
            product_of_coefficients = a * b
            max_consecutive_primes = consecutive_primes

    print (product_of_coefficients)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
