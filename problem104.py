"""
http://projecteuler.net/problem=104
"""

from euler import count_digits_in, fib, int_to_list


def main():
    """
    >>> main()
    329468
    """
    base = frozenset(xrange(1, 10))

    i = 0
    fibs = fib()
    while True:
        f, i = next(fibs), i + 1
        fmod = f % 1000000000
        fs = int_to_list(fmod)
        if not base == frozenset(fs):
            continue

        fdigits = count_digits_in(f) - 9
        if fdigits < 0:
            continue

        fdiv = f / 10 ** fdigits
        fs = int_to_list(fdiv)
        if base == frozenset(fs):
            break

    print(i)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
