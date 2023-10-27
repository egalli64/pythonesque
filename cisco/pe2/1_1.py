"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Module 1 Section 1 – Introduction to modules in Python
"""
# say to python I want to use the math module (it should be available)
import math
# more module could be imported in a single statement (comma separated list)
# but it is more readable, as so preferred, to have each import standing alone
import sys
# importing names (comma separated list, or *) in the current namespace
from math import pi

# math has to be imported to be found
# sin() should be defined in the namespace math
print('Sin of pi/2 is', math.sin(math.pi/2))


def sin(x):
    """this sin() definition won't clash with math.sin(), they are in different namespaces"""
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print('My (fake) sin of pi/2 gives', sin(pi/2))

from math import sin

print('My (fake) sin now is shadowed by the math one:', sin(pi/2))

# alias, usually to avoid shadowing
from math import cos as std_cos

print('The standard cos of pi is', std_cos(pi))

# alias on module
import math as m
print('The standard cos of pi is', m.cos(pi))
