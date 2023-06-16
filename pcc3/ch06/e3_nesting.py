"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 6 - Dictionaries - Nesting
"""
# list of dictionaries
aliens = [
    {'color': 'green', 'points': 5},
    {'color': 'yellow', 'points': 10},
    {'color': 'red', 'points': 15}
]
for alien in aliens:
    print(alien)

# alien generation
aliens = []
for alien_number in range(30):
    aliens.append({'color': 'green', 'points': 5, 'speed': 'slow'})

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# (possibly) change some alien
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# list in dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza with")
for topping in pizza['toppings']:
    print(f"\t{topping}")

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language(s):")
    for language in languages:
        print(f"\t{language.title()}")

# dictionary in dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
print('\nUsers:')
for username, user_info in users.items():
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"{username}: {full_name.title()} - {location.title()}")
