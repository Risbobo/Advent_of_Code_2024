from aocd.models import Puzzle
import numpy as np

day = 8
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
antenna_map = [list(line) for line in raw_data.split('\n')]
n = len(antenna_map)
m = len(antenna_map[0])
antennas = {}
for i in range(n):
    for j in range(m):
        if antenna_map[i][j] != '.':
            try:
                antennas[antenna_map[i][j]].append(np.array([i, j]))
            except KeyError:
                antennas[antenna_map[i][j]] = [np.array([i, j])]


def is_bounded(pos):
    return 0 <= pos[0] < n and 0 <= pos[1] < m

# ====== Part 1 & 2 =======
nodes1 = set()
nodes2 = set()
for letter in antennas:
    positions = antennas[letter]
    for i, antenna in enumerate(positions):
        for other_antenna in positions[:i] + positions[i+1:]:
            vec = other_antenna - antenna
            node1 = other_antenna + vec
            if is_bounded(node1):
                nodes1.add((node1[0], node1[1]))
            node2 = antenna + vec
            while is_bounded(node2):
                nodes2.add((node2[0], node2[1]))
                node2 = node2 + vec



print(len(nodes1))
print(len(nodes2))