"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Anton is 21 years old.
Beth is 6 years older than Anton.
Chen is 20 years older than Beth.
Drew is as old as Chen's age plus Anton's age.
Ethan is the same age as Chen.

How old are they?
"""


def main():
    anton = 21
    print("Anton is " + str(anton))

    beth = anton + 6
    print("Beth is " + str(beth))

    chen = beth + 20
    print("Chen is " + str(chen))

    drew = chen + anton
    print("Drew is " + str(drew))

    ethan = chen
    print("Ethan is " + str(ethan))


if __name__ == "__main__":
    main()
