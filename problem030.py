from itertools import ifilter, count, permutations, combinations_with_replacement
"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

power = 5
limit = ifilter(lambda i: 10**i > i*(9**power), count(1)).next()

def int_from_list_of_strings(ns):
    return int(''.join(ns))

def x_th_power_of(ns, power): # ns = tupel of strings, each string is a single number
    return reduce(lambda x, y: x + int(y)**power, ns, 0)
    pass

def t(ns, power): # ns = tupel of strings, each string is a single number
    summe = x_th_power_of(ns, power)
    for i in permutations(ns, len(ns)):
        nummer = int_from_list_of_strings(i)
        if summe == nummer:
            return nummer
            pass
        if summe < nummer:
            break
            pass
        pass
    return 0
    pass


print reduce( \
        lambda x, y: x + t(y, power), \
        combinations_with_replacement(map(str, range(10)), r=limit), \
        0 \
        ) -1
