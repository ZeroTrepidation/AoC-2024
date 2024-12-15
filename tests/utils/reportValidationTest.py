import unittest
import src.utils.reportValidation as rv

class ReportValidationTest(unittest.TestCase):


    def test_validateReport(self):
        reports = []
        reports.append('7 6 4 2 1')
        reports.append('1 2 7 8 9')
        reports.append('9 7 6 2 1')
        reports.append('1 3 2 4 5')
        reports.append('8 6 4 4 1')
        reports.append('1 3 6 7 9')
        reports.append('6 7 7 9 9')
        reports.append('6 8 9 12 14 15')

        expectedResult = [True, False, False, False, False, True, False, True]
        actualResult = []

        for report in reports:
            actualResult.append(rv.validateReport(report))

        self.assertEqual(expectedResult, actualResult)

    def test_validateReportIncreasing(self):
        report = [int(n) for n in '6 8 9 12 14 15'.split()]
        self.assertTrue(rv.validateReportIncreasing(report))


    def test_validateReportDecreasing(self):
        report = [int(n) for n in '12 10 7 6 4 2 1'.split()]
        self.assertTrue(rv.validateReportDecreasing(report))
