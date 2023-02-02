"""
CodeEval Da Vyncy
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/77/
"""
import unittest

from c077 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('O draconian devil! Oh lame saint!', solution('O draconia;conian devil! Oh la;h lame sa;saint!'))

    def test_provided_2(self):
        self.assertEqual('Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, '
                         'sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam '
                         'quaerat voluptatem.',
                         solution('m quaerat voluptatem.;pora incidunt ut labore et d;'
                                  ', consectetur, adipisci velit;olore magnam aliqua;idunt ut labore et dolore magn;'
                                  'uptatem.;i dolorem ipsum qu;iquam quaerat vol;'
                                  'psum quia dolor sit amet, consectetur, a;ia dolor sit amet, conse;'
                                  'squam est, qui do;Neque porro quisquam est, qu;aerat voluptatem.;m eius modi tem;'
                                  'Neque porro qui;, sed quia non numquam ei;lorem ipsum quia dolor sit amet;'
                                  'ctetur, adipisci velit, sed quia non numq;unt ut labore et dolore magnam aliquam qu;'
                                  'dipisci velit, sed quia non numqua;us modi tempora incid;'
                                  'Neque porro quisquam est, qui dolorem i;uam eius modi tem;pora inc;am al'))

if __name__ == '__main__':
    unittest.main()
