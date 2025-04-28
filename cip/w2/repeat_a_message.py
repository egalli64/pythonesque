"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Section Week 2: Repeat a message
"""


def main():
    """Get a string from the user and then print it 10 times"""
    s = input("Please, input a string: ")
    for _ in range(10):
        print(s)


if __name__ == "__main__":
    main()
