"""
http://projecteuler.net/problem=81
"""
import Queue


result = {}


def main():
    """
    >>> main()
    427337
    """
    matrix = []
    with open("problem081.txt") as f:
        for line in f.read().splitlines():
            matrix.append([int(n) for n in line.split(',')])

    queue = Queue.PriorityQueue()
    queue.put((matrix[0][0], 0, 0))
    while queue.empty() is False:
        (cost, x, y) = queue.get()

        if x < len(matrix) - 1:
            new_x = x + 1
            costx = matrix[new_x][y] + cost
            if min_path_sum((new_x, y), costx):
                queue.put((costx, new_x, y))

        if y < len(matrix) - 1:
            new_y = y + 1
            costy = matrix[x][new_y] + cost
            if min_path_sum((x, new_y), costy):
                queue.put((costy, x, new_y))

    print(result[(len(matrix) - 1, len(matrix) - 1)])


def min_path_sum(pos, cost):
    if pos in result:
        if cost > result[pos]:
            return False

    result[pos] = cost
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
