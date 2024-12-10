from aocd.models import Puzzle

day = 7
puzzle = Puzzle(year=2024, day=day)
print("Welcome to day " + str(day) + " of Advent of Code 2024 !")
EXAMPLE = False
if EXAMPLE:
    raw_data = puzzle.example_data
    print("Here is the example : \n" + raw_data)
    print()
else:
    raw_data = puzzle.input_data

# ======= Part 1 & 2 =======
part = 2
sum_calibration = 0
for equation in raw_data.split("\n"):
    line = equation.split(':')
    target = int(line[0])
    variables = [int(x) for x in line[1][1:].split(' ')]
    calibration = [variables[0]]
    for variable in variables[1:]:
        new_calibration = []
        for calib in calibration:
            new_calibration.append(calib + variable)
            new_calibration.append(calib * variable)
            if part == 2:
                new_calibration.append(int(str(calib) + str(variable)))
        calibration = new_calibration
    if target in calibration:
        sum_calibration += target

print("The total calibration result for part ", part, " is : ", sum_calibration)
