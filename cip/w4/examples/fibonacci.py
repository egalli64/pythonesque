"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Print the terms in the Fibonacci sequence, starting with Fib(0) up to the biggest Fibonacci less than 10,000
"""

MAX = 10_000


def main():
    cur = 0
    next = 1
    while cur <= MAX:
        print(cur)
        temp = cur + next
        cur = next
        next = temp


if __name__ == "__main__":
    main()
