"""
Consecutive Primes
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/codeeval-consecutive-primes.html
      https://www.codeeval.com/open_challenges/187/
"""

import unittest
from c187 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(1, solution('2'))

    def test_provided_2(self):
        self.assertEqual(2, solution('4'))

    def test_provided_3(self):
        self.assertEqual(0, solution('5'))

    def test_six(self):
        self.assertEqual(2, solution('6'))

    def test_eight(self):
        self.assertEqual(4, solution('8'))

    def test_ten(self):
        self.assertEqual(96, solution('10'))

    def test_twelve(self):
        self.assertEqual(1024, solution('12'))

    def test_fourteen(self):
        self.assertEqual(2880, solution('14'))

    def test_sixteen(self):
        self.assertEqual(81024, solution('16'))

    def test_eighteen(self):
        self.assertEqual(770144, solution('18'))


if __name__ == '__main__':
    unittest.main()
