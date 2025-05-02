"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Convert a Fahrenheit temperature to Celsius
"""


def main():
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0
    print("Temperature:" + str(degrees_fahrenheit) + "F = " + str(degrees_celsius) + "C")


if __name__ == "__main__":
    main()
