"""
Maximizing the Number of Prize Places in a Competition

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 3 - greedy algorithms
"""


def solution(candies):
    assert candies > 0

    unassigned = candies
    results = []
    for i in range(1, candies):
        if unassigned - i <= i:
            results.append(unassigned)
            break
        else:
            results.append(i)
            unassigned -= i

    return len(results), results


if __name__ == '__main__':
    print(solution(int(input())))
