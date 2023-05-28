"""
Code in Place 2023 https://codeinplace.stanford.edu/cip3
My notes: https://github.com/egalli64/pythonesque/cip

Diagnostic 1

Write a console program which asks the user for their height in meters and prints
whether or not they are the correct height to be a NASA astronaut.
"""
def main():
    height = float(input('Enter your height in meters: '))
    if 1.6 < height < 1.9:
        print('Correct height to be an astronaut')
    elif height <= 1.6:
        print('Below minimum astronaut height')
    else:
        print('Above maximum astronaut height')


if __name__ == "__main__":
    main()
