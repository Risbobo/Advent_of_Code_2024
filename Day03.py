from aocd.models import Puzzle
import re
day = 3
puzzle = Puzzle(year=2024, day=day)
print("Welcome to day " + str(day) + " of Advent of Code 2024 !")
EXAMPLE = False
if EXAMPLE :
    raw_data = puzzle.example_data
    print("Here is the example : \n" + raw_data)
else:
    raw_data = puzzle.input_data

# ======= Function =======
def parse_mult(text):
    instructions1 = re.findall("mul\([0-9]?[0-9]?[0-9]{1},[0-9]?[0-9]?[0-9]{1}\)", text)
    sum = 0
    for instruction in instructions1:
        parse = re.search("mul\((.+),(.+)\)", instruction)
        mult1 = int(parse.group(1))
        mult2 = int(parse.group(2))
        sum += mult1 * mult2
    return sum

# ======= Part 1 =======
sum = parse_mult(raw_data)
print("The sum of the multiplications asked in part 1 is : " + str(sum))

# ======= Part 2 =======
# We split by don't, then by do and keep only from the first element in this later split
parsed = raw_data.split("don't()")
# Here it is a bit ugly because is a split is empty, we still add it to the instructions
instructions = [parsed[0]] + [''.join(elem.split("do()")[1:]) for elem in parsed[1:]]
# Remove empty element (len : 43 -> 17 more than half lol)
instructions = list(filter(lambda x: x != '', instructions))

sum = 0
for elem in instructions:
    sum += parse_mult(elem)
# 72948684
print("The sum of the multiplications asked in part 2 is : " + str(sum))