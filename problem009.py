"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
"""

from math import sqrt


def pythagorean_triplets():
    """
    pythagorean_triplets yields pytagorean triplets in order of increasing c.
    """
    c = 4
    while True:
        c += 1
        a_min = int(sqrt(2 * c - 1))
        a_max = int(c / sqrt(2)) + 1

        for a in range(a_min, a_max):
            b = int(sqrt(c * c - a * a))
            if a ** 2 + b ** 2 == c ** 2:
                yield (a, b, c)


def main():
    """
    >>> main()
    31875000
    """
    a, b, c = next((pt for pt in pythagorean_triplets() if sum(pt) == 1000))
    print(a * b * c)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
