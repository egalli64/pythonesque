"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Module 2 Section 6 LAB
"""


def exercise_1(x):
    """joy of divisions"""
    return 1 / (x + 1 / (x + 1 / (x + 1 / x)))


print(exercise_1(1) == 0.6000000000000001)
print(exercise_1(10) == 0.09901951266867294)
print(exercise_1(100) == 0.009999000199950014)
print(exercise_1(-5) == -0.19258202567760344)


def exercise_2(hh, mm, delta):
    """end of time"""
    mm += delta
    hh += mm // 60

    mm %= 60
    hh %= 24
    return str(hh) + ':' + str(mm)


print(exercise_2(12, 17, 59) == '13:16')
print(exercise_2(23, 58, 642) == '10:40')
print(exercise_2(0, 1, 2939) == '1:0')
