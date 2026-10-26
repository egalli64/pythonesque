"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Grocery List: generate list from user input
"""


def main():
    groceries = []

    for _ in range(3):
        groceries.append(input("Add an item: "))

    print(f"In your list, {groceries}, there are {len(groceries)} items")
    print("The first one is", groceries[0])


if __name__ == "__main__":
    main()
