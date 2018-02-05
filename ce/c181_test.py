"""
Gronsfeld cipher
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/codeeval-gronsfeld-cipher.html
      https://www.codeeval.com/open_challenges/181/
"""

import unittest
from ce.c181 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('EXALTATION', solution('31415;HYEMYDUMPS'))

    def test_provided_2(self):
        self.assertEqual('I love challenges!', solution('45162;M%muxi%dncpqftiix"'))

    def test_provided_3(self):
        self.assertEqual('Test input.', solution('14586214;Uix!&kotvx3'))

    def test_extra(self):
        self.assertEqual('xyz', solution('3; !"'))


if __name__ == '__main__':
    unittest.main()
