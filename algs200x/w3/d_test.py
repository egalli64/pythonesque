"""
Collecting Signatures

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/half-dozen-of-greedy-problems.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 3 - greedy algorithms
"""
from d_signatures import solution


class TestSolution:
    def test_given_1(self):
        assert solution([(1, 3), (2, 5), (3, 6)]) == (1, [3])

    def test_given_2(self):
        assert solution([(4, 7), (1, 3), (2, 5), (5, 6)]) == (2, [3, 6])

    def test_extra(self):
        with open("algs200x/w3/d_signatures.in") as file:
            size = int(next(file))

            items = []
            for i in range(size):
                lhs, rhs = map(int, next(file).split())
                items.append((lhs, rhs))

        size, result = solution(items)
        assert size == 68
        assert result == [4540685, 17791449, 42730821, 57675158, 69257274, 87685143, 111278931, 131105794, 150811455,
                          153224903, 180214319, 195339444, 205355137, 221513640, 239842876, 240853681, 245482970,
                          268497305, 290089156, 293793390, 308190293, 316708899, 329142564, 352262601, 360288494,
                          364499571, 396976427, 404785508, 409648764, 418906067, 429266086, 442569910, 452696819,
                          464143707, 469104057, 486563665, 498486555, 505350048, 537888238, 543254495, 554995522,
                          577289076, 584012773, 602911042, 634355270, 644142989, 660392634, 666562291, 682951728,
                          714157315, 736936164, 757759511, 771009814, 792248030, 798695268, 817642716, 843526369,
                          851852947, 867676334, 897199026, 911975174, 915320114, 925541061, 932525735, 958828493,
                          973788153, 985479570, 999257764]
