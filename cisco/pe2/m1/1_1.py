"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2: Module 1 Section 1 – Introduction to modules in Python
"""
# say to python I want to use the math module (it should be available)
import math as m
from math import cos as std_cos
from math import sin
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
    """won't clash with math.sin(), since they are in different namespaces"""
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print('My sin() of pi/2 gives', sin(pi/2))


print('My sin() now is shadowed by the math one:', sin(pi/2))

# alias, usually to avoid shadowing

print('The standard cos of pi is', std_cos(pi))

# alias on module, usually for shorter names in code
print('The standard cos of pi is', m.cos(pi))
