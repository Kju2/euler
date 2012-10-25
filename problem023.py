"""
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""

ABUNDANT_NUMBERS = set([])


def is_not_multiple_of_abundant(number):
    """
    >>> is_not_multiple_of_abundant(24)
    True
    """
    if is_abundant(number):
        ABUNDANT_NUMBERS.add(number)

    for a in ABUNDANT_NUMBERS:
        if (number - a) in ABUNDANT_NUMBERS:
            return False

    return True


def is_abundant(number):
    """
    >>> is_abundant(28123)
    False
    >>> is_abundant(24)
    True
    """
    return sum_of_proper_divisors(number) > number


def sum_of_proper_divisors(number):
    """
    >>> sum_of_proper_divisors(28)
    28
    """
    return sum_of_divisors(number) - number


def sum_of_divisors(number):
    """
    >>> sum_of_divisors(28)
    56
    """
    if number == 0:
        return 0

    summe = 1
    p = 2
    while p * p <= number and number > 1:
        if number % p == 0:
            j = p * p
            number = number / p
            while number % p == 0:
                j = j * p
                number = number / p
            summe = summe * (j - 1)
            summe = summe / (p - 1)
        if p == 2:
            p = 3
        else:
            p = p + 2

    if number > 1:
        summe *= (number + 1)

    return summe


def main():
    """
    >>> main()
    4179871
    """
    print(sum((n for n in range(28123) if is_not_multiple_of_abundant(n))))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
