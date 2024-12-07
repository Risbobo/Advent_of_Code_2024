from aocd.models import Puzzle

day = 5
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
full_instructions = raw_data.split("\n\n")
first_part, second_part = full_instructions[0], full_instructions[1]

order_rules = {}
# Dictionnary of sets as value that contains the updates allowed after the key
for elem in first_part.split("\n"):
    rule = elem.split("|")
    x, y = int(rule[0]), int(rule[1])
    try:
        order_rules[x].add(y)
    except KeyError:
        order_rules[x] = {y}
updates = [[int(x) for x in update.split(",")] for update in second_part.split("\n")]

# ======= Part 1 =======
sum1 = 0
sum2 = 0
for update in updates:
    correct_order = True
    printed = {update[0]}
    for i, page in enumerate(update):
        try:
            intersec = order_rules[page] & printed
            if len(intersec) != 0:
                correct_order = False
                # ======= Part 2 =======
                for j, printed_page in enumerate(update):
                    if printed_page in intersec:
                        update[i], update[j] = update[j], update[i]
        except KeyError:
            pass
        printed.add(page)
    increment = update[int(len(update) / 2)]
    if correct_order:
        sum1 += increment
    else:
        sum2 += increment
print("The sum of the center page of correct updates is : ", sum1)
print("The sum of the center page of corrected updates is : ", sum2)