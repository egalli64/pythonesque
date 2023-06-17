"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 7 - User Input and While Loops - Using a while Loop with Lists and Dictionaries
"""
# Moving Items from One List to Another
unconfirmed_users = ['alice', 'brian', 'candace']
print('Unconfirmed users:', unconfirmed_users)

confirmed_users = []
# until there are unconfirmed users
while unconfirmed_users:
    user = unconfirmed_users.pop()
    print(f"Verifying user: {user.title()}")
    confirmed_users.append(user)

print("The following users have been confirmed:")
for user in confirmed_users:
    print(user.title())

# Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print('Original pets:', pets)
while 'cat' in pets:
    pets.remove('cat')
print('After removing cats:', pets)

# Filling a Dictionary with User Input
responses = {}
while True:
    name = input("Name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response

    repeat = input("Would you like to let another person respond? (y/n) ")
    if repeat == 'n':
        break

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
