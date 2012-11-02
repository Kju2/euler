"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192  1 = 192
192  2 = 384
192  3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

from itertools import count

from euler import int_to_list, is_int_pandigital, list_to_int


def main():
    """
    >>> main()
    932718654
    """
    max_len_number = 9
    max_pandigital_number = 0
    # since the multiplier must be at least 2 we can stop when the
    # multiplicand * 1 and multiplicand * 2 together have more than 9 numbers
    for multiplicand in range(2, 10000):
        product_as_list = int_to_list(multiplicand)
        for multiplier in count(2):
            product_as_list += int_to_list(multiplicand * multiplier)
            product = list_to_int(product_as_list)

            if is_int_pandigital(product) and max_pandigital_number < product:
                max_pandigital_number = product
            elif len(product_as_list) > max_len_number:
                break

    print(max_pandigital_number)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
