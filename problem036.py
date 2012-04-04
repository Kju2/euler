"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""


def is_palindrome(n):
    middle = len(n) // 2
    for index in xrange(middle):
        if n[index] != n[-(index + 1)]:
            return False
            pass
        pass
    return True
    pass

numbers = range(1, 10 ** 6, 2)
palindroms = filter(lambda n: is_palindrome(str(n)), numbers)
palindroms = filter(lambda n: is_palindrome(bin(n)[2:]), palindroms)

print sum(palindroms)
