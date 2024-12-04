from aocd.models import Puzzle

day = 4
puzzle = Puzzle(year=2024, day=day)
print("Welcome to day " + str(day) + " of Advent of Code 2024 !")
EXAMPLE = False
if EXAMPLE:
    raw_data = "MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX"
    print("Here is the example : \n" + raw_data)
else:
    raw_data = puzzle.input_data

# ======= Cleaning and Setup =======
# number of lines
n = raw_data.count("\n") + 1
# number of columns
m = len(raw_data.split("\n")[0])
string = list(filter(lambda x: x != '\n', raw_data))


# ======= functions =======
def is_bounded(index):
    return 0 <= index < len(string)


def check(index, direction, letter, grid):
    if not is_bounded(index) or grid[index] != letter:
        return False
    next_letter = letter
    if letter == 'S':
        return True
    elif letter == "X":
        next_letter = "M"
    elif letter == "M":
        next_letter = "A"
    elif letter == "A":
        next_letter = "S"
    # 0 for up
    if direction == 0:
        next_indice = index - m
        return check(next_indice, direction, next_letter, grid)
    # 1 for up right
    if direction == 1:
        next_indice = index - m + 1
        if next_indice % m != index % m + 1:
            return False
        return check(next_indice, direction, next_letter, grid)
    # 2 for right
    if direction == 2:
        next_indice = index + 1
        if next_indice % m != index % m + 1:
            return False
        return check(next_indice, direction, next_letter, grid)
    # 3 for down right
    if direction == 3:
        next_indice = index + m + 1
        if next_indice % m != index % m + 1:
            return False
        return check(next_indice, direction, next_letter, grid)
    # 4 for down
    if direction == 4:
        next_indice = index + m
        return check(next_indice, direction, next_letter, grid)
    # 5 for down left
    if direction == 5:
        next_indice = index + m - 1
        if next_indice % m != index % m - 1:
            return False
        return check(next_indice, direction, next_letter, grid)
    # 6 for left
    if direction == 6:
        next_indice = index - 1
        if next_indice % m != index % m - 1:
            return False
        return check(next_indice, direction, next_letter, grid)
    # 7 for up left
    if direction == 7:
        next_indice = index - m - 1
        if next_indice % m != index % m - 1:
            return False
        return check(next_indice, direction, next_letter, grid)



sum1 = 0
sum2 = 0
for i in range(len(string)):
    # ======= part 1 =======
    for dir in range(8):
        if check(i, dir, "X", string):
            sum1 += 1
    # ======= part 2 =======
    if (check(i - m - 1, 3, "M", string) or check(i + m + 1, 7, "M", string)) and \
            (check(i - m + 1, 5, "M", string) or check(i + m - 1, 1, "M", string)):
        sum2 += 1

print("There are ", sum1, " XMAS in the grid in part 1")
print("There are ", sum2, " X-MAS in the grid in part 2")
