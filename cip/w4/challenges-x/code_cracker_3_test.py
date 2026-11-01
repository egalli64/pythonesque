"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Code Cracker: step 3, decode
"""
from code_cracker_3 import decode


class TestCodeCracker3:
    def test_given_1(self):
        assert decode('phhw ph dw qrrq', 3) == 'meet me at noon'

    def test_given_2(self):
        assert decode('bgdtc', 2) == 'zebra'

    def test_given_3(self):
        assert decode('gdkkn', 25) == 'hello'
