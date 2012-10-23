"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 + 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


def sum_of_squares(number):
    """
    >>> sum_of_squares(10)
    385
    """
    return sum((x ** 2 for x in range(number + 1)))


def square_of_sum(number):
    """
    >>> square_of_sum(10)
    3025
    """
    return sum(range(number + 1)) ** 2


def main():
    """
    >>> main()
    25164150
    """
    print(square_of_sum(100) - sum_of_squares(100))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
