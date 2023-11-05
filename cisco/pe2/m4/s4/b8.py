"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 4 - The os module - interacting with the operating system
 8. LAB The os module
 Function find()
 - given a start path, print the absolute path of any directory in the path with the passed name
"""
import os


def find(path, dir):
    try:
        os.chdir(path)
    except OSError:
        return

    current = os.getcwd()
    print("checking", current)
    for item in os.listdir("."):
        if item == dir:
            print(" Found", dir)
        find(current + "/" + item, dir)


find("cisco/pe2/m4", "b1.py")
