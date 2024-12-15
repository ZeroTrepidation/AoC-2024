from src.utils.reportValidation import validate_report_strict, validate_report_lenient

def solution():
    filepath = "../resources/inputs/day2_input.txt"

    with open(filepath) as file:
        lines = file.readlines()
        print("Safe records without deletions {} \nSafe records with deleteions {}"
              .format(solutionPart1(lines), solution_part2(lines)))




def solutionPart1(reports):
    safeReports = 0

    for report in reports:
        if validate_report_strict(report):
            safeReports += 1

    return safeReports


def solution_part2(reports):
    safeReports = 0
    for report in reports:
        if validate_report_lenient(report):
            safeReports += 1

    return safeReports
