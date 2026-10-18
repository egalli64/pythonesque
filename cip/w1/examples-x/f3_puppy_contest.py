"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Numbers - Puppy Contest
"""


def main():
    first = int(input("Enter judge 1's score: "))
    second = int(input("Enter judge 2's score: "))
    third = int(input("Enter judge 3's score: "))
    average = (first + second + third) / 3

    print(f"The average score is {average}")


if __name__ == "__main__":
    main()
