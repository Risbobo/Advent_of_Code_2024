from aocd.models import Puzzle
import numpy as np
import itertools
from tqdm import tqdm

day = 6
puzzle = Puzzle(year=2024, day=day)
print("Welcome to day " + str(day) + " of Advent of Code 2024 !")
EXAMPLE = False
if EXAMPLE:
    raw_data = puzzle.example_data
    print("Here is the example : \n" + raw_data)
    print()
else:
    raw_data = puzzle.input_data

# ======= Cleaning =======
# number of lines
n = raw_data.count("\n") + 1
# number of columns
m = len(raw_data.split("\n")[0])

# guard_map[i][j] to access the element at the i-th line and j-th column on the map
grid_map = [list(line) for line in raw_data.split('\n')]


# ======= Functions =======
def print_map(map_):
    for line in map_:
        print(''.join(line))


def find_start():
    for i in range(n):
        for j in range(n):
            if grid_map[i][j] == "^":
                return i, j


def is_bounded(i, j):
    return 0 <= i < n and 0 <= j < m


def rotate(direction):
    rotation = np.array([[0, 1], [-1, 0]])
    return rotation.dot(direction)


def is_paradoxable(i, j, direction):
    map_copy = [line.copy() for line in grid_map]
    next_i, next_j = i + direction[0], j + direction[1]
    map_copy[next_i][next_j] = "#"
    direction = rotate(direction)
    marked = set()
    while is_bounded(i, j):
        position = (i, j, direction[0], direction[1])
        if position in marked:
            return True
        marked.add(position)

        next_i, next_j = i + direction[0], j + direction[1]
        # If the guard encounter an obstacle
        if is_bounded(next_i, next_j) and map_copy[next_i][next_j] == "#":
            direction = rotate(direction)
            next_i, next_j = i, j
        i, j = next_i, next_j
    return False


# ======= Part 1 =======
i_start, j_start = find_start()
guard_map = [line.copy() for line in grid_map]
i, j = i_start, j_start
steps = 1
paradoxes = 0
obstacles_created = set()
direction = np.array([-1, 0])
while is_bounded(i, j):
    if guard_map[i][j] == '.':
        steps += 1
    print(steps)
    guard_map[i][j] = "X"
    next_i, next_j = i + direction[0], j + direction[1]
    if is_bounded(next_i, next_j):
        # If the guard encounter an obstacle
        if guard_map[next_i][next_j] == "#":
            direction = rotate(direction)
            next_i, next_j = i, j
        # ======= Part 2 =======
        else:
            if not (next_i == i_start and next_j == j_start) and is_paradoxable(i, j, direction):
                paradoxes += 1
                obstacles_created.add((next_i, next_j))
                # print("Obstacle at ", next_i, next_j)
                #print_map(guard_map)
    i, j = next_i, next_j

for obs in obstacles_created:
    guard_map[obs[0]][obs[1]] = "O"
print_map(guard_map)
print("The guard made ", steps, " steps during her round")
# not 1355 too high, not 1325, not 1352, 1328, 1354 -> Right answer = 1309 ?
print("Second part doesn't work")
print("There are ", paradoxes, " possible paradoxes and ", len(obstacles_created), "positions for obstacles")

