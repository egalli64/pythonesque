"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Times Table: for the integer required by user
"""


def main():
    num = int(input("Which number? "))

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


if __name__ == "__main__":
    main()
