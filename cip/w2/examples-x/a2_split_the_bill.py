"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Numbers - Split the Bill
"""


def main():
    bill = float(input("Enter the total bill: "))
    people = int(input("Enter the number of people: "))
    share = round(bill / people, 2)

    print(f"Each person owes ${share}")


if __name__ == "__main__":
    main()
