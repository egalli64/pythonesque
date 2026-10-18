"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Numbers - Even or Odd
"""


def main():
    num = int(input("Enter a number: "))

    print(num, "is", end=" ")
    if num % 2 == 0:
        print("even!")
    else:
        print("odd!")


if __name__ == "__main__":
    main()
