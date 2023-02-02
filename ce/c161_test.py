"""
Game of Life
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-game-of-life.html
      https://www.codeeval.com/open_challenges/161/
"""

import unittest
from c161 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        data = '.........*\n' \
               '.*.*...*..\n' \
               '..........\n' \
               '..*.*....*\n' \
               '.*..*...*.\n' \
               '.........*\n' \
               '..........\n' \
               '.....*..*.\n' \
               '.*....*...\n' \
               '.....**...\n'
        output = '..........\n' \
                 '...*......\n' \
                 '..*.*.....\n' \
                 '..*.*.....\n' \
                 '...*......\n' \
                 '..........\n' \
                 '..........\n' \
                 '..........\n' \
                 '..........\n' \
                 '..........\n'
        self.assertEqual(output, solution(data))


if __name__ == '__main__':
    unittest.main()
