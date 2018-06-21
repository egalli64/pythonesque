"""
Partitioning Souvenirs

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/06/partitioning-souvenirs-patched.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 6 - Dynamic Programming 2 - 3-Partition problem
"""


def solution(values):
    third, module = divmod(sum(values), 3)
    if len(values) < 3 or module or max(values) > third:
        return False

    table = [[0] * (len(values) + 1) for _ in range(third + 1)]
    taken = [[0] * (len(values) + 1) for _ in range(third + 1)]

    for i in range(1, third + 1):
        for j in range(1, len(values) + 1):
            if table[i][j-1] == 2:
                table[i][j] = 2
                continue

            if values[j-1] == i:
                table[i][j] = 1 if table[i][j-1] == 0 else 2
                taken[i][j] = j
                continue

            ii = i - values[j-1]

            available = True
            taken_id = taken[ii][j-1]
            if taken_id:
                for jj in range(1, j):
                    if taken[ii][jj] == taken_id:
                        if taken[i][jj]:
                            available = False
                            break

            if ii > 0 and table[ii][j - 1] > 0 and not taken[i][j - 1] and available:
                table[i][j] = 1 if table[i][j - 1] == 0 else 2

                taken[i][j] = j
                taken[i][j-1] = j

                matcher = values[j-1] + values[j-2]
                if taken_id:
                    for jj in range(1, len(values)):
                        if taken[ii][jj] == taken_id:
                            taken[i][jj] = j
                            matcher += values[jj-1]
                if matcher < i:
                    for jj in range(j-2, 0, -1):
                        if taken[i][jj] or matcher + values[jj-1] > i:
                            continue
                        matcher += values[jj-1]
                        taken[i][jj] = j
                        if matcher == i:
                            break
            else:
                table[i][j] = table[i][j - 1]

    return True if table[-1][-1] == 2 else False


if __name__ == '__main__':
    while True:
        input()  # discard header

        items = [x for x in map(int, input().split())]
        print(solution(items))
        input()  # discard tail
