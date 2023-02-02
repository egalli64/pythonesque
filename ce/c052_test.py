"""
CodeEval Text Dollar
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/52/
"""
import unittest
from c052 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('Three', solution('3'))

    def test_provided_2(self):
        self.assertEqual('Ten', solution('10'))

    def test_provided_3(self):
        self.assertEqual('TwentyOne', solution('21'))

    def test_provided_4(self):
        self.assertEqual('FourHundredSixtySix', solution('466'))

    def test_provided_5(self):
        self.assertEqual('OneThousandTwoHundredThirtyFour', solution('1234'))

    def test_thirty_thousand_odd(self):
        self.assertEqual('ThirtyThousandFiveHundredTwentyTwo', solution('30522'))

    def test_eight_hun_eighty(self):
        self.assertEqual('EightHundredEighty', solution('880'))


if __name__ == '__main__':
    unittest.main()
