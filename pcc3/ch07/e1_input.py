"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 7 - User Input and While Loops - How the input() Function Works
"""
# input() accepts a prompt and return the user input as a string
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

try:
    # let's cast the user input to integer
    age = int(input("How old are you? "))
except:
    print('You should give an integer as you age, I assume you are 6.')
    age = 6

if age < 14:
    print('You are so young!')
else:
    print(f'Are you really {age}?')

# even checker
number = input("Enter an integer, and I'll tell you if it's even or odd: ")
try:
    number = int(number)
    # the operator modulo returns the remainder of the operands division
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
except:
    print(number, 'is not an integer!')
