"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Section Week 3: Mars Weight
- Earthling's weight on Mars is 37.8% of their weight on Earth
- Write a program that prompts an Earthling to enter their weight on Earth and prints their calculated weight on Mars.
"""

MARS_FACTOR = 0.378


def main():
    # 1. ask the user for a weight
    user_input = input("Enter a weight on Earth: ")
    # 2. convert user input in a real number
    earth_weight = float(user_input)
    # 3. get the mars weight from it
    mars_weight = earth_weight * MARS_FACTOR
    # 4. output the result
    print("The equivalent weight on Mars: " + str(mars_weight))
    # 5. extra: rounding to 2 decimal digits
    mars_weight = round(mars_weight, 2)
    print("The equivalent weight on Mars (rounded): " + str(mars_weight))


if __name__ == "__main__":
    main()
