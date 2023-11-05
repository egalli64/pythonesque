"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 3 - Working with real files
 10. LAB Evaluating students' results
"""


class StudentsDataException(Exception):
    pass


class WrongLine(StudentsDataException):
    def __init__(self, line, filename):
        self.line = line
        self.filename = filename


class FileEmpty(StudentsDataException):
    pass


source = "cisco/pe2/m4/s3/sample.txt"

data = {}

try:
    f = open(source, "rt")
    lines = f.readlines()
    f.close()

    if len(lines) == 0:
        raise FileEmpty()

    for i in range(len(lines)):
        line = lines[i]
        columns = line.split()
        if len(columns) != 3:
            raise WrongLine(i + 1, source)

        student = columns[0] + " " + columns[1]
        try:
            points = float(columns[2])
        except ValueError:
            raise WrongLine(i + 1, source)

        if student in data:
            data[student] += points
        else:
            data[student] = points

    for student in sorted(data.keys()):
        print(f"{student}: {data[student]}")

except IOError as ex:
    print("I/O error occurred: ", ex)
except WrongLine as ex:
    print(f"Line {ex.line} wrong in {ex.filename}")
except FileEmpty:
    print("Source file empty")
