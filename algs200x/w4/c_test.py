"""
Improving Quick Sort

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/a-few-divide-and-conquer-problems.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 4 - Divide and Conquer
"""
from algs200x.w4.c_quick import solution_quick, solution_quick3


class TestSolution:
    def test_quick_1(self):
        data = [2, 3, 9, 2, 2]
        solution_quick(data)
        assert data == [2, 2, 2, 3, 9]

    def test_quick_2(self):
        data = [x for x in range(10, -1, -1)] * 100000
        solution_quick(data)
        expected = [x for x in range(11) for _ in range(100000)]
        assert data == expected

    def test_quick3_1(self):
        data = [2, 3, 9, 2, 2]
        solution_quick3(data)
        assert data == [2, 2, 2, 3, 9]

    def test_quick3_2(self):
        data = [x for x in range(10, -1, -1)] * 100000
        solution_quick3(data)
        expected = [x for x in range(11) for _ in range(100000)]
        assert data == expected
