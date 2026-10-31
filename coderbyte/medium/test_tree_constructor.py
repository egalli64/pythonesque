"""
Coder-byte Challenges

Source: https://coderbyte.com/challenges
My solutions: https://github.com/egalli64/pythonesque coderbyte folder

Tree Constructor
"""
from tree_constructor import tree_constructor


class TestTreeConstructor():
    def test_given_1(self):
        assert tree_constructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]) == "true"

    def test_given_2(self):
        assert tree_constructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"]) == "false"

    def test_given_3(self):
        assert tree_constructor(["(2,5)", "(2,6)"]) == "false"
