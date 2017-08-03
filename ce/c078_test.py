"""
CodeEval Sudoku
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/78/
"""
import unittest

from ce.c078 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(True, solution(4, [1, 4, 2, 3,
                                            2, 3, 1, 4,
                                            4, 2, 3, 1,
                                            3, 1, 4, 2]))

    def test_provided_2(self):
        self.assertEqual(False, solution(4, [2, 1, 3, 2,
                                             3, 2, 1, 4,
                                             1, 4, 2, 3,
                                             2, 3, 4, 1]))

    def test_extra(self):
        self.assertEqual(False, solution(9, [1, 2, 3, 4, 5, 6, 7, 8, 9,
                                             2, 3, 4, 5, 6, 7, 8, 9, 1,
                                             3, 4, 5, 6, 7, 8, 9, 1, 2,
                                             4, 5, 6, 7, 8, 9, 1, 2, 3,
                                             5, 6, 7, 8, 9, 1, 2, 3, 4,
                                             6, 7, 8, 9, 1, 2, 3, 4, 5,
                                             7, 8, 9, 1, 2, 3, 4, 5, 6,
                                             8, 9, 1, 2, 3, 4, 5, 6, 7,
                                             9, 1, 2, 3, 4, 5, 6, 7, 8]))


if __name__ == '__main__':
    unittest.main()
