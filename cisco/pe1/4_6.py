"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Module 4 Section 6 – Tuples and dictionaries
"""
#  A tuple is an immutable sequence type
empty_tuple = ()
print(empty_tuple)

one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,
print(one_element_tuple_1)
print(one_element_tuple_2)

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

my_tuple = (1, 10, 100)
print("A tuple:", my_tuple)

t1 = my_tuple + (1000, 10000)
print("Cons tuple by +:", t1)
t2 = my_tuple * 3
print("Cons tuple by *:", t2)
print("Using len() on a tuple:", len(t2))
print("Check existence by in", 10 in my_tuple)
print("Check if not existing by not in", -10 not in my_tuple)

# tuple's elements can be variables
var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)
print("Three tuples:", t1, t2, t3)

t1, t2, t3 = t2, t3, t1

print("Three tuples swapped:", t1, t2, t3)

# 4.6.3 Dictionaries
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

print("Value for cat:", dictionary['cat'])
print("Value for Suzy:", phone_numbers['Suzy'])
try:
    print(phone_numbers['president'])
except KeyError:
    print("Missing key!")

words = ['cat', 'lion', 'horse']
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

# 4.6.4 Dictionary methods and functions
print("Looping by keys()")
for key in dictionary.keys():
    print(key, "->", dictionary[key])
print("--")

print("Looping by items()")
for english, french in dictionary.items():
    print(english, "->", french)
print("--")

print("Looping on sorted values()")
for french in sorted(dictionary.values()):
    print(french)
print("--")

dictionary['cat'] = 'minou'
print("Value for cat changed:", dictionary)

dictionary['swan'] = 'cygne'
print("New pair inserted", dictionary)

dictionary.update({"duck": "canard"})
print("New pair by update()", dictionary)

del dictionary['dog']
print("Pair removed by del", dictionary)

dictionary.popitem()
print("Last pair removed popitem()", dictionary)

# 4.6.5 Tuples and dictionaries can work together - evaluate student average scores
school_class = {}

while True:
    name = input("Enter the student name: ")
    if name == '':
        break

    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
        break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

# tuple()
my_tuple = tuple((1, 2, "string"))
print(my_tuple)

my_list = [2, 4, 6]
print(my_list, type(my_list))
tup = tuple(my_list)
print(tup, type(tup))

# list()
my_list = list(tup)
print(my_list, type(my_list))
