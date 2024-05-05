"""
Code in Place 2023 https://codeinplace.stanford.edu/cip3
My notes: https://github.com/egalli64/pythonesque/cip

Program: Liftoff
--------------------
Countdown from 10 to 1 and then output Liftoff!
"""


def main():
    for i in range(10):
        print(10 - i)
    print("Liftoff!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
