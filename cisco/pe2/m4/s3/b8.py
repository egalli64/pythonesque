"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 3 - Working with real files
 8. LAB Character frequency histogram
"""
source = "cisco/pe2/m4/s3/text.txt"

# Counters for each Latin letter: counters[0] is for 'a', counters[25] is for 'z'
counters = [0] * 26

try:
    file = open(source, "rt")
    for line in file:
        for current in line:
            if current.isalpha():
                i = ord(current.lower()) - ord('a')
                counters[i] += 1
    file.close()

    for i, counter in enumerate(counters):
        if counter > 0:
            c = chr(ord('a') + i)
            print(c, "->", counter)
except IOError as ex:
    print("I/O error occurred: ", ex)

