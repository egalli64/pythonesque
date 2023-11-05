"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 3 - Working with real files
 7. Copying files - a simple and functional tool
"""
source = "cisco/pe2/m4/s3/text.txt"
destination = "cisco/pe2/m4/s3/copy.txt"

try:
    src = open(source, "rb")
except IOError as ex:
    print("Cannot open the source file:", ex)
    exit(ex.errno)

try:
    dst = open(destination, "wb")
except Exception as ex:
    print("Cannot create the destination file:", ex)
    src.close()
    exit(ex.errno)

buffer = bytearray(65536)
total = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as ex:
    print("Cannot create the destination file: ", ex)
    exit(ex.errno)
finally:
    print(total, "bytes written to", destination)
    src.close()
    dst.close()
