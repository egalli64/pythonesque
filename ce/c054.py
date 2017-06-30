"""
CodeEval Cash register
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/54/
"""
import sys

DENOMINATIONS = {
    'PENNY': 1,
    'NICKEL': 5,
    'DIME': 10,
    'QUARTER': 25,
    'HALF DOLLAR': 50,
    'ONE': 100,
    'TWO': 200,
    'FIVE': 500,
    'TEN': 1000,
    'TWENTY': 2000,
    'FIFTY': 5000,
    'ONE HUNDRED': 10000
}


def solution(price, cash):
    if cash < price:
        return 'ERROR'
    if cash == price:
        return 'ZERO'

    change = int(cash * 100) - int(price * 100)
    result = []

    for name, value in sorted(DENOMINATIONS.items(), key=lambda x: x[1], reverse=True):
        while value <= change:
            result.append(name)
            change -= value
        if change == 0:
            break

    return ','.join(result)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                lhs, rhs = map(float, test.split(';'))
                print(solution(lhs, rhs))
    else:
        print('Data filename expected as argument!')
