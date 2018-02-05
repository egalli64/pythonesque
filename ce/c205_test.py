"""
Clean up the words
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-clean-up-words.html
      https://www.codeeval.com/open_challenges/205/
"""
import unittest
from ce.c205 import solution


class TestStepwiseWord(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('hello world', solution('(--9Hello----World...--)'))

    def test_provided_2(self):
        self.assertEqual('can you', solution('Can 0$9 ---you~'))

    def test_provided_3(self):
        self.assertEqual('what are you doing', solution('13What213are;11you-123+138doing7'))

    def test_garbage(self):
        self.assertEqual('', solution('7/8§§?'))


if __name__ == '__main__':
    unittest.main()
