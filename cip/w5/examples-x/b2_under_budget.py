"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Under Budget
- Ask the user how many dollars they have.
- Loop over MENU and print every item that costs that much or less, with its price.
"""
MENU = {"tea": 2, "coffee": 3, "cookie": 1, "sandwich": 7, "soup": 5, "cake": 4}


def main():
    budget = int(input("How many dollars do you have? "))
    print("You can afford:")
    for item, price in MENU.items():
        if price <= budget:
            print(f"{item} (${price})")


if __name__ == "__main__":
    main()
