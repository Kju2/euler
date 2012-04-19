"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

LIMIT = 1000

# All numbers that are multiples of 3 and below the limit
multiples_of_3 = sum(range(3, LIMIT, 3))

# All numbers that are multiples of 5 and below the limit
multiples_of_5 = sum(range(5, LIMIT, 5))

# Since multiples of 15 are counted two times remove them once from the sum
multiples_of_15 = sum(range(15, LIMIT, 15))

print(multiples_of_3 + multiples_of_5 - multiples_of_15)
