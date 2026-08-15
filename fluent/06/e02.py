"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Identity, Equality, and Aliases
"""
charles = {"name": "Charles L. Dodgson", "born": 1832}
print("the charles dict:", charles)

lewis = charles
print("lewis is a charles alias:", lewis is charles)
print(f"charles id: {id(charles)}, lewis id: {id(lewis)}")

lewis["balance"] = 950
print("change lewis, see the change in charles:", charles)

# an impostor! same info but he is a different person
alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
print("alex == charles:", alex == charles)
print("but alex is not charles:", alex is not charles)
