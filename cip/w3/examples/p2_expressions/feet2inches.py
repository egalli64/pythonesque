"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

feet2inches: converts feet to inches
"""

# 1 foot is 12 inches
INCHES_IN_FOOT = 12


def main():
    feet = float(input("Enter number of feet: "))
    inches = feet * INCHES_IN_FOOT
    print("That is", inches, "inches!")


if __name__ == "__main__":
    main()
