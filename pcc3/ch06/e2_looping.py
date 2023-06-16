"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 6 - Dictionaries - Looping Through a Dictionary
"""
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

# looping on each k/v pair by items()
for key, value in user_0.items():
    print(f"Key: {key}", f"Value: {value}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# naming k/v in more readable way
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# looping on all keys()
for name in favorite_languages.keys():
    print(name.title())

# given a list of friends
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    # for each dictionary key that is in the friend list ...
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# if k is not a key in the dictionary ...
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# looping on sorted keys()
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# looping on values()
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# using set() to get rid of duplicates
print("The following languages have been mentioned (no duplicates - no order):")
for language in set(favorite_languages.values()):
    print(language.title())

# set definition
languages = {'python', 'rust', 'python', 'c'}
print("Set representation is close to dictionary one", languages)
