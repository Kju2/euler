"""
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""

from itertools import count


def main():
    """
    >>> main()
    142857
    """
    for i in count(1):
        c = sorted(str(i))
        if all((c == sorted(str(i * x)) for x in (2, 3, 4, 5, 6))):
            print i
            return


if __name__ == "__main__":
    import doctest
    doctest.testmod()
