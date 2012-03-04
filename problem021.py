"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def divisors_of(n):
    divisors = filter((lambda x: n % x == 0), range(2, int(n**0.5)))
    return 1 + sum(map((lambda x: n / x), divisors)) + sum(divisors)
    pass

def amicable(n):
    div_sum_of = divisors_of(divisors_of(n))
    if div_sum_of == n and n != divisors_of(n):
        return True
        pass
    return False
    pass

print sum(filter(amicable, range(1, 10000)))
