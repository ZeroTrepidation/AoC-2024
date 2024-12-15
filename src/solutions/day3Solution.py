import src.utils.multiParser as mp

def solution():
    filepath = "../resources/inputs/day3_input.txt"

    with open(filepath) as file:
        lines = file.readlines()
        print("Total value without toggle {}\nTotal value with toggle {}"
              .format(solutionPart1(lines), solutionPart2(lines)))


def solutionPart1(lines):
    total = 0
    multi_on = True

    for line in lines:
        v, multi_on = mp.parse_line(line, False, multi_on)
        total = total + v

    return total

def solutionPart2(lines):
    total = 0
    multi_on = True

    for line in lines:
        v, multi_on = mp.parse_line(line, True, multi_on)
        total = total + v

    return total






