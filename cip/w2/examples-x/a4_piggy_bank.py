"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Numbers - Piggy Bank
"""
TARGET = 10


def main():
    total = 0

    while total < TARGET:
        amount = float(input("Enter an amount to add: "))
        total += amount
        print(f"You have saved ${total}")

    print("You saved enough!")


if __name__ == "__main__":
    main()
