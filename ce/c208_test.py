"""
Find the highest score
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-find-highest-score.html
      https://www.codeeval.com/open_challenges/208/
"""
import unittest
from ce.c208 import solution


class TestStepwiseWord(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('100 250 150', solution('72 64 150 | 100 18 33 | 13 250 -6'))

    def test_provided_2(self):
        self.assertEqual('13 25 70 44', solution('10 25 -30 44 | 5 16 70 8 | 13 1 31 12'))

    def test_provided_3(self):
        self.assertEqual('100 200 300 400 500', solution('100 6 300 20 10 | 5 200 6 9 500 | 1 10 3 400 143'))


if __name__ == '__main__':
    unittest.main()
