"""
Zachariah Kline
20 May 2022
Maze Solver
"""


initial = (5,5) # Where 'o' is.
goal = (95,95) # Where 'x' is.

# Creates a dictionary where the keys are the coordinate points for each character in the txt file.
maze = {}
with open('maze.txt', 'r') as file:
    matrix = (0,0)
    for tile in file.read():
        if tile == '\n':
            maze[matrix] = tile
            matrix = (matrix[0] + 1, 0)
        else:
            maze[matrix] = tile
            matrix = (matrix[0], matrix[1] + 1)
            
def map_maze(solution):
    """
    Plots the path through the maze to the goal.\nOutputs the maze and path to the file 'solved_maze.txt'.\n
    """
    for direction in extract_path(solution):
        if (direction != initial) and (direction != goal):
            maze[direction] = ',' # Path
    with open('solved_maze.txt', 'w') as file:
        for k in maze.keys():
            file.write(maze[k])
            
    print('Generateed a new file, "solved_maze.txt", where you can see the path!\n')
                    
# ----------------------------------------------------------------
# Functions and helper functions for initializing Problem
        
def is_goal(state):
    return state == goal
    
def move_N(state):
    row, col = state[0], state[1]
    row -= 1
    return (row, col)

def move_S(state):
    row, col = state[0], state[1]
    row += 1
    return (row, col)

def move_E(state):
    row, col = state[0], state[1]
    col += 1
    return (row, col)

def move_W(state):
    row, col = state[0], state[1]
    col -= 1
    return (row, col)

def actions(state):
    n, s, e, w = 0, 0, 0, 0 # How many times, given a coordinate, can it move n,s,e, and w.
    while True:
        if state and maze[(state[0] - n - 1, state[1])] != '#':
            n += 1
        else:
            break

    while True:
        if state and maze[(state[0] + s + 1, state[1])] != '#':
            s += 1
        else:
            break
            
    while True:
        if state and maze[(state[0], state[1] + e + 1)] != '#':
            e += 1
        else:
            break

    while True:
        if state and maze[(state[0], state[1] - w - 1)] != '#':
            w += 1
        else:
            break
    
    north = ['N' for _ in range(n)]
    south = ['S' for _ in range(s)]
    east = ['E' for _ in range(e)]
    west = ['W' for _ in range(w)]
    return north + south + east + west
    
def result(state, action):
    if action == 'N':
        return move_N(state)
    elif action == 'S':
        return move_S(state)
    elif action == 'E':
        return move_E(state)
    elif action == 'W':
        return move_W(state)
    else:
        raise ValueError(f'Unrecognized Action: {action}')
        
def action_cost(state, action, new_state):
    return 0

# ----------------------------------------------------------------

from search import Problem, extract_path, extract_actions, breadth_first_search, best_first_search
import os

if __name__ == '__main__':
    os.system('python3 build_maze.py')
    
    problem = Problem(initial, is_goal, result, actions, action_cost)
    #solution = breadth_first_search(problem)
    solution = best_first_search(problem, lambda x: x)
    path = extract_path(solution)
    if path == ['Failure']:
        print('A wall is blocking the path of the goal!\nRe-run file.')
    else:
        print(f'Path:\n{extract_path(solution)}\n')
        print(f'Actions:\n{extract_actions(solution)}')
        map_maze(solution)