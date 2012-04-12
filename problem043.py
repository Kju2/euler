"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we
note the following:

d_2d_3d_4  = 406 is divisible by 2
d_3d_4d_5  = 063 is divisible by 3
d_4d_5d_6  = 635 is divisible by 5
d_5d_6d_7  = 357 is divisible by 7
d_6d_7d_8  = 572 is divisible by 11
d_7d_8d_9  = 728 is divisible by 13
d_8d_9d_10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from euler import list_to_int, int_to_list


BASE = frozenset(range(10))


RESULT = 0
for d4 in [0, 2, 4, 6, 8]:  # to be divisible by 2
    d6 = 5  # otherwise d_7 and d_8 must be equal to be divisible by 11

    for div11 in range(506, 605, 11):  # divisible by 11
        _, d7, d8 = int_to_list(div11)

        number = set([d4, d6])
        if d7 in number or d8 in number:
            continue  # not pandigital

        for div17 in range(102, 1003, 17):  # divisible by 17
            if div17 < d8 * 100 or div17 > (d8 + 1) * 100:
                continue  # d8 doesn't match

            _, d9, d10 = int_to_list(div17)

            number = set([d4, d6, d7, d8])
            if d9 in number or d10 in number:
                continue  # not pandigital

            if list_to_int([d7, d8, d9]) % 13 != 0:
                continue  # not divisible by 13

            number = set([d4, d6, d7, d8, d9, d10])
            for d3 in BASE - number:

                number = set([d3, d4, d6, d7, d8, d9, d10])
                for d5 in BASE - number:

                    if list_to_int([d3, d4, d5]) % 3 != 0:
                        continue  # not divisible by 3

                    if list_to_int([d5, d6, d7]) % 7 != 0:
                        continue  # not divisible by 7

                    number = set([d3, d4, d5, d6, d7, d8, d9, d10])
                    for d2 in BASE - number:

                        number = set([d2, d3, d4, d5, d6, d7, d8, d9, d10, 0])
                        for d1 in BASE - number:
                            RESULT += list_to_int([ \
                                    d1, d2, d3, d4, d5, d6, d7, d8, d9, d10])

print(RESULT)
# 16695334890
