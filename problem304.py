"""
http://projecteuler.net/problem=304
"""


def fib(nth):
    """fib returns the nth fibonacci number."""
    fib_matrix = [[1, 1], [1, 0]]
    if nth == 0:
        return 0
    power(fib_matrix, nth - 1)
    return fib_matrix[0][0]


def power(matrix, exponent):
    """power computes the power to a given matrix."""
    if exponent == 0 or exponent == 1:
        return

    power(matrix, exponent / 2)
    multiply(matrix, matrix)

    if exponent % 2 != 0:
        multiply(matrix, [[1, 1], [1, 0]])


def multiply(matrix_a, matrix_b):
    """
    multiply multiplies two matrixes. The result is saved to matrix_a and
    is given mod 1234567891011.
    """
    x = matrix_a[0][0] * matrix_b[0][0] + matrix_a[0][1] * matrix_b[1][0]
    y = matrix_a[0][0] * matrix_b[0][1] + matrix_a[0][1] * matrix_b[1][1]
    z = matrix_a[1][0] * matrix_b[0][0] + matrix_a[1][1] * matrix_b[1][0]
    w = matrix_a[1][0] * matrix_b[0][1] + matrix_a[1][1] * matrix_b[1][1]

    matrix_a[0][0] = x % 1234567891011
    matrix_a[0][1] = y % 1234567891011
    matrix_a[1][0] = z % 1234567891011
    matrix_a[1][1] = w % 1234567891011


def main():
    """
    Precomupted the primes in the file "problem304.txt" to reduce the runtime.
    >>> main()
    283988410192
    """
    limit = 100000

    primes = [int(i) for i in open("problem304.txt").readline().split(' ')]

    print(sum(fib(primes[n]) for n in range(limit)) % 1234567891011)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
