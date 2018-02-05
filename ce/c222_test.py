"""
Black card
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-black-card.html
      https://www.codeeval.com/open_challenges/222/
"""

import unittest
from ce.c222 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('Sara', solution('John     Sara\tTom\nSusan | 3'))

    def test_provided_2(self):
        self.assertEqual('Mary', solution('John Tom Mary | 5'))


if __name__ == '__main__':
    unittest.main()
