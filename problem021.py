"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a != b, then a
and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from euler import divisors_of


def amicable(number):
    """
    >>> amicable(220)
    True
    """
    divs_of_n = sum(divisors_of(number)) - number
    divs_sum_of_n = sum(divisors_of(divs_of_n)) - divs_of_n
    return divs_sum_of_n == number and number != divs_of_n


def main():
    """
    >>> main()
    31626
    """
    print(sum((i for i in range(1, 10000) if amicable(i))))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
