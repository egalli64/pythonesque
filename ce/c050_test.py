"""
CodeEval String Substitution
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/50/
"""
import unittest
from c050 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('11100110', solution('10011011001;0110,1001,1001,0,10,11'))

    def test_two_dozens(self):
        self.assertEqual('11111101111111111110111110', solution('10100101101110011000;10,111,00,10,010,00'))

    def test_longer(self):
        self.assertEqual('101000011111110101001110101110001010101011011111001000111111100', solution('1001010100001001101000111101011100010011010101101111100100010000100;011001,00,0011,01,100101,101000,01100,1001,10000,111111'))



if __name__ == '__main__':
    unittest.main()
