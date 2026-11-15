"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

elif, and, or, not: Ticket Booth
- ticket_price(age) should return the price for one visitor.
  - under 5 is free, kids under 18 and seniors 65 and over pay $8, and everyone else pays $12
- Loop over the list of visitors and print each visitor's name, age, and price.
- Print the total for the whole group.
"""
VISITORS: list[dict] = [
    {"name": "Ana", "age": 4},
    {"name": "Ben", "age": 16},
    {"name": "Cleo", "age": 35},
    {"name": "Dev", "age": 70},
]


def ticket_price(age: int) -> int:
    if age < 5:
        return 0
    elif age < 18 or age >= 65:
        return 8
    else:
        return 12


def main() -> None:
    total = 0

    for visitor in VISITORS:
        current = ticket_price(visitor["age"])
        print(f"{visitor['name']} ({visitor['age']}): ${current}")
        total += current

    print(f"Total: ${total}")


if __name__ == "__main__":
    main()
