"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 6 - Dictionaries - Working with Dictionaries
"""
# create a dictionary
alien = {'color': 'green', 'points': 5}

# accessing value by key
print(alien['color'], alien['points'])
print(f"You just earned {alien['points']} points!")

# adding a k/v pair
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)

# an empty dictionary
alien_0 = {}
print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# change value
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# remove a k/v pair
del alien_0['points']
print(alien_0)

favorite_languages = {'jen': 'python', 'sarah': 'c',
                      'edward': 'rust', 'phil': 'python'}

print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}.")

# KeyError when key is not there
try:
    print(favorite_languages['tom'])
except KeyError:
    print('Tom has no favorite language')

# get()
print(f"Tom's favorite is {favorite_languages.get('tom')}.")

# get() / 2
print(f"Tom's favorite is {favorite_languages.get('tom', 'unknown')}.")
