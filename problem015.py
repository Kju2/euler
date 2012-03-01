from itertools import islice
"""
Starting in the top left corner of a 22 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?
"""
SIZE = 20

def pascals_triangle():
    line = [1]
    yield line
    line = [1,1]
    yield line

    while True:
        new_line = [1]
        for i in range(0, len(line)-1):
            new_line.append(line[i] + line[i+1])
            pass
        new_line.append(1)
        line = new_line
        yield new_line
        pass
    pass

pascals_triangle_line_42 = next(islice(pascals_triangle(), 2*(SIZE-1) + 2, None))
print pascals_triangle_line_42[len(pascals_triangle_line_42)/2]
