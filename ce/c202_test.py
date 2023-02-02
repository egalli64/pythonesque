# Stepwise word
# author: Manny egalli64@gmail.com
# info: http://thisthread.blogspot.com/2017/01/codeeval-stepwise-word.html
#       https://www.codeeval.com/open_challenges/202/

import unittest
from c202 import solution


class TestStepwiseWord(unittest.TestCase):

    def test_provided_1(self):
        result = solution('cat dog hello')
        self.assertEqual('h *e **l ***l ****o', result)

    def test_provided_2(self):
        result = solution('stop football play')
        self.assertEqual('f *o **o ***t ****b *****a ******l *******l', result)

    def test_provided_3(self):
        result = solution('music is my life')
        self.assertEqual('m *u **s ***i ****c', result)


if __name__ == '__main__':
    unittest.main()
