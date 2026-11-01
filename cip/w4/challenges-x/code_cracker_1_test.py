"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Code Cracker: step 1, shift_letter
"""
from code_cracker_1 import shift_letter


class TestCodeCracker1:
    def test_given_1(self):
        assert shift_letter('c', 3) == 'f'

    def test_given_2(self):
        assert shift_letter('z', 1) == 'a'

    def test_given_3(self):
        assert shift_letter('a', 25) == 'z'

    def test_given_4(self):
        assert shift_letter('m', 0) == 'm'
