"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def sum_of_divisors(n):
    if n == 0:
        return 0

    summe = 1
    p = 2
    while p * p <= n and n > 1:
        if n % p == 0:
            j = p * p
            n = n / p
            while n % p == 0:
                j = j * p
                n = n / p
                pass
            summe = summe * (j-1)
            summe = summe / (p-1)
            pass
        if p == 2:
            p = 3
            pass
        else:
            p = p+2
            pass
        pass

    if n > 1:
        summe *= (n+1)
        pass

    return summe

def sum_of_proper_divisors(n):
    return sum_of_divisors(n) - n

def is_abundant(n):
    return sum_of_proper_divisors(n) > n

abundant_numbers = set([])
def is_not_multiple_of_abundant(n):
    if is_abundant(n):
        abundant_numbers.add(n)
        pass

    for a in abundant_numbers:
        if (n-a) in abundant_numbers:
            return False
            pass
        pass

    return True
    pass

print sum(filter(is_not_multiple_of_abundant, range(28123)))
