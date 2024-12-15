def validate_report_strict(report):
    is_valid = False
    splitReport = [int(n) for n in report.split()]

    is_valid = is_valid or validate_split_report(splitReport, True, True)
    is_valid = is_valid or validate_split_report(splitReport, False, True)

    return is_valid


def validate_report_lenient(report):

    is_valid = False
    splitReport = [int(n) for n in report.split()]

    is_valid = is_valid or validate_split_report(splitReport, True, False)
    is_valid = is_valid or validate_split_report(splitReport, False, False)

    return is_valid


def validate_split_report(report, increasing, strict):

    if strict:
        deletion_used = True
        deletions_allowed = False
    else:
        deletion_used = False
        deletions_allowed = True

    for i in range(len(report)-1):
        valid_level = level_compare(report[i], report[i + 1], increasing)

        if not valid_level and not deletions_allowed:
            return False

        if not valid_level and deletions_allowed:
            if deletion_used:
                return False

            list1 = report.copy()
            list2 = report.copy()

            list1.pop(i)
            list2.pop(i+1)

            valid_removal = (validate_split_report(list1, True, True) or validate_split_report(list2, True, True) or
                             validate_split_report(list1, False, True) or validate_split_report(list2, False, True))

            if valid_removal:
                return True
            else:
                return False

    return True


def level_compare(num_1, num_2, increasing):
    difference = abs(num_1 - num_2)

    if difference < 1 or difference > 3:
        return False

    if num_1 > num_2 and increasing:
        return False

    if num_1 < num_2 and not increasing:
        return False

    return True
