"""
Code in Place Section Leader Application 2024 https://codeinplace.stanford.edu/

My notes: https://github.com/egalli64/pythonesque/cip/karel
"""


def main():
    dictionary = {}
    dictionary["learning"] = "awesome"
    dictionary["coding"] = "fun"
    # ... Fill with more data
    dictionary = remove_keys_containing_string(dictionary, "learning")
    print(dictionary)


def remove_keys_containing_string(dictionary, remove):
    """
    This Python function takes in a dict and a string and
    removes all keys containing that string from the dict
    """
    new_dictionary = {}
    for key in dictionary:
        if remove not in key:
            new_dictionary[key] = dictionary[key]
    return new_dictionary


if __name__ == "__main__":
    main()
