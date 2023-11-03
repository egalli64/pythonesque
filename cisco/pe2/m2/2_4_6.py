"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 4 – String in action
 6. LAB - A LED Display

  012 012 012
0 000 5_1 ___
1 ___ 5_1 ___
2 4_2 5_1 666
3 4_2 ___ ___
4 4_2 333 ___
"""
#                0          1          2          3          4
digits = ['1111110', '0110000', '1101101', '1111001', '0110011',
          #      5          6          7          8          9
          '1011011', '1011111', '1110000', '1111111', '1111011']


def print_number(number):
    lines = ['' for _ in range(5)]

    for cipher in number:
        segments = [[' ', ' ', ' '] for _ in range(5)]
        pattern = digits[int(cipher)]
        if pattern[0] == '1':
            segments[0][0] = segments[0][1] = segments[0][2] = '#'
        if pattern[1] == '1':
            segments[0][2] = segments[1][2] = segments[2][2] = '#'
        if pattern[2] == '1':
            segments[2][2] = segments[3][2] = segments[4][2] = '#'
        if pattern[3] == '1':
            segments[4][0] = segments[4][1] = segments[4][2] = '#'
        if pattern[4] == '1':
            segments[2][0] = segments[3][0] = segments[4][0] = '#'
        if pattern[5] == '1':
            segments[0][0] = segments[1][0] = segments[2][0] = '#'
        if pattern[6] == '1':
            segments[2][0] = segments[2][1] = segments[2][2] = '#'

        for i in range(5):
            lines[i] += ''.join(segments[i]) + ' '

    for line in lines:
        print(line)


print_number('123')
print_number('9081726354')
