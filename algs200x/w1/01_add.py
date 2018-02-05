import sys

data = sys.stdin.read()
tokens = data.split()

a = int(tokens[0])
b = int(tokens[1])
print(a + b)