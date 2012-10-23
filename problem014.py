"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

COLLATZ_ = {0: 0, 1: 1}


def collatz(number):
    """
    >>> collatz(13)
    10
    """
    if number not in COLLATZ_:
        if number % 2 == 0:
            COLLATZ_[number] = collatz(number / 2) + 1
        else:
            COLLATZ_[number] = collatz(3 * number + 1) + 1

    return COLLATZ_[number]


def main():
    """
    >>> main()
    837799
    """
    limit = 10 ** 6

    print(max(xrange(limit), key=collatz))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
