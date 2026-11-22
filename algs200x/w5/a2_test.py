"""
Money Change Again

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/money-change-again.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 5 - Dynamic Programming 1
"""
from a2_money_dp import solution


class TestSolution:
    def test_given_1(self):
        assert solution(2) == 2

    def test_given_2(self):
        assert solution(34) == 9

    def test_extra_1(self):
        assert solution(6) == 2

    def test_extra_2(self):
        assert solution(28) == 7

    def test_extra_3(self):
        assert solution(950) == 238
