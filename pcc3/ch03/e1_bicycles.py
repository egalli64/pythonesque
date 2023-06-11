"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 3 - Introducing Lists
"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print("First:", bicycles[0])
print(bicycles[0].title())
print("Second:", bicycles[1])
print("Forth:", bicycles[3])
print("Last:", bicycles[-1])

message = f"His first bicycle was a {bicycles[0].title()}."
print(message)
