from itertools import takewhile, count
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
limit = 1000

def take_while_below(iterable):
    return takewhile(lambda x: x < limit, iterable)
    pass

#All numbers that are multiples of 3 and below the limit
multiples_of_three = take_while_below(count(0, 3))

#All numbers that are multiples of 5 and below the limit
multiples_of_five = take_while_below(count(0, 5))

#All numbers that are multiples of 15 and below the limit
multiples_of_fifteen = take_while_below(count(0, 15))

#Since multiples of 15 are counted two times remove them once from the sum
print sum(multiples_of_five) + sum(multiples_of_three) - sum(multiples_of_fifteen)
