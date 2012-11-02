"""
http://projecteuler.net/problem=297
"""

from itertools import takewhile

from euler import fib


def main():
    """
    >>> main()
    2252639041804718029
    """
    limit = 10 ** 17

    fibs = list(takewhile(lambda x: x < limit, fib()))
    zrts = {1: 0}

    def sum_z(number):
        """
        sum_z computes the sum of the zeckendorf representations terms up
        to the given number.
        """
        if number not in zrts:
            f = max((f for f in fibs if f < number))
            zrts[number] = number - f + sum_z(number - f) + sum_z(f)
        return zrts[number]

    print(sum_z(limit))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
