"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 3 - Working with real files
 1. Processing text files
 2. readline()
 3. readlines()
"""
print("\n*** Reading a file char by char")

try:
    counter = 0
    stream = open("cisco/pe2/m4/s3/text.txt", "rt")
    current = stream.read(1)
    while current != "":
        print(current, end="")
        counter += 1
        current = stream.read(1)
    stream.close()
    print("\n\nCharacters in file:", counter)
except IOError as ex:
    print("I/O error occurred: ", ex)

print("\n*** Reading a file in a single shot")

try:
    counter = 0
    stream = open("cisco/pe2/m4/s3/text.txt", "rt")
    content = stream.read()
    for current in content:
        print(current, end="")
        counter += 1
    stream.close()
    print("\n\nCharacters in file:", counter)
except IOError as ex:
    print("I/O error occurred: ", ex)

print("\n*** Reading a file line by line")

try:
    char_counter = line_counter = 0
    stream = open("cisco/pe2/m4/s3/text.txt", "rt")
    line = stream.readline()
    while line != "":
        line_counter += 1
        for current in line:
            print(current, end="")
            char_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCharacters in file:", char_counter)
    print("Lines in file:     ", line_counter)
except IOError as ex:
    print("I/O error occurred: ", ex)

print("\n*** Reading a file by chunks of lines")

try:
    char_count = line_count = 0
    stream = open("cisco/pe2/m4/s3/text.txt", "rt")
    lines = stream.readlines(3)
    while len(lines) != 0:
        for line in lines:
            line_count += 1
            for current in line:
                print(current, end="")
                char_count += 1
        lines = stream.readlines(3)
    stream.close()
    print("\n\nCharacters in file:", char_count)
    print("Lines in file:     ", line_count)
except IOError as ex:
    print("I/O error occurred: ", ex)

print("\n*** Iterating on the file stream (line by line)")

try:
    char_count = line_count = 0
    with open("cisco/pe2/m4/s3/text.txt", "rt") as stream:
        for line in stream:
            line_count += 1
            for current in line:
                print(current, end="")
                char_count += 1

    print("\n\nCharacters in file:", char_count)
    print("Lines in file:     ", line_count)
except IOError as ex:
    print("I/O error occurred: ", ex)
