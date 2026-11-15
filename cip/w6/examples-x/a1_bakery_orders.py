"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Lists of Dictionaries: Bakery Orders
- Print every order with its price.
- Add up the prices and print the total.
- Find the order with the highest price and print its item.
"""
ORDERS: list[dict] = [
    {"item": "croissant", "price": 3},
    {"item": "sourdough", "price": 7},
    {"item": "bagel", "price": 2},
    {"item": "muffin", "price": 4},
]


def main():
    priciest = ORDERS[0]
    total = 0

    for order in ORDERS:
        print(f"{order['item']}: ${order['price']}")
        total += order['price']
        if order["price"] > priciest["price"]:
            priciest = order

    print(f"Total: ${total}")
    print("Most expensive:", priciest["item"])


if __name__ == "__main__":
    main()
