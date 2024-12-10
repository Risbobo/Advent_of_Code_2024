from aocd.models import Puzzle

day = 9
puzzle = Puzzle(year=2024, day=day)
print("Welcome to day " + str(day) + " of Advent of Code 2024 !")
EXAMPLE = False
if EXAMPLE:
    raw_data = puzzle.example_data
    print("Here is the example : \n" + raw_data)
    print()
else:
    raw_data = puzzle.input_data


# ====== Part 1 ======
free1 = []
files1 = []
files2 = []
files_size1 = []
counter = 0
for i in range(len(raw_data)):
    value = int(raw_data[i])
    if i % 2 == 1:
        free1.append(value)
    else:
        file = []
        for _ in range(value):
            files1.append(counter)
            file.append(counter)
        files2.append(file)
        files_size1.append(value)
        counter += 1
free2 = free1.copy()
files_size2 = files_size1.copy()

rearranged = []
for _ in range(files_size1.pop(0)):
    rearranged.append(files1.pop(0))

free_space = sum(free1)
while free1[-1] != free_space:
    next_free = free1.pop(0)
    for i in range(next_free):
        try:
            rearranged.append(files1.pop(-1))
        except IndexError:
            break
    free1[-1] += next_free

    next_file = files_size1.pop(0)
    for i in range(next_file):
        try:
            rearranged.append(files1.pop(0))
        except IndexError:
            break

checksum = 0
for i, x in enumerate(rearranged):
    checksum += i * x
print("The checksum value from part 1 is : ", checksum)


# ====== Part 2 ======
i = len(files2) - 1
while i >= 1 :
    block = files2[i]
    for j, space in enumerate(free2[:i]):
        if len(block) <= space:
            free2[j] -= len(block)
            free2[i-1] += len(block)
            if i < len(files2) - 1:
                free2[i-1] += free2.pop(i)
            files2.pop(i)
            files2.insert(j+1, block)
            free2.insert(j, 0)
            i += 1
            break
    i -= 1

checksum = 0
index = 0
for i, file in enumerate(files2):
    for data in file:
        checksum += data * index
        index += 1
    index += free2[i]
print("The checksum value from part 2 is : ", checksum)