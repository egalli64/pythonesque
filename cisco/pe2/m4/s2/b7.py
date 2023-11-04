"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 2 – Files (file streams, file processing, diagnosing stream problems)
 1. Accessing files from Python code
 2. File names
 3. File streams
 4. File handles
 5. Opening the streams
    r (read), w (write, created or reset), a (append or create), r+ (read+write), w+ (write+read), x (create)
    b (binary), t (text - default)
 6. Selecting text and binary modes
 7. Opening the stream for the first time
 8. Pre-opened streams
    sys.stdin, sys.stdout, and sys.stderr
 9. Closing streams
10. Diagnosing stream problems
    see IOError (errno)
"""
# from os import strerror

try:
    stream = open("cisco/pe2/m4/s2/hello.txt", "rt")
    # Processing goes here.
    stream.close()
except IOError as ex:
    print("Cannot open the file:", ex)
    # to get just the specific error message, see os.strerror()
    # print("More info: " + strerror(ex.errno))
finally:
    print("Done")
