"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Variables Are Not Boxes
"""
a_list = [1, 2, 3]
print("a list:", a_list)
b_list = a_list
print("another reference to the same list:", b_list)
a_list.append(4)
print("change the list from a reference, see the change from the other one:", b_list)


class Gizmo:
    def __init__(self):
        print(f'Gizmo id: {id(self)}')


x = Gizmo()

try:
    # the new Gizmo object is created, but not y
    y = Gizmo() * 10
except TypeError as e:
    print(f"{e!r}")
