import numpy as np

from aocd.models import Puzzle
day = 2
puzzle = Puzzle(year=2024, day=day)
print("Welcome to day " + str(day) + " of Advent of Code 2024 !")
EXAMPLE = False
if EXAMPLE :
    raw_data = puzzle.example_data
    print("Here is the example : \n" + raw_data)
else:
    raw_data = puzzle.input_data
    # print("Here is the beginning of the data : \n" + str(raw_data.split("\n")[:10]))
#example = puzzle.example_data

# ======= Cleaning =======
reports = [[int(x) for x in elems.split(" ")] for elems in raw_data.split("\n")]
safe_reports1 = 0
safe_reports2 = 0


# ======= functions =======
# Check if levels are either all increasing or all decreasing.
# Accomplished by comparing with sorted levels
def first_conditon(report):
    return report == sorted(report) or report == sorted(report, reverse=True)


# Check is the difference between two successice values is between 1 and 3
def second_condition(report):
    return all([1 <= x <= 3 for x in abs(np.array(report)[:-1] - np.array(report)[1:])])


# ======= Part 1 =======
for report in reports :
    safety1 = first_conditon(report) and second_condition(report)
    if safety1:
        safe_reports1 += 1
    # === Part 2 =======
    else:
        for i in range(len(report)):
            safety2 = first_conditon(report[:i] + report[i+1:]) and second_condition(report[:i] + report[i+1:])
            if safety2:
                safe_reports2 += 1
                break

print("First part : There are " + str(safe_reports1) + " safe reports sur " + str(len(reports)) + " reports")
print("Second part : There are " + str(safe_reports1 + safe_reports2) + " safe reports sur " + str(len(reports)) + " reports")

