"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Deque
"""
from collections import deque

a_deque = deque(range(10), maxlen=10)
print("a deque:", a_deque)

a_deque.rotate(3)
print("rotate 3:", a_deque)

a_deque.rotate(-4)
print("rotate -4:", a_deque)

# when the deque is full, append left/(right) implies discarding elements on the other end
a_deque.appendleft(-1)
print("append left:", a_deque)

# same concept for extend
a_deque.extend([11, 22, 33])
print("extend (right):", a_deque)
