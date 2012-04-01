"""
In England the currency is made up of pound and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, 1 Pound (100p) and 2 Pound (200p).
It is possible to make 2 Pound in the following way:

1 x 1 Pound + 1 x 50p + 2 x 20p + 1 x 5p + 1 x 2p + 3 x 1p

How many different ways can 2 Pound be made using any number of coins?
"""
limit = 200

coins =[1, 2, 5, 10, 20, 50, 100, 200]

array = [0] * 201
array[0] = 1

for c in coins:
    for n in xrange(c, limit+1):
        array[n] += array[n-c]
        pass
    pass

print array[200]
