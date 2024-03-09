"""
Code in Place Section Leader Application 2024 https://codeinplace.stanford.edu/

My notes: https://github.com/egalli64/pythonesque/cip/karel
"""

def main():
    """
    Double the input until reaching 100
    """
    curr_value = int(input("Enter a number: "))
    while curr_value < 100:
        curr_value *= 2
        print(curr_value)


if __name__ == "__main__":
    main()
