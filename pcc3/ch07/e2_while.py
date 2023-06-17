"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 7 - User Input and While Loops - Introducing while Loops
"""
print('A for loop:')
for i in range(1, 6):
    print(i)

print("Same by while:")
current_number = 1
while current_number <= 5:
    print(current_number)
    # do not forget to change the loop variable - an infinite loop is lurking here!
    current_number += 1


prompt = "Tell me something, or 'q' to end: "
message = ""
while message != 'q':
    message = input(prompt)
    print(message)

print('Again, with double check on quit')
prompt = "Tell me something, or 'q' to end: "
message = ""
while message != 'q':
    message = input(prompt)
    if message != 'q':
        print(message)

print('Again, using a flag')
prompt = "Tell me something, or 'q' to end: "
active = True
while active:
    message = input(prompt)
    if message == 'q':
        active = False
    else:
        print(message)

print('Again, using break to interrupt the loop')
prompt = "Tell me something, or 'q' to end: "
while True:
    message = input(prompt)
    if message == 'q':
        break
    else:
        print(message)

print('Filter by continue')
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
