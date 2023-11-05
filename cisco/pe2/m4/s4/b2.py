"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 4 - The os module - interacting with the operating system
 1. Introduction to the os module
 2. Getting information about the operating system
 3. Creating directories in Python
 4. Recursive directory creation
 5. Where am I now?
 6. Deleting directories in Python
"""
import os

print(os.name)

# get the current directory
print("Currently in", os.getcwd())
# create a new directory in the current one
os.mkdir("my_first_directory")
# create a directory branch in the current folder
os.makedirs("my_second_directory/my_third_directory")
# change the current directory
os.chdir("my_second_directory")
print("Currently in", os.getcwd())
# list the content of the current directory
print(os.listdir())
os.chdir("..")
# remove directory
os.rmdir("my_first_directory")
# remove branch directory
os.removedirs("my_second_directory/my_third_directory")
