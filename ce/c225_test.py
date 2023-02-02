"""
Testing
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-testing.html
      https://www.codeeval.com/open_challenges/225/
"""

import unittest
from c225 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('Low', solution('Heelo Codevval | Hello Codeeval'))

    def test_provided_2(self):
        self.assertEqual('Critical', solution('hELLO cODEEVAL | Hello Codeeval'))

    def test_provided_3(self):
        self.assertEqual('Done', solution('Hello Codeeval | Hello Codeeval'))


if __name__ == '__main__':
    unittest.main()
