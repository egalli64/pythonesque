"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Byte Essentials
"""
a_bytes = bytes("café", encoding="utf_8")
print("a bytes object:", a_bytes)
print(f"first byte is {a_bytes[0]}")
print(f"its slices are bytes objects: {a_bytes[:1]}, {a_bytes[1:]}")

a_bytearray = bytearray(a_bytes)
print("a bytearray object:", a_bytearray)  # no literal syntax
print(f"first byte is {a_bytearray[0]}")
print(f"its slices are bytearray objects: {a_bytearray[:1]}, {a_bytearray[1:]}")
