"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from euler import is_palindrom


def main():
    """
    >>> main()
    906609
    """
    max_palindrom_number = 0
    for multiplier in range(100, 1000):
        for multiplicand in range(multiplier, 1000):
            product = multiplier * multiplicand
            if is_palindrom(product) and product > max_palindrom_number:
                max_palindrom_number = product

    print(max_palindrom_number)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
