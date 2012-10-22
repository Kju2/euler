"""
A googol (10100) is a massive number: one followed by one-hundred zeros;
100100 is almost unimaginably large: one followed by two-hundred zeros. Despite
their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the
maximum digital sum?
"""

from euler import int_to_list


def main():
    """
    >>> main()
    972
    """
    max_digit_sum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            digit_sum = sum(int_to_list(a ** b))
            if digit_sum > max_digit_sum:
                max_digit_sum = digit_sum

    print(max_digit_sum)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
