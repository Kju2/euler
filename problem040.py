from functools import reduce
from itertools import chain, count, imap, islice
"""
An irrational decimal fraction is created by concatenating
the positive integers:

             x
0.123456789101112131415161718192021...
             x

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the n^th digit of the fractional part, find the value of
the following expression.

d_1 *  d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000
"""

indices = [0] + [(9 * 10 ** p) - 1 for p in range(0, 6)]

fraction = chain.from_iterable(imap(str, count(1)))

print((reduce( \
        lambda prev, i: prev * int(next(islice(fraction, i, None))), \
        indices, \
        1) \
    ))
