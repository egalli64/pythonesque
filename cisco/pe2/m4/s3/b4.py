"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 3 - Working with real files
 4. Dealing with text files: write()
"""
print("*** Write to file, char by char")
try:
    # A new file is created (or reset)
    file = open("cisco/pe2/m4/s3/newtext.txt", "wt")
    for i in range(10):
        line = "line #" + str(i + 1) + "\n"
        for current in line:
            file.write(current)
    file.close()
except IOError as ex:
    print("I/O error occurred: ", ex)
finally:
    print("Done")

print("\n*** Write to file, line by line")

try:
    file = open("cisco/pe2/m4/s3/newtext2.txt", "wt")
    for i in range(10):
        file.write("line #" + str(i + 1) + "\n")
    file.close()
except IOError as ex:
    print("I/O error occurred: ", ex)
finally:
    print("Done")
