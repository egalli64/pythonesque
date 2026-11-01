"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Code Cracker: step 2, encode
"""
from code_cracker_2 import encode


class TestCodeCracker2:
    def test_given_1(self):
        assert encode('meet me at noon', 3) == 'phhw ph dw qrrq'

    def test_given_2(self):
        assert encode('hello', 1) == 'ifmmp'

    def test_given_3(self):
        assert encode('zebra', 2) == 'bgdtc'

    def test_given_4(self):
        assert encode('attack at dawn', 0) == 'attack at dawn'
