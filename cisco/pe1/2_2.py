"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque/cisco/pe1/

PE1: Module 2 Section 2 Literals
"""
print('A string literal')
# double quote in string literals
print("I like \"Monty Python\"")
print('I like "Monty Python"')
# single quote in string literals
print('I\'m Monty Python.')
print("I'm Monty Python.")
print('An empty string:', '', '<-')
print("Another empty string:", "", "<-")

print('Plain integer literal:', 42)
print('An integer literal with underscore for readability:', 11_111_111)
print('A negative integer literal:', -11_111_111)

print('Expressing an integer as octal (leading 0o):', 0o123, 0O123)
print('Expressing an integer as hexadecimal (leading 0x):', 0x123, 0X123)

print('Floating point literals:', 0.4, .4, -.4, 2.5, 4.)
print('Floating point literal in scientific notation:',
      3e8, 6.62607E-34, 0.0000000000000000000001)

print('Boolean literals:', False, True)
print('True is bigger than False?', True > False)
print('True is smaller than False?', True < False)

# exercise: output on three lines "I'm" ""learning"" """Python"""
print('"I\'m"', '""learning""', '"""Python"""', sep='\n')
