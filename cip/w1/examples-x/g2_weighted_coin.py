"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Random - Weighted Coin
"""
from random import randint


def main():
    flip = randint(1, 10)
    if flip <= 7:
        print("Heads!")
    else:
        print("Tails!")


if __name__ == '__main__':
    main()
