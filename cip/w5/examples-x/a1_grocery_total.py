"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Grocery Total
- Keep asking the user for items until they press enter without typing anything.
- Lowercase each item, because every key in PRICES is lowercase.
- If the item is in PRICES, print what it costs and add it to the total.
- If it is not, print a polite message and keep going.
- At the end, print the total.
"""
PRICES = {"apple": 1, "bread": 3, "milk": 2, "cheese": 5, "eggs": 4}


def main():
    total = 0

    while True:
        item = input("Item: ").lower()
        if not item:
            break
        elif item in PRICES:
            print(f"{item} costs ${PRICES[item]}")
            total += PRICES[item]
        else:
            print(f"Sorry, we do not sell {item}.")

    print(f"Your total is ${total}.")


if __name__ == "__main__":
    main()
