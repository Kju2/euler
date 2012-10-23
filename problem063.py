"""
The 5-digit number, 16807=7^5, is also a fifth power. Similarly,
the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""


def main():
    """
    >>> main()
    49
    """
    counter = 0
    for power in range(1, 22):
        for base in range(10, 0, -1):
            number = base ** power
            length = len(str(number))
            if length <= power:
                if length == power:
                    counter += 1
                    continue
                break

    print(counter)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
