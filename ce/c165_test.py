"""
Suggest Groups
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-suggest-groups.html
      https://www.codeeval.com/open_challenges/165/
"""

import unittest
from ce.c165 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        data = 'Amira:Isaura,Lizzie,Madalyn,Margarito,Shakira,Un:Driving,Mineral collecting\n' \
                'Elliot:Isaura,Madalyn,Margarito,Shakira:Juggling,Mineral collecting\n' \
                'Isaura:Amira,Elliot,Lizzie,Margarito,Verla,Wilford:Juggling\n' \
                'Lizzie:Amira,Isaura,Verla:Driving,Mineral collecting,Rugby\n' \
                'Madalyn:Amira,Elliot,Margarito,Verla:Driving,Mineral collecting,Rugby\n' \
                'Margarito:Amira,Elliot,Isaura,Madalyn,Un,Verla:Mineral collecting\n' \
                'Shakira:Amira,Elliot,Verla,Wilford:Mineral collecting\n' \
                'Un:Amira,Margarito,Wilford:\n' \
                'Verla:Isaura,Lizzie,Madalyn,Margarito,Shakira:Driving,Juggling,Mineral collecting\n' \
                'Wilford:Isaura,Shakira,Un:Driving\n'
        output = 'Isaura:Driving,Mineral collecting\n' \
                'Lizzie:Juggling\n' \
                'Madalyn:Juggling\n' \
                'Margarito:Driving,Juggling\n' \
                'Shakira:Driving,Juggling\n' \
                'Un:Driving,Mineral collecting\n'
        self.assertEqual(output, solution(data))


if __name__ == '__main__':
    unittest.main()
