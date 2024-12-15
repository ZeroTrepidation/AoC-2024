
def validateReport(report):
    splitReport = [int(n) for n in report.split()]
    if (splitReport[0] > splitReport[len(splitReport)-1]):
        return validateReportDecreasing(splitReport)
    else:
        return validateReportIncreasing(splitReport)


def validateReportIncreasing(report):
    for i in range(len(report)-1):
        difference = abs(report[i] - report[i + 1])
        if report[i] > report[i+1]:
            return False
        if difference < 1 or difference > 3:
            return False

    return True


def validateReportDecreasing(report):
    for i in range(len(report)-1):
        difference = abs(report[i] - report[i+1])
        if report[i] < report[i+1]:
            return False
        if difference < 1 or difference > 3:
            return False

    return True


