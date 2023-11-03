"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 2 - A short journey from procedural to object approach
 3 The stack - the procedural approach vs. the object-oriented approach
 4 The stack - the object approach
 5 The object approach: a stack from scratch
"""


class Stack:
    """A simple class"""

    def __init__(self):
        self._data = []

    def push(self, val):
        self._data.append(val)

    def pop(self):
        val = self._data[-1]
        del self._data[-1]
        return val


stack = Stack()
print("Stack 'private' data is", stack._data)

stack.push(3)
stack.push(2)
stack.push(1)
print("Stack 'private' data is", stack._data)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print("Stack 'private' data is", stack._data)


class AddingStack(Stack):
    """A derived class"""

    def __init__(self):
        # mandatory call to Stack constructor
        Stack.__init__(self)
        self._sum = 0

    def push(self, val):
        """An override"""
        self._sum += val
        Stack.push(self, val)

    def pop(self):
        """Another override"""
        val = Stack.pop(self)
        self._sum -= val
        return val

    def sum(self):
        return self._sum


a_stack = AddingStack()

for i in range(5):
    a_stack.push(i)
    print("Stack sum is", a_stack.sum())

for i in range(5):
    print("Stack sum is", a_stack.pop())
