"""
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""

from itertools import combinations_with_replacement, permutations

from euler import list_to_int


def main():
    """
    >>> main()
    443839
    """
    power = 5
    limit = 6

    result = (-1)  # 1 ** power isn't included
    for combination in combinations_with_replacement(xrange(10), r=limit):
        summe = sum([d ** power for d in combination])
        for permutation in permutations(combination, limit):
            number = list_to_int(permutation)
            if summe < number:
                break
            elif summe == number:
                result += number
                break

    print(result)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
