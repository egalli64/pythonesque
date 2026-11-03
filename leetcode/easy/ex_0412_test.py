"""
LeetCode: https://leetcode.com/problemset/
My solutions: https://github.com/egalli64/pythonesque/leetcode

412. Fizz Buzz: https://leetcode.com/problems/fizz-buzz/
"""
from ex_0412 import fizz_buzz


class TestSolution:
    def test_given_1(self):
        assert fizz_buzz(3) == ["1", "2", "Fizz"]

    def test_given_2(self):
        assert fizz_buzz(5) == ["1", "2", "Fizz", "4", "Buzz"]

    def test_given_3(self):
        assert fizz_buzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13",
                                 "14", "FizzBuzz"]
