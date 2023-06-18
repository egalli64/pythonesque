"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 10 - Files and Exceptions - Storing Data
"""
from pathlib import Path
import json

input_numbers = [2, 3, 5, 7, 11, 13]
path = Path('numbers.json')
content = json.dumps(input_numbers)

# the data are going to be stored in a file in the current execution path
path.write_text(content)
print(input_numbers, 'written to', path)

load_data = path.read_text()
load_numbers = json.loads(load_data)
print(load_numbers, 'read from', path)
