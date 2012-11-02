"""
http://projecteuler.net/problem=104
"""


def main():
    """
    >>> main()
    329468
    """
    base = frozenset(map(str, xrange(1, 10)))

    index = 2
    f1, f2 = 1, 1  # first digits of fibonacci number
    l1, l2 = 1, 1  # last digits of fibonacci number
    while set(str(f2)[:9]) != base or set(str(l2)) != base:
        index += 1
        f1, f2 = f2, f1 + f2
        if f2 > 10 ** 18:
            f1, f2 = f1 // 10, f2 // 10

        l1, l2 = l2, (l1 + l2) % 10 ** 10

    print(index)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
