"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Star Square
"""


def main():
    size = int(input("Square size: "))

    row = "*" * size
    for _ in range(size):
        print(row)


if __name__ == "__main__":
    main()
