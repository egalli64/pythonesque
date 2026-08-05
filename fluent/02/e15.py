"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Slice Objects
"""
# Recalling how stepping (aka striding) works in a slice
s = 'bicycle'
print("Original sequence:", s)
print("Stepping by 3:", s[::3])
print("Stepping by -1 to reverse:", s[::-1])
print("Stepping by -2:", s[::-2])

# Example 2-13. Line items from a flat-file invoice
invoice = """
..........1.........2.........3.........4.........5.........6.....
012345678901234567890123456789012345678901234567890123456789012345
1909 Pimoroni PiBrella                      $17.50    3    $52.50
1489 6mm Tactile Switch x20                  $4.95    2    $9.90
1510 Panavise Jr. - PV-201                  $28.00    1    $28.00
1601 PiTFT Mini Kit 320x240                 $34.95    1    $34.95
"""

# using slice objects to improve readability
SKU = slice(0, 4)
DESCRIPTION = slice(5, 43)
UNIT_PRICE = slice(44, 50)
QUANTITY = slice(51, 55)
ITEM_TOTAL = slice(59, None)

for line in invoice.splitlines()[3:]:
    print(line[SKU], end="|")
    print(line[DESCRIPTION], end="|")
    print(line[UNIT_PRICE], end="|")
    print(line[QUANTITY], end="|")
    print(line[ITEM_TOTAL])
