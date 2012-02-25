from itertools import islice
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
_primes = [2, 3]

def primes():
    yield 2
    yield 3

    # a number is a prime if it is not divisible by any other prime
    possible_prime = 5
    while True:
        maxDivisor = possible_prime ** 0.5
        for divisor in _primes:
            if divisor > maxDivisor:
                _primes.append(possible_prime)
                yield possible_prime
                break
                pass

            if possible_prime % divisor == 0:
                break
                pass
            pass

        possible_prime += 2
        pass
    pass

print next(islice(primes(), 10000, None))
