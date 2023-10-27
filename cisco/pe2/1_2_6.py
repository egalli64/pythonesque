"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2: Module 1 Section 2 – Selected Python modules (math, random, platform)
Selected functions from the platform module
"""
import platform as p

print("Platform info (OS) possibly in different formats:", end=' ')
print(f"{p.platform()}, {p.platform(1)}, {p.platform(0, 1)}")

print("Machine info (HW):", p.machine())
print("Processor info:", p.processor())
print("System info:", p.system())
print("[OS] version:", p.version())

print("Python implementation:", p.python_implementation())
print("Python version:", p.python_version_tuple())
