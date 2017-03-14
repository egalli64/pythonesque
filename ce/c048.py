"""
CodeEval Discount Offers
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/48/

!!! Still not working fine in a few cases !!!
"""
from math import gcd  # was: fractions
import sys


def score(customer, product):
    customer_letters = sum(c.isalpha() for c in customer)
    product_letters = sum(c.isalpha() for c in product)

    result = 1.5 if gcd(product_letters, customer_letters) > 1 else 1
    if product_letters % 2 == 0:
        result *= 1.5 * sum(1 for c in customer if c in 'aeiouyAEIOUY')
    else:
        result *= sum(1 for c in customer if c.isalpha() and c not in 'aeiouyAEIOUY')
    return int(result * 100)


def assign(assigned, vacant, values, epsilon):
    current = vacant.pop()
    current_values = values[current]

    first_choice = max(current_values)
    fc_index = current_values.index(first_choice)

    second_choice = max([x for x in current_values if x != first_choice])
    bid_chip = first_choice - second_choice + epsilon

    for v in values:
        v[fc_index] -= bid_chip

    if fc_index in assigned:
        vacant.append(assigned[fc_index])
    assigned[fc_index] = current


def auction(values):
    assigned = {}
    vacant = list(range(len(values)))

    diffs = [[abs(i - j) for i, j in zip(v[:-1], v[1:]) if i != j] for v in values]
    epsilon = min([min(x) for x in diffs]) // 2 + 1

    while vacant:
        assign(assigned, vacant, values, epsilon)
    return assigned


def solution(line):
    customers, products = [sub.split(',') for sub in line.split(';')]
    if customers[0] == '' or products[0] == '':
        return '0.00'

    values = [[score(c, p) for p in products] for c in customers]

    if len(customers) != len(products):
        for v in values:
            v.extend([0] * (len(customers) - len(products)))
    bids = auction([v[:] for v in values])
    result = sum(values[bids[p]][p] for p in bids)
    return '{:.2f}'.format(result / 100)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test.rstrip('\n')))
    else:
        print('Data filename expected as argument!')
