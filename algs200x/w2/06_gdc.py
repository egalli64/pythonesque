# Euclid Greater Common Divisor


def gcd_euclid(a, b):
    if b == 0:
        return a
    return gcd_euclid(b, a % b)


if __name__ == "__main__":
    lhs, rhs = map(int, input().split())
    print(gcd_euclid(lhs, rhs))
