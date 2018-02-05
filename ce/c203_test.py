# Strings and arrows
# author: Manny egalli64@gmail.com
# info: http://thisthread.blogspot.com/2017/01/codeeval-strings-and-arrows.html
#       https://www.codeeval.com/open_challenges/203/

import unittest
from ce.c203 import solution


class TestStepwiseWord(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(2, solution('<--<<--<<'))

    def test_provided_2(self):
        self.assertEqual(4, solution('<<>>--><--<<--<<>>>--><'))

    def test_provided_3(self):
        self.assertEqual(0, solution('<-->>'))

    def test_empty(self):
        self.assertEqual(0, solution(''))

    def test_overlapping_right(self):
        self.assertEqual(3, solution('>>-->>-->>-->'))


if __name__ == '__main__':
    unittest.main()
