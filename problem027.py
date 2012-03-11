from itertools import count, dropwhile, product
"""
Euler published the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n**2  79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n**2 + an + b, where |a|  1000 and |b|  1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

# primes_up_to from problem 10
def primes_up_to(limit):
    """the sieve of Eratosthenes"""
    sieve_bound = (limit-1) // 2
    sieve = range(0,sieve_bound)
    cross_limit = int((limit**0.5 -1) / 2)

    for i in range(cross_limit):
        if sieve[i]: # 2*i + 1 is prime, mark multiples
            for j in range(2*i*(i+1), sieve_bound, 2*i+1):
                sieve[j] = 0
            pass
        pass
    pass
    return [2] + [2*p+1 for p in sieve if p]

def is_prime(p):
    if p in is_prime.primes:
        return True
        pass
    if p < is_prime.max_prime:
        return False
        pass
    if p < 0:
        return is_prime(abs(p))
        pass

    is_prime.primes = frozenset(primes_up_to(p*2))
    is_prime.max_prime = max(is_prime.primes)
    return is_prime(p)
    pass

is_prime.primes = frozenset(primes_up_to(10**5))
is_prime.max_prime = max(is_prime.primes)

def consecutive_primes_for(a, b):
    return next(dropwhile(lambda n: is_prime(n**2 + a*n + b), count(0)))-1

# 'a' needs to be odd, otherwise for every odd 'n', the result is even
a = range(-999, 1000, 2)
# 'b' needs to be prime, otherwise for n=0 the formula will never give a prime
b = filter(is_prime, range(-999, 1000, 2))

print max( \
        map(lambda (a, b): (consecutive_primes_for(a, b), a * b), product(a, b)), \
        key=(lambda (consecutive_primes, product_a_b): consecutive_primes) \
        )[1]
