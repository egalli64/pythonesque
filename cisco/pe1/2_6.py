"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Module 2 Section 6 Interaction with the user
"""
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

anything = input("Enter a number: ")
try:
    something = anything ** 2.0
    print(anything, "to the power of 2 is", something)
except TypeError:
    print('input() returns a string, not a number!')

anything = int(input("Enter an integer: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

anything = float(input("Enter a float: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

# a square:
# top line: +----------+
print("+" + 10 * "-" + "+")
# body x 5: |          |
print(("|" + " " * 10 + "|\n") * 5, end="")
# bottom line as top one
print("+" + 10 * "-" + "+")

