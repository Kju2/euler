"""
euler - a collection of functions useful in more than one euler problem
"""

from math import log10, sqrt


def pascals_triangle():
    """pascals_triangle is an generator for lines of the pascal's triangle.

    >>> pt = pascals_triangle()
    >>> pt.next()
    [1]
    >>> pt.next()
    [1, 1]
    >>> pt.next()
    [1, 2, 1]
    >>> pt.next()
    [1, 3, 3, 1]
    """
    line = [1]
    yield line

    line = [1, 1]
    yield line

    while True:
        new_line = [1]
        for i in range(0, len(line) - 1):
            new_line.append(line[i] + line[i + 1])

        new_line.append(1)
        line = new_line
        yield new_line


def divisors_of(number):
    """
    divisors_of returns a set of all divisors of the given number.

    >>> divisors_of(36) == set([1, 2, 3, 4, 6, 9, 12, 18, 36])
    True
    >>> divisors_of(220) == set([1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110, 220])
    True
    >>> [divisors_of(n) for n in range(100000)] != []
    True
    """
    divisors = {d for d in range(1, int(sqrt(number) + 1)) if number % d == 0}
    return divisors.union({number // d for d in divisors})


def fib():
    """
    fib calculates the Fibonacci sequence
    """
    fib_n, fib_m = 0, 1

    while True:
        yield fib_m
        fib_n, fib_m = fib_m, fib_n + fib_m


def int_to_list(number):
    """
    int_to_list - returns a list of digits of a positive number.

    >>> int_to_list(42)
    [4, 2]
    >>> int_to_list(101)
    [1, 0, 1]
    """
    return [int(n) for n in str(number)]


def is_even(number):
    """
    is_even - returns True if a number is even, False otherwise.
    >>> is_even(0)
    True
    >>> is_even(1)
    False
    >>> is_even(2)
    True
    >>> map(is_even, [3, 4, 5, 6, 7, 8, 9, 10])
    [False, True, False, True, False, True, False, True]
    """
    return number % 2 == 0


def is_integer(number):
    """
    is_integer - returns True if a number is without decimal part, False
    otherwise.
    >>> is_integer(10)
    True
    >>> is_integer(192.9320)
    False
    """
    return number % 1 == 0


def is_int_pandigital(number):
    """
    is_int_pandigital tests if a int number is pandigital. A pandigital number
    uses numbers 1 trough to the count of a digits of the number.

    >>> is_int_pandigital(1)
    True
    >>> is_int_pandigital(4)
    False
    >>> is_int_pandigital(1234)
    True
    >>> is_int_pandigital(36932)
    False
    """
    digits = int(log10(number) + 1)
    if digits > 9:
        return False

    base = [False] * digits

    while number > 0:
        number, rest = divmod(number, 10)
        if rest > digits:
            return False
        base[rest - 1] = True

    return all(base)


def is_odd(number):
    """
    is_odd - return True if a number is odd, False otherwise.
    >>> is_odd(1)
    True
    >>> is_odd(2)
    False
    >>> map(is_odd, [3, 4, 5, 6, 7, 8, 9, 10])
    [True, False, True, False, True, False, True, False]
    """
    return not is_even(number)


def is_palindromic(number):
    """is_palindromic tests if a number is palindromic.

    >>> is_palindromic(232)
    True
    >>> is_palindromic(9009)
    True
    >>> is_palindromic(23292)
    False
    """
    n_str = str(number)
    return n_str == n_str[::-1]


def list_to_int(digits):
    """
    list_to_int - joins a list of digits to an integer. The digits can be
    strings or ints. For base 10 numbers. Efficient up to 30 digits, then
    a map-approach is faster.

    >>> list_to_int('0')
    0
    >>> list_to_int([0])
    0
    >>> list_to_int('2904234')
    2904234
    >>> list_to_int([2, 9, 0, 4, 2, 3, 4])
    2904234
    >>> list_to_int((2, 9, 0, 4, 2, 3, 4))
    2904234
    >>> list_to_int((2, 9)) == int(''.join(map(str, (2, 9))))
    True
    >>> list_to_int((4, 2)) == int(''.join(('4', '2')))
    True
    """
    number = 0

    for digit in digits:
        number *= 10
        number += int(digit)

    return number


if __name__ == "__main__":
    import doctest
    doctest.testmod()
