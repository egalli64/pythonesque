# Fizz Buzz
# author: Manny egalli64@gmail.com
# info: http://thisthread.blogspot.com/2017/01/fizz-buzz.html
#       https://www.codeeval.com/open_challenges/1/

import unittest
from c001 import solution


class TestFizzBuzz(unittest.TestCase):

    def test_provided_1(self):
        result = solution('3 5 10 ')
        self.assertEqual('1 2 F 4 B F 7 8 F B ', result)

    def test_provided_2(self):
        result = solution('2 7 15 ')
        self.assertEqual('1 F 3 F 5 F B F 9 F 11 F 13 FB 15 ', result)


if __name__ == '__main__':
    unittest.main()