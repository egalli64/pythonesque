"""
Majority Element

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/a-few-divide-and-conquer-problems.html
      http://thisthread.blogspot.com/2018/02/majority-element.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 4 - Divide and Conquer
"""


def solution_naive(data):
    size = len(data)
    for i in range(size // 2 + size % 2):
        current = data[i]
        count = 1
        for j in range(i+1, size):
            if data[j] == current:
                count += 1
        if count > size // 2:
            return True
    return False


def majority(data, left, right):
    size = right - left + 1
    if size < 3:
        return data[left] if data[left] == data[right] else None

    pivot = left + size // 2
    lhs = majority(data, left, pivot)
    rhs = majority(data, pivot + 1, right)

    if not lhs or not rhs:
        return lhs if lhs else rhs
    if lhs == rhs:
        return lhs

    for candidate in (lhs, rhs):
        count = 0
        for i in range(left, right + 1):
            if data[i] == candidate:
                count += 1
        if count > size // 2:
            return candidate
    return None


def solution_dac(data):
    if not data:
        return False
    return True if majority(data, 0, len(data) - 1) else False


def solution_sort(data):
    data.sort()
    half_size = len(data) // 2
    for i in range(half_size + len(data) % 2):
        if data[i] == data[i + half_size]:
            return True
    return False


def solution_hash(data):
    from collections import Counter
    return True if Counter(data).most_common(1)[0][1] > len(data) // 2 else False


def bm_candidate(data):
    result = None
    count = 0
    for element in data:
        if count == 0:
            result = element
            count = 1
        elif element == result:
            count += 1
        else:
            count -= 1

    return result


# Boyer–Moore
def solution_bm(data):
    candidate = bm_candidate(data)
    return True if data.count(candidate) > len(data) // 2 else False


# user changed requisite, the actual element is now required
if __name__ == '__main__':
    input()  # header discarded

    items = [int(x) for x in input().split()]
    print(majority(items, 0, len(items) - 1))
