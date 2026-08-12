"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Bytes creation extra
"""
import array

# 1. bytes from hex
hex_string = "31 4B CE A9"
print("a hex string:", hex_string)

a_bytes = bytes.fromhex(hex_string)
print("bytes from hexes", a_bytes)

# 2. bytes from short int array
numbers = array.array('h', [-2, -1, 0, 1, 2])
print(f"an array of {len(numbers)} short integers:", numbers)

a_bytes = bytes(numbers)
print(f"bytes of {len(a_bytes)} from int array:", a_bytes)
