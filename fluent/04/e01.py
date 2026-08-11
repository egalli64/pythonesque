"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Character Issues
"""
# Example 4-1. Encoding and decoding
a_string = "café"
print(f"the string {a_string} has len {len(a_string)}")

bs = a_string.encode("utf8")
print(f"the bytes {bs} has len {len(bs)}")

print("Decode the bytes to get the original string:", bs.decode("utf8"))
