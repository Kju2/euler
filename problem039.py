from math import sqrt
"""
If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""


max_perimeter = 1000


def pythagoren_triples(max_c):
    #  the smallest pythagoren triple has c == 5
    for c in range(5, max_c):
        #  a as the smallest number in the triple must be between
        #  sqrt(c ** 2 - (c - 1) ** 2) <= a <= sqrt(c ** 2 / 2)
        #  otherwise for b < c: a ** 2 + b ** 2 != c ** 2
        #  or a ** 2 > (z ** 2) / 2 and b < a, although a is the smallest
        for a in range(int(sqrt(2 * c - 1)), int(c / sqrt(2) + 1)):
            b = int(sqrt(c ** 2 - a ** 2))
            if a ** 2 + b ** 2 == c ** 2:
                yield (a, b, c)
                pass
            pass
        pass
    pass


def grouper(iterable):
    """ counts objects which are the same and groups them """
    groups = {}
    for key in iterable:
        #  if key is not in the dict set the value to 0
        #  otherwise use the value from the dict
        groups.setdefault(key, 0)
        groups[key] += 1
        pass

    return groups
    pass

perimeters = map(sum, pythagoren_triples(max_perimeter))
filtered_perimeters = filter(lambda pm: pm <= max_perimeter, perimeters)
grouped_perimeters = grouper(filtered_perimeters)

print max(grouped_perimeters.iteritems(), key=lambda d: d[1])[0]
