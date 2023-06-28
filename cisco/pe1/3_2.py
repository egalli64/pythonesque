"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Module 3 Section 2 Loops in Python
"""
# Example 1: Get the largest number
import time
largest_number = 0
number = int(input("Enter an integer (0 to stop): "))

# If the number is not equal to -1, continue.
while number != 0:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Next: "))

# Print the largest number.
print("The largest number is:", largest_number)


# Example 2: Count odd / even numbers
odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number (0 to stop): "))

# implicit: 0 terminates execution
while number:
    # Check if the number is odd (implicit: not equal to zero)
    if number % 2:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Next: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

# Example 3: count down
counter = 5

# implicit: count not zero
while counter:
    print("Inside the loop:", counter)
    counter -= 1
print("Outside the loop:", counter)


# lab 3 2 4: Guess the secret number"""
SECRET_NUMBER = 777
guess = 0

while guess != SECRET_NUMBER:
    guess = int(input('Guess my integer: '))

print('Well done!')

# Example 4: for loops
print('Loop in range 5')
for i in range(5):
    print(i)

print('Loop in range 2, 8')
for i in range(2, 8):
    print("The value of i is currently", i)

print('Loop in range 2, 8, step 3')
for i in range(2, 8, 3):
    print("The value of i is currently", i)

power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

# Lab 3.2.7 counting mississippily

for i in range(1, 6):
    print(i, 'Mississippi')
    time.sleep(1)

# Example 5: break / continue
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter an integer (0 to stop): "))
    if number == 0:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

# Lab 3.2.9 - loop until the user input "chupacabra" then print "You've successfully left the loop."
while True:
    word = input('Exit word is ... ')
    if word == 'chupacabra':
        break
print("You've successfully left the loop.")

# Lab 3.2.10 - input a string, output it uppercase, without A, E, I, O, or U

word = input('A string (with many vowels): ')
word = word.upper()
for letter in word:
    if letter in {'A', 'E', 'I', 'O', 'U'}:
        continue
    print(letter, end=' ')
print()

# while - else
i = 1
print('while - else')
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

print('Never entering the loop')
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

# for - else
print('for - else')
for i in range(5):
    print(i)
else:
    print("else:", i)

print('for - else never entering the loop')
for i in range(2, 1):
    print(i)
else:
    print("else:", i)

# Lab 3.2.14 - read the number of blocks, output the height of the pyramid that can be built
blocks = int(input('Number of blocks: '))
height = 0
while blocks > height:
    height += 1
    blocks -= height
print('The height of the pyramid: ', height)

# Lab 3.2.15 - Collatz's hypothesis
"""
    take any non-negative and non-zero integer number and name it c0;
    if it's even, evaluate a new c0 as c0 ÷ 2;
    otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
    if c0 ≠ 1, go back to point 2.
"""
c0 = int(input('c0 = '))
step = 0
while c0 != 1:
    step += 1
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = 3 * c0 + 1
    print(c0)
else:
    print("steps =", step)
