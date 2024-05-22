"""
Code in Place 2023 https://codeinplace.stanford.edu/cip3
My notes: https://github.com/egalli64/pythonesque/cip

Diagnostic 4

When the user enters a number which is smaller than their previously entered value, the program is over. Tell the user how long their sequence was.
"""


def main():
    print('Enter a sequence of non-decreasing numbers.')
    prev = float(input('Enter num: '))
    cur = float(input('Enter num: '))
    len = 1
    while cur >= prev:
        len += 1
        prev = cur
        cur = float(input('Enter num: '))
    print('Thanks for playing!')
    print('Sequence length:', len)


if __name__ == "__main__":
    main()
