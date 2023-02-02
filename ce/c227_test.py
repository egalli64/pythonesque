"""
Real fake
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-real-fake.html
      https://www.codeeval.com/open_challenges/227/
"""

import unittest
from c227 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('Fake', solution('9999 9999 9999 9999'))

    def test_provided_2(self):
        self.assertEqual('Real', solution('9999 9999 9999 9993'))


if __name__ == '__main__':
    unittest.main()
