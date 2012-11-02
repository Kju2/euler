"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from itertools import combinations_with_replacement
from math import factorial

from euler import int_to_list


def main():
    """
    >>> main()
    40730
    """
    factorials = [factorial(n) for n in range(10)]

    summe = -3  # 1 & 2 which are not counted
    for num_digits in range(8):  # upper limit: 7 * 9! < 10**7
        for number in combinations_with_replacement(xrange(10), num_digits):
            factorial_sum = sum((factorials[digit] for digit in number))
            if sorted(int_to_list(factorial_sum)) == list(number):
                summe += factorial_sum

    print(summe)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
