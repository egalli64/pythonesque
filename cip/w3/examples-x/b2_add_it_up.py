"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Add It Up: print each element in the list, and then the total
"""


def main():
    prices = [4, 12, 3, 8, 5]

    total = 0
    print("Values:", end=' ')
    for price in prices:
        print(price, end=' ')
        total += price

    print("\nTotal:", total)


if __name__ == "__main__":
    main()
