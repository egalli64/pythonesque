"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 3 - Working with real files
 9. LAB Sorted character frequency histogram
"""
source = "cisco/pe2/m4/s3/text.txt"

# map each char in [a..z] with its frequency
counters = {chr(ord("a") + i): 0 for i in range(26)}

try:
    file = open(source, "rt")
    for line in file:
        for current in line:
            if current.isalpha():
                counters[current.lower()] += 1
    file.close()

    file = open(source + ".hist", "wt")
    for current in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):
        frequency = counters[current]
        if frequency > 0:
            file.write(f"{current} -> {frequency}\n")
    file.close()
except IOError as ex:
    print("I/O error occurred: ", ex)
