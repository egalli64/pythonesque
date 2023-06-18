"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 10 - Files and Exceptions - Reading from a File
"""
from pathlib import Path

# the script is supposed to run in the current folder!
pi_file = 'pi_digits.txt'
path = Path(pi_file)
# remove the last newline
content = path.read_text().rstrip()

print("The file content is:")
print(content)

lines = content.splitlines()
print("The file content is (line by line):")
for line in lines:
    print('->', line)

pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print('Splicing lines in a single string, removing leading blanks', pi_string)


def load_from_file(filename):
    """
    Read a file in the current folder, remove leading and trailing blanks, return a single 'clean' string
    """
    content = Path(filename).read_text()
    lines = content.splitlines()
    result = ''
    for line in lines:
        result += line.strip()
    return result


# more fun with the 1M file from the original git repo: pi_million_digits.txt
# https://github.com/ehmatthes/pcc_3e/tree/main/chapter_10/reading_from_a_file
pi_string = load_from_file(pi_file)

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print(f"Your birthday appears in {pi_file}!")
else:
    print(f"Your birthday does not appear in {pi_file}")
