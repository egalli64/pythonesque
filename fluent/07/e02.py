"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

The built-in sorted()
"""
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print("a list of fruits:", fruits)
print("naturally sorted fruits:", sorted(fruits))

# sorted() is a HOF, accept a function as key argument - here the built-in len()
fruits_by_len = sorted(fruits, key=len)
print("fruits sorted by len:", fruits_by_len)


# any suitable function could be used as HOF argument
def reverse(word):
    """Reverse the passed word"""
    return word[::-1]


print("reversing 'banana' gives", reverse("banana"))
print("fruits sorted by reverse():", sorted(fruits, key=reverse))
