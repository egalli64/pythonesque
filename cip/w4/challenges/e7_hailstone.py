"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Week 4: Hailstone
--------------------
Pick some positive integer and call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.4
"""


def main():
    n = int(input("Enter a number: "))

    while n != 1:
        if n % 2 == 0:
            print(f"{n} is even, so I take half: ", end=" ")
            n //= 2
            print(n)
        else:
            print(f"{n} is odd, so I make 3n + 1:", end=" ")
            n = n * 3 + 1
            print(n)


if __name__ == "__main__":
    main()
