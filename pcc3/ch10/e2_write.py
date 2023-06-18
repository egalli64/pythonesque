"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 10 - Files and Exceptions - Writing to a File
"""
from pathlib import Path

# the script is supposed to run in the current folder!
path = Path('programming.txt')

content = "I love programming\n"
content += "I love creating new games\n"
content += "I also love working with data\n"

# if existing, the file is overwritten!
path.write_text(content)
