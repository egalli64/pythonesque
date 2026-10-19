"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Random - Estimate Pi
"""
from random import randint

RADIUS = 10000
NUM_POINTS = 100000


def main():
    inside = 0

    for _ in range(NUM_POINTS):
        x = randint(0, RADIUS)
        y = randint(0, RADIUS)
        if is_in_circle(x, y):
            inside += 1

    print(4 * inside / NUM_POINTS)


def is_in_circle(x: int, y: int) -> bool:
    return x * x + y * y <= RADIUS * RADIUS


if __name__ == '__main__':
    main()
