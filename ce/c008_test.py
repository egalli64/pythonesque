"""
CodeEval Reverse Words
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/codeeval-reverse-words.html
      https://www.codeeval.com/open_challenges/8/
"""
import unittest
from c008 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('World Hello', solution('Hello World'))

if __name__ == '__main__':
    unittest.main()
