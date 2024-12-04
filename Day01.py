import numpy as np

from aocd.models import Puzzle
day = 1
puzzle = Puzzle(year=2024, day=day)
print("Welcome to day " + str(day) + " of Advent of Code 2024 !")
EXAMPLE = False
if EXAMPLE :
    raw_data = puzzle.example_data
else:
    raw_data = puzzle.input_data
example = puzzle.example_data

# ======= Cleaning =======
list1, list2 = [], []
for elems in raw_data.split("\n"):
    elem = elems.split("   ")
    list1.append(int(elem[0]))
    list2.append(int(elem[1]))

list1.sort()
list2.sort()
array1 = np.array(list1)
array2 = np.array(list2)

# ======= Part 1 =======
print("The answer for the first part is : " + str(sum(abs(array2 - array1))))
part1 = sum(abs(array2 - array1))

# ======= Part 2 =======
sum = 0
for elem in list1:
    sum += elem * list2.count(elem)

print("The answer for the first part is : " + str(sum))
part2 = sum
