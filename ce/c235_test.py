"""
Simple or trump
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-simple-or-trump.html
      https://www.codeeval.com/open_challenges/235/
"""

import unittest
from c235 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('2H', solution('AD 2H | H'))

    def test_provided_2(self):
        self.assertEqual('KD KH', solution('KD KH | C'))

    def test_provided_3(self):
        self.assertEqual('JH', solution('JH 10S | C'))


if __name__ == '__main__':
    unittest.main()
