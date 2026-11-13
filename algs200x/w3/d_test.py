"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w3

Week 3 - greedy algorithms: Collecting Signatures
"""
from d_signatures import solution


class TestSolution:
    def test_given_1(self):
        assert solution([(1, 3), (2, 5), (3, 6)]) == [3]

    def test_given_2(self):
        assert solution([(4, 7), (1, 3), (2, 5), (5, 6)]) == [3, 6]

    def test_extra(self):
        with open("algs200x/w3/d_signatures.in") as file:
            size = int(next(file))
            items = [tuple(map(int, next(file).split())) for _ in range(size)]

        assert solution(items) == [4540685, 17791449, 42730821, 57675158, 69257274, 87685143, 111278931, 131105794,
                                   150811455, 153224903, 180214319, 195339444, 205355137, 221513640, 239842876,
                                   240853681, 245482970, 268497305, 290089156, 293793390, 308190293, 316708899,
                                   329142564, 352262601, 360288494, 364499571, 396976427, 404785508, 409648764,
                                   418906067, 429266086, 442569910, 452696819, 464143707, 469104057, 486563665,
                                   498486555, 505350048, 537888238, 543254495, 554995522, 577289076, 584012773,
                                   602911042, 634355270, 644142989, 660392634, 666562291, 682951728, 714157315,
                                   736936164, 757759511, 771009814, 792248030, 798695268, 817642716, 843526369,
                                   851852947, 867676334, 897199026, 911975174, 915320114, 925541061, 932525735,
                                   958828493, 973788153, 985479570, 999257764]
