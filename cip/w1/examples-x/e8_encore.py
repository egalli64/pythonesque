"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque/cip

Encore: Play the concert finale again for as long as the user keeps asking for an encore.
"""


def main():
    request = input("Type encore to hear the finale again: ")

    while request == "encore":
        print("The band plays the finale!")
        request = input("Type encore to hear it again: ")
    print("The concert is over!")


if __name__ == "__main__":
    main()
