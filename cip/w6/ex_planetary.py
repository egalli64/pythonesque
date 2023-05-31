"""
Code in Place 2023 https://codeinplace.stanford.edu/cip3
My notes: https://github.com/egalli64/pythonesque/cip

Section Week 6 (review from 3): Planetary Weights
- Earthling's weight on Mercury is 37.6% of their weight on Earth, ...
- Write a program that
    Prompts an Earthling to enter their weight on Earth, and the name of a planet
    Prints the calculated weight
"""
FACTORS = {"Mercury": 0.376, "Venus": 0.89, "Mars": 0.378, "Jupiter": 2.36,
           "Saturn": 1.081, "Uranus": 0.82, "Neptune": 1.14}


def main():
    # 1. ask the user for a weight - convert it to real number on the spot
    earth_weight = float(input("Enter a weight on Earth: "))

    # 2. ask the user for a planet
    planet = input("Enter a planet: ")

    # 3. determine the factor that should be applied
    factor = FACTORS.get(planet, 1.0)
    if factor == 1.0:
        # unknown planet - let the user know something strange is going on
        print("I don't know anything of planet " +
              planet + ". I assume it is just like Earth.")

    # 4. get the weight on the selected planet
    planetary_weight = earth_weight * factor

    # 5. output the result
    print(f"The equivalent weight on {planet}: {planetary_weight}")


if __name__ == "__main__":
    main()
