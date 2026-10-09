"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque/cip

Echo Until Done: Echo back everything the user types, until they type "done".
"""


def main():
    while True:
        message = input("Type a message, or done: ")
        if message == "done":
            break
        else:
            print(message)


if __name__ == "__main__":
    main()
