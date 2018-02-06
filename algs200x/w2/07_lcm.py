# Naive Least Common Multiple calculator


def lcm_naive(a, b):
    for tentative in range(1, a*b):
        if tentative % a == 0 and tentative % b == 0:
            return tentative
    else:
        return a*b


if __name__ == '__main__':
    lhs, rhs = map(int, input().split())
    print(lcm_naive(lhs, rhs))
