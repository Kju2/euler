"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we
note the following:

d_2d_3d_4=406 is divisible by 2
d_3d_4d_5=063 is divisible by 3
d_4d_5d_6=635 is divisible by 5
d_5d_6d_7=357 is divisible by 7
d_6d_7d_8=572 is divisible by 11
d_7d_8d_9=728 is divisible by 13
d_8d_9d_10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from euler import list_to_int
from itertools import permutations

DIVISABLE_BY_2 = frozenset([0, 2, 4, 6, 8])
DIVISABLE_BY_5 = frozenset([0, 5])

result = set([])
for p in permutations(range(10)):
    if p[0] == 0:
        continue

    #if list_to_int(p[3:6]) % 5 != 0:
    if p[5] not in DIVISABLE_BY_5:
        continue

    #if list_to_int(p[1:4]) % 2 != 0:
    if not p[3] in DIVISABLE_BY_2:
        continue

    if list_to_int(p[7:10]) % 17 != 0:
        continue

    if list_to_int(p[6:9]) % 13 != 0:
        continue

    if list_to_int(p[5:8]) % 11 != 0:
        continue

    if list_to_int(p[4:7]) % 7 != 0:
        continue

    #if list_to_int(p[2:5]) % 3 != 0:
    if sum(p[2:5]) % 3 != 0:
        continue

    result.add(p)

print(sum([list_to_int(p) for p in result]))
