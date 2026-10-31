"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Vowel Hider: step 1, hide_vowels()
"""
from vowel_hider_1 import hide_vowels


class TestHideVowels:
    def test_given_1(self):
        assert hide_vowels('banana') == 'b*n*n*'

    def test_given_2(self):
        assert hide_vowels('meet me at noon') == 'm**t m* *t n**n'

    def test_given_3(self):
        assert hide_vowels('rhythm') == 'rhythm'

    def test_given_4(self):
        assert hide_vowels('aeiou') == '*****'
