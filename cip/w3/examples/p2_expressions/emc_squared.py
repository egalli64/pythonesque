"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

E=mc^2: ask the user for mass, give the energy
"""

# Speed of light in m/s
C = 299_792_458


def main():
    mass = float(input("Enter kilos of mass: "))

    energy = mass * C**2

    print("e = m * C^2...")
    print("m = " + str(mass) + " kg")
    print("C = " + str(C) + " m/s")
    print(str(energy) + " joules of energy!")


if __name__ == "__main__":
    main()
