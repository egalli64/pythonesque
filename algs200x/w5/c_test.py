"""
Computing the Edit Distance Between Two Strings

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/computing-edit-distance-between-two.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 5 - Dynamic Programming 1
"""
from c_edit_distance import solution_dp


class TestSolution:
    def test_given_1(self):
        assert solution_dp('ab', 'ab') == 0

    def test_given_2(self):
        assert solution_dp('short', 'ports') == 3

    def test_given_3(self):
        assert solution_dp('editing', 'distance') == 5

    def test_extra(self):
        assert solution_dp('a', 'abc') == 2

    def test_file(self):
        with open('algs200x/w5/c_test.py') as file:
            lhs = next(file)
            rhs = next(file)
        assert solution_dp(lhs, rhs) == 47
