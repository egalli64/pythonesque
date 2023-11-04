"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 3 - Working with real files
 5. What is a bytearray?
 6. How to read bytes from a stream
"""
# bytearray, each element has a value in [0..255]
data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

print("[ ", end="")
for current in data:
    print(hex(current), end=" ")
print("]")

print("Writing to binary file")
try:
    bf = open("cisco/pe2/m4/s3/file.bin", "wb")
    bf.write(data)
    bf.close()
except IOError as ex:
    print("I/O error occurred: ", ex)
finally:
    print("Done")

print("Reading from binary file in a buffer")

deserialized = bytearray(10)

try:
    bf = open("cisco/pe2/m4/s3/file.bin", "rb")
    bf.readinto(deserialized)
    bf.close()

    for current in data:
        print(hex(current), end=" ")
    print()
except IOError as ex:
    print("I/O error occurred: ", ex)
finally:
    print("Done")

print("Reading all from binary file")

try:
    bf = open("cisco/pe2/m4/s3/file.bin", "rb")
    data = bytearray(bf.read())
    bf.close()

    for current in data:
        print(hex(current), end=" ")
    print()
except IOError as ex:
    print("I/O error occurred: ", ex)
finally:
    print("Done")

print("Reading a sized chunk from binary file")

try:
    bf = open("cisco/pe2/m4/s3/file.bin", "rb")
    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(hex(b), end=" ")
    print()
except IOError as ex:
    print("I/O error occurred: ", ex)
finally:
    print("Done")
