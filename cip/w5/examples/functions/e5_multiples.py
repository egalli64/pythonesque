"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Print multiple
print_multiple(message, repeats) should take as parameters a string message to print
and an integer repeats number of times to print message.
"""


def print_multiple(message, repeats):
    for i in range(repeats):
        print(message)


def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)


if __name__ == "__main__":
    main()
