"""
Trick or Treat
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-trick-or-treat.html
      https://www.codeeval.com/
"""

import unittest
from ce.c220 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(4, solution('Vampires: 1, Zombies: 1, Witches: 1, Houses: 1'))

    def test_provided_2(self):
        self.assertEqual(36, solution('Vampires: 3, Zombies: 2, Witches: 1, Houses: 10'))


if __name__ == '__main__':
    unittest.main()
