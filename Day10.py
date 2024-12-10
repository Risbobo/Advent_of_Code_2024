from aocd.models import Puzzle

day = 10
puzzle = Puzzle(year=2024, day=day)
print("Welcome to day " + str(day) + " of Advent of Code 2024 !")
EXAMPLE = False
if EXAMPLE:
    raw_data = "89010123\n78121874\n87430965\n96549874\n45678903\n32019012\n01329801\n10456732"
    print("Here is the example : \n" + raw_data)
    print()
else:
    raw_data = puzzle.input_data

# ======= Cleaning =======
topo_map = [[int(x) for x in line] for line in raw_data.split("\n")]
# number of lines
n = len(topo_map)
# number of columns
m = len(topo_map[0])


# ====== Functions ======
def is_bounded(i, j):
    return 0 <= i < n and 0 <= j < m


def explore(position, elevation):
    if elevation == 9:
        return {position}, 1
    score = set()
    rate = 0
    for direction in [(1,0), (0,1), (-1,0), (0,-1)]:
        next_i = position[0] + direction[0]
        next_j = position[1] + direction[1]
        if is_bounded(next_i, next_j) and topo_map[next_i][next_j] == elevation + 1:
            score_update, rate_update = explore((next_i, next_j), elevation + 1)
            score.update(score_update)
            rate += rate_update
    return score, rate

# ======= Part 1 =======
map_score = 0
map_rate = 0
for i, line in enumerate(topo_map):
    for j, elevation in enumerate(line):
        if elevation == 0:
            trailscore, trailrate = explore((i,j), 0)
            map_score += len(trailscore)
            map_rate += trailrate

print("The score of all trailheads in part 1 is : ", map_score)
print("The rating of all trailheads in part 2 is : ", map_rate)