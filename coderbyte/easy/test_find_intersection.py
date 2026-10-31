"""
Coder-byte Challenges

Source: https://coderbyte.com/challenges
My solutions: https://github.com/egalli64/pythonesque coderbyte folder

Find Intersection
"""
from find_intersection import find_intersection


class TestFindIntersection:
    def test_given_1(self):
        assert find_intersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]) == "1,4,13"

    def test_given_2(self):
        assert find_intersection(["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]) == "1,9,10"
