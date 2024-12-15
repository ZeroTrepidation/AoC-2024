from src.utils.reportValidation import validateReport

def solution():
    filepath = "../resources/inputs/day2_input.txt"

    with open(filepath) as file:
        lines = file.readlines()
        print(solutionPart1(lines))




def solutionPart1(reports):
    safeReports = 0

    for report in reports:
        if validateReport(report):
            safeReports += 1

    return safeReports
