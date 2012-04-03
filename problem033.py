from fractions import Fraction
from operator import mul
"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""

# not a curious fraction 30/50 or 77/77
curious_fractions = []

for numerator_tens in range(1, 10, 1):
    for denominator_unit in range(1, 10):
        for cancler in range(1, 10):
            numerator = numerator_tens * 10 + cancler
            denominator = cancler * 10 + denominator_unit

            f1 = Fraction(numerator, denominator)
            f2 = Fraction(numerator_tens, denominator_unit)

            if f1 == f2 and numerator != denominator:
                curious_fractions.append(f1)
                pass
            pass
        pass
    pass

print reduce(mul, curious_fractions).denominator
