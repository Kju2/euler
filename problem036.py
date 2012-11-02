"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

from euler import is_palindromic


def main():
    """
    >>> main()
    872187
    """
    numbers = xrange(1, 10 ** 6, 2)
    palindroms = [n for n in numbers if is_palindromic(str(n))]
    palindroms = [n for n in palindroms if is_palindromic(bin(n)[2:])]

    print(sum(palindroms))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
