"""
Changing Money

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/half-dozen-of-greedy-problems.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 3 - greedy algorithms
"""
from a_changing_money import solution


class TestSolution:
    def test_given_1(self):
        assert solution(2) == 2

    def test_given_2(self):
        assert solution(28) == 6

    def test_extra(self):
        assert solution(997) == 102
