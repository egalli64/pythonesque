"""
Coder-byte Challenges

Source: https://coderbyte.com/challenges
My solutions: https://github.com/egalli64/pythonesque coderbyte folder

Min Window Substring
"""
from min_window_substring import min_window_substring

class TestMinWindowSubstring:
    def test_given_1(self):
        assert min_window_substring(["ahffaksfajeeubsne", "jefaa"]) == "aksfaje"

    def test_given_2(self):
        assert min_window_substring(["aaffhkksemckelloe", "fhea"]) == "affhkkse"
