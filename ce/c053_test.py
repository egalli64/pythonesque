"""
CodeEval Repeated Substring
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/53/
"""
import unittest
from c053 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('an', solution('banana'))

    def test_provided_2(self):
        self.assertEqual('NONE', solution('am so uniq'))

if __name__ == '__main__':
    unittest.main()
