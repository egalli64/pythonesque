"""
CodeEval Spiral Printing
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/57/
"""
import unittest

from ce.c057 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided(self):
        self.assertEqual('1 2 3 6 9 8 7 4 5', solution(3, 3, '1 2 3 4 5 6 7 8 9'))

    def test_one_line(self):
        self.assertEqual('1 2 3 4 5', solution(1, 5, '1 2 3 4 5'))

    def test_two_columns(self):
        self.assertEqual('1 2 4 6 8 7 5 3', solution(4, 2, '1 2 3 4 5 6 7 8'))

if __name__ == '__main__':
    unittest.main()
