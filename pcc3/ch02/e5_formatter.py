"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 2 - Strings - Formatter
"""
first_name = "ada"
last_name = "lovelace"

full_name = f"{first_name} {last_name}"
print(full_name)

message = f"Hello, {full_name.title()}!"
print(message)
