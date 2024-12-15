import unittest
import src.utils.multiParser as mp

class multiParserTest(unittest.TestCase):
    def testMultiParser_toggle_off(self):

        number = mp.parse_line("mul(50,5)", False, True)
        number2 = mp.parse_line("mul(50,,,,,,5)mul(50,5)", False, True)
        number3 = mp.parse_line("mul(50,5)feafeafe", False, True)
        number4 = mp.parse_line("feafewsaf3mul(50,5)", False, True)
        number5 = mp.parse_line("mul(50,5)mul(50,5)", False, True)

        self.assertEqual(250, number)
        self.assertEqual(250, number2)
        self.assertEqual(250, number3)
        self.assertEqual(250, number4)
        self.assertEqual(500, number5)

    def testMultiParser_toggle_on(self):
        number = mp.parse_line("mul(50,5)", True, True)[0]
        number2 = mp.parse_line("don't()mul(50,5)", True, True)[0]
        number3 = mp.parse_line("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))", True, True)[0]

        self.assertEqual(250, number)
        self.assertEqual(0, number2)
        self.assertEqual(48, number3)

