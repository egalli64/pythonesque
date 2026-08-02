"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Listcomps Versus map and filter
"""
# Example 2-3. The same list built by a listcomp and a map/filter composition
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print("listcomp:", beyond_ascii)

# map/filter leads to the same result, but it's less readable
alt_beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print("filter and map:", alt_beyond_ascii)
