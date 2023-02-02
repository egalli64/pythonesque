"""
Burrows-Wheeler transform
author: Manny egalli64@gmail.com
info: https://www.codeeval.com/open_challenges/184/
      http://thisthread.blogspot.com/2017/02/codeeval-burrows-wheeler-transform.html
"""

import unittest
from c184 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo$',
            solution('oooooooo$  ffffffff     ffffffffuuuuuuuuaaaaaaaallllllllbbBbbBBb'))

    def test_provided_2(self):
        self.assertEqual('James while John had had had had had had had had had had had a better effect on the teacher$',
            solution('edarddddddddddntensr$  ehhhhhhhhhhhJ aeaaaaaaaaaaalhtf thmbfe           tcwohiahoJ eeec t e '))

    def test_provided_3(self):
        self.assertEqual('Neko no ko koneko, shishi no ko kojishi$', solution('ooooio,io$Nnssshhhjo  ee  o  nnkkkkkkii '))

    def test_extra(self):
        self.assertEqual('easy-peasy$', solution('yyeep$-aass'))


if __name__ == '__main__':
    unittest.main()
