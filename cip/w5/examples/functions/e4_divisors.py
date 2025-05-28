"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Print divisor
define print_divisors(num) that prints all num's divisors
"""


def main():
    num = int(input("Enter a number: "))
    print_divisors(num)


def print_divisors(num):
    print("Here are the divisors of", num)
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)


if __name__ == "__main__":
    main()
