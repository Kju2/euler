from math import log10
"""
The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain prime at
each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""


def primes_up_to(limit):
    """the sieve of Eratosthenes"""
    sieve_bound = (limit - 1) // 2
    sieve = range(0, sieve_bound)
    cross_limit = int((limit ** 0.5 - 1) / 2)

    for i in range(cross_limit):
        if sieve[i]:  # 2*i + 1 is prime, mark multiples
            for j in range(2 * i * (i + 1), sieve_bound, 2 * i + 1):
                sieve[j] = 0
            pass
        pass
    pass
    return [2] + [2 * p + 1 for p in sieve if p]


def truncateable_prime(n):
    p = n
    while p > 10:
        #  truncate right
        p = p / 10
        if p not in primes:
            return False
            pass
        pass

    p = n
    while p > 10:
        #  truncate left
        p = p % (10 ** int(log10(p)))
        if p not in primes:
            return False
            pass
        pass

    return True
    pass

primes = frozenset(primes_up_to(10 ** 6))
print sum(filter(truncateable_prime, primes)) - sum([2, 3, 5, 7])
