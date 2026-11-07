"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Phone Book
- Start with an empty dictionary of contacts.
- Keep asking for a name and a number until the user presses enter instead of typing a name.
    - Store names in lowercase.
- Print how many contacts were saved.
- Then keep asking who to call until the user presses enter.
- Print their number if they are in the contacts, or a message if they are not.
"""


def main():
    contacts = {}
    print("Add your contacts. Press enter when you are done.")

    while name := input("Name: ").lower():
        contacts[name] = input("Number: ")
    print("Contacts saved:", len(contacts))

    while name := input("Who do you want to call? ").lower():
        if name in contacts:
            print(f"Calling {name} at {contacts[name]}...")
        else:
            print(name, "is not in your contacts.")


if __name__ == "__main__":
    main()
