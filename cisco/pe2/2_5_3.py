"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 5 – Four simple programs
 3. The Numbers Processor
"""


def adder(line):
    try:
        return sum([float(value) for value in line.split()])
    except:
        return 0


sample = '1 2 3'
print(f'Adding {sample} gives', adder(sample))
print('Adding an empty line gives', adder(''))
print('Adding an wrong line gives', adder('mistake'))
