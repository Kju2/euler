"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


def main():
    """
    >>> main()
    9110846700
    """
    print(str(sum((n ** n for n in range(1, 1000))))[-10:])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
