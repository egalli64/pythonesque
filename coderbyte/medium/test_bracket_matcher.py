"""
Coder-byte Challenges

Source: https://coderbyte.com/challenges
My solutions: https://github.com/egalli64/pythonesque coderbyte folder

Bracket Matcher
"""
from bracket_matcher import bracket_matcher


class TestTreeConstructor():
    def test_given_1(self):
        assert bracket_matcher("(coder)(byte))") == 0

    def test_given_2(self):
        assert bracket_matcher("(c(oder)) b(yte)") == 1
