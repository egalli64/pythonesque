"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 8 - Functions - Return Values
"""


def format_name(first_name, last_name):
    """A function returning a string, a full name neatly formatted"""
    return f"{first_name} {last_name}".title()


musician = format_name('jimi', 'hendrix')
print(musician)


def format_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted"""
    return f"{first_name} {middle_name} {last_name}".title()


musician = format_name('john', 'lee', 'hooker')
print(musician)


def format_full_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = format_full_name('jimi', 'hendrix')
print(musician)
musician = format_full_name('john', 'hooker', 'lee')
print(musician)


def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix')
print(musician)
musician = build_person('jimi', 'hendrix', 27)
print(musician)
