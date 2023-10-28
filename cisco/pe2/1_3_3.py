"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2: Module 1 Section 3 – Modules and Packages
- A module contains functions, ready for distribution - name should be descriptive
- A package is a module container, to keep them together organically

1.3.3 Your first package
"""
# Notice that first packages has to be added to the Python system path, then extra package could be added
# Notice __init__.py in the extra folder, it makes it a package
import sys
sys.path.append("cisco\\pe2\\packages")
import extra.iota

print(extra.iota.funI())

import extra.good.best.sigma as sig
import extra.good.alpha as alp
 
print(sig.funS())
print(alp.funA())
