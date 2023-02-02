"""
Justify the Text
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/177/
"""

import unittest
from c177 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('Hello, World!', solution('Hello, World!'))

    def test_provided_2(self):
        text_in = 'The precise 50-digits value of Pi is 3.14159265358979323846264338327950288419716939937510.'
        text_out = 'The         precise         50-digits        value        of        Pi        is\n' \
                   '3.14159265358979323846264338327950288419716939937510.'
        self.assertEqual(text_out, solution(text_in))

    def test_provided_3(self):
        text_in = 'But he who would be a great man ought to regard, not himself or his interests, but what is just,' \
                  ' whether the just act be his own or that of another. Next as to habitations. Such is the tradition.'
        text_out = 'But  he  who would be a great man ought to regard, not himself or his interests,\n' \
                   'but what is just, whether the just act be his own or that of another. Next as to\n' \
                   'habitations. Such is the tradition.'
        self.assertEqual(text_out, solution(text_in))

    def test_extra(self):
        text_in = 'This is the language of naval warfare, and is anything but worthy of extraordinary praise.'
        text_out = 'This  is  the  language  of  naval  warfare,  and  is  anything  but  worthy  of\n' \
                   'extraordinary praise.'
        self.assertEqual(text_out, solution(text_in))


if __name__ == '__main__':
    unittest.main()
