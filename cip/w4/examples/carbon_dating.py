"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Program: Carbon Dating
"""

import math

# Half life constant
K = -8266.64


def main():
    """
    Gets user input for a percent of c14 left in a sample
    and then calculates the age of the sample based on that
    information, printing it out to the console.
    """

    # Ask the user to enter the percent c14 left in their sample
    pct_left = float(input("% of natural c14: "))

    # Calculate the age
    age = K * math.log(pct_left / 100)

    # Print the result
    print("Sample is " + str(age) + " years old.")


if __name__ == "__main__":
    main()
