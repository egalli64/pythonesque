"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 8 – Useful exceptions
 2. LAB Reading ints safely
"""


def read_int(prompt, min, max):
    while True:
        try:
            value = int(input(prompt))
            if value >= min and value <= max:
                return value
            else:
                print(f"Error: the value is not in range [{min} .. {max}]")
        except ValueError:
            print("Error: wrong input")


v = read_int("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)
