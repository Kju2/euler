"""
Starting in the top left corner of a 2x2 grid, there are 6 routes (without
backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?
"""

from itertools import islice

from euler import pascals_triangle


def main():
    """
    >>> main()
    137846528820
    """
    size = 20

    pascals_triangle_line_42 = next(
            islice(pascals_triangle(), 2 * (size - 1) + 2, None)
    )
    print(pascals_triangle_line_42[len(pascals_triangle_line_42) / 2])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
