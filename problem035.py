"""
The number, 197, is called a circular prime because all rotations of
the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

limit = 10 ** 6


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

primes = frozenset(primes_up_to(limit))


def rotate(n):
    """ return all rotations of this number"""
    digits = list(str(n))
    for _ in range(len(digits)):
        yield int(''.join(digits))
        digits.append(digits.pop(0))
        pass
    pass


def circular_prime(n):
    for rotated_n in rotate(n):
        if rotated_n not in primes:
            return False
            pass
        pass
    return True
    pass

print len(filter(circular_prime, primes))
