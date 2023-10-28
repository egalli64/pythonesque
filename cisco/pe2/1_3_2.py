"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2: Module 1 Section 3 – Modules and Packages
- A module contains functions, ready for distribution - name should be descriptive
- A package is a module container, to keep them together organically

1.3.2 Your first module
"""
# being in the same folder, python knows how to import module.py
# see __pycache__ folder, where the python compiled (to python bytecode) module has been placed
import sys
import module as m

print(f"[{__name__}]", "The module _counter is",
      m._counter, "(but I should not access it)")

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(f"[{__name__}] sum list gives", m.suml(zeroes))
print(f"[{__name__}] prod list gives", m.prodl(ones))


# change the Python system path to make extra modules accessible, then import a module from the new extra path
sys.path.append("cisco\\pe2\\modules")
print("Folders in sys.path:", sys.path)

# import should be in the header, but in this case we really need it _after_ sys.path.append()
import module13
