"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Perimeter of a triangle: Ask for the lengths of the sides and print the perimeter
"""


def main():
    a = float(input("What is the length of side 1? "))
    b = float(input("What is the length of side 2? "))
    c = float(input("What is the length of side 3? "))

    print("The perimeter of the triangle is " + str(a + b + c))


if __name__ == "__main__":
    main()
