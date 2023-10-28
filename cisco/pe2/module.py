"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2: Module 1 Section 3 – Modules and Packages
- A module contains functions, ready for distribution - name should be descriptive
- A package is a module container, to keep them together organically
"""
# The first time a module is imported, its content is implicitly executed

# a module variable, please, consider it as private
_counter = 0

# when run as module, name is the filename (no ext), when run as standalone program, name is "__main__"
print(f"[{__name__}]", "Hello from the module")

def suml(values):
    global _counter
    _counter += 1
    result = 0
    for value in values:
        result += value
    return result


def prodl(values):
    global _counter
    _counter += 1
    result = 1
    for value in values:
        result *= value
    return result

if __name__ == "__main__":
    print(f"[{__name__}]", "Called as a standalone program")

    # Smoke test
    values = [i+1 for i in range(5)]
    print(f"[{__name__}] testing suml:", suml(values) == 15)
    print(f"[{__name__}] testing prodl:", prodl(values) == 120)
else:
    print(f"[{__name__}]", "Called as a module")
