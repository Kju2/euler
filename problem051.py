"""
By replacing the 1st digit of *3, it turns out that six of the nine possible
values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
"""

from euler import list_to_int, int_to_list
from prime import Primes


def main():
    """
    >>> main()
    121313
    """
    amount_of_primes = 8

    primes = Primes(10 ** 6)
    for prime in primes:
        prime_as_list = int_to_list(prime)

        list_of_indices = []  # indices of reoccuring digits
        for i in range(len(prime_as_list)):
            for j in range(i + 1, len(prime_as_list)):
                for k in range(j + 1, len(prime_as_list)):
                    if prime_as_list[j] == prime_as_list[k]:
                        list_of_indices.append((i, j, k))

        for indices in list_of_indices:
            prime_family = []
            for d in range(10):
                prime_candidate = prime_as_list[:]
                for i in indices:
                    prime_candidate[i] = d

                # ensure that we don't look at n-1-digit numbers
                if prime_candidate[0] == 0:
                    continue

                prime_candidate = list_to_int(prime_candidate)
                if prime_candidate in primes:
                    prime_family.append(prime_candidate)

                # check if we still can get the neccasry amount of primes
                if (10 - d) + len(prime_family) < amount_of_primes:
                    break

            if len(prime_family) == amount_of_primes:
                print(prime)
                return


if __name__ == "__main__":
    import doctest
    doctest.testmod()
