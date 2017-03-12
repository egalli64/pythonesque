"""
CodeEval Jolly Jumpers
author: Manny egalli64@gmail.com
info: https://www.codeeval.com/open_challenge_scores/?pkbid=43
      https://www.codeeval.com/
"""
import unittest
from ce.c043 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertTrue(solution('4 1 4 2 3'))

    def test_provided_2(self):
        self.assertFalse(solution('3 7 7 8'))

    def test_provided_3(self):
        self.assertFalse(solution('9 8 9 7 10 6 12 17 24 38'))

if __name__ == '__main__':
    unittest.main()
