"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Section Week 3: Planetary Weights
- Earthling's weight on Mercury is 37.6% of their weight on Earth, ...
- Write a program that
    Prompts an Earthling to enter their weight on Earth, and the name of a planet
    Prints the calculated weight
"""

# sort of handmade dictionary - stay tuned for a more pythonic solution
MERCURY_FACTOR = 0.376
VENUS_FACTOR = 0.89
MARS_FACTOR = 0.378
JUPITER_FACTOR = 2.36
SATURN_FACTOR = 1.081
URANUS_FACTOR = 0.82
NEPTUNE_FACTOR = 1.14
EARTH_FACTOR = 1.0


def main():
    # 1. ask the user for a weight - convert it to real number on the spot
    earth_weight = float(input("Enter a weight on Earth: "))

    # 2. ask the user for a planet
    planet = input("Enter a planet: ")

    # 3. determine the factor that should be applied
    if planet == "Mercury":
        factor = MERCURY_FACTOR
    elif planet == "Venus":
        factor = VENUS_FACTOR
    elif planet == "Mars":
        factor = MARS_FACTOR
    elif planet == "Jupiter":
        factor = JUPITER_FACTOR
    elif planet == "Saturn":
        factor = SATURN_FACTOR
    elif planet == "Uranus":
        factor = URANUS_FACTOR
    elif planet == "Neptune":
        factor = NEPTUNE_FACTOR
    else:
        # unknown planet - let the user know something strange is going on
        factor = EARTH_FACTOR
        print(
            "I don't know anything of planet "
            + planet
            + ". I assume it is just like Earth."
        )

    # 4. get the weight on the selected planet
    planetary_weight = earth_weight * factor

    # 5. output the result
    print("The equivalent weight on " + planet + ":  " + str(planetary_weight))


if __name__ == "__main__":
    main()
