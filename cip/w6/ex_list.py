"""
Code in Place 2023 https://codeinplace.stanford.edu/cip3
My notes: https://github.com/egalli64/pythonesque/cip

Week 6: #2 List Practice

Implement the functionality described in the comments
"""


def main():
    # Create a list called `fruit_list` that contains the following fruits:
    # 'apple', 'banana', 'orange', 'grape', 'pineapple'.
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list.
    print('List length is', len(fruit_list))

    # Add 'mango' at the end of the list.
    fruit_list.append('mango')

    # Print the updated list.
    for fruit in fruit_list:
        print(fruit)


if __name__ == "__main__":
    main()
