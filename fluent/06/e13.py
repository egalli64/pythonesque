"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Watching the end of an object when no more references point to it
"""
import weakref

s1 = {1, 2, 3}
s2 = s1
print("s2 is an alias of s1:", s1 is s2)


def bye():
    print('...like tears in the rain.')


# bye callback registered on the object referenced by s1
ender = weakref.finalize(s1, bye)
print("The object should be alive:", ender.alive)

del s1
print("The object should still be alive:", ender.alive)

s2 = {}
print("The object shouldn't be alive anymore:", not ender.alive)
