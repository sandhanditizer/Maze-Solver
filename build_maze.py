"""
Zachariah Kline
20 May 2022
Maze Solver
"""


import random

def line(x, y, dx, dy, length):
    """Returns points for a line. Starts at (x, y) goes in the direction (dx, dy) for given length"""
    return {(x+i*dx, y+i*dy) for i in range(length)}

def random_lines(Nx, Ny, N=100, lengths=range(5, 20)):
    X = range(0, Nx)
    Y = range(0, Ny)
    result = set()
    for _ in range(N):
        x, y = random.choice(X), random.choice(Y)
        dx, dy = random.choice(((0, 1), (1, 0)))
        result |= line(x, y, dx, dy, random.choice(lengths))
    return result


if __name__ == '__main__':
    Nx = 100
    Ny = 100

    start = (5, 5)
    goal = (Nx-5, Ny-5)

    walls = random_lines(Nx, Ny)

    with open('maze.txt', 'w') as f:
        for y in range(Ny):
            for x in range(Nx):
                if (x, y) == start:
                    f.write('O')
                elif (x, y) == goal:
                    f.write('X')
                elif x == 0 or y == 0 or x == Nx-1 or y == Ny-1 or (x, y) in walls:
                    f.write('#')
                else:
                    f.write(' ')
            f.write('\n')