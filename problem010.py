from itertools import takewhile
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
limit = 2 * 10**6

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

print sum(primes_up_to(limit))
