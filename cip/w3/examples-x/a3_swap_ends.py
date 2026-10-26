"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Swap Ends
"""


def main():
    line = ["Ana", "Ben", "Cleo", "Dev"]
    print("Before:", line)

    line[0], line[-1] = line[-1], line[0]
    print("After:", line)


if __name__ == "__main__":
    main()
