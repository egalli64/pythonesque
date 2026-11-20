"""
Improving Quick Sort

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/a-few-divide-and-conquer-problems.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 4 - Divide and Conquer
"""
from c1_quick import solution

EXPECTED_TEST_50_000 = [x for x in range(11) for _ in range(50000)]


class TestSolution:
    def test_given(self):
        data = [2, 3, 9, 2, 2]
        solution(data)
        assert data == [2, 2, 2, 3, 9]

    def test_50_000(self):
        data = [x for x in range(10, -1, -1)] * 50000
        solution(data)
        assert data == EXPECTED_TEST_50_000
