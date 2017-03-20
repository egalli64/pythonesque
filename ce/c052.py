"""
CodeEval Text Dollar
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/52/
"""
import sys

conversion = {
    1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
    9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
    16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty',
    40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'
}


def solution(line):
    amount = int(line)
    result = ''

    small = amount % 100
    if small:
        if small < 21:
            result = conversion[small]
        else:
            units = amount % 10
            result = conversion.get(small - units, '') + conversion.get(units, '')

    more = amount - small
    if more == 0:
        return result

    hundreds = (more % 1000) // 100
    if hundreds:
        result = conversion[hundreds] + 'Hundred' + result
    more -= hundreds * 100
    if more == 0:
        return result

    thousands = (more % 100000) // 1000
    if thousands:
        if thousands < 21:
            result = conversion[thousands] + 'Thousand' + result
        else:
            units = thousands % 10
            tens = thousands - units
            result = conversion.get(tens, '') + conversion.get(units, '') + 'Thousand' + result

        more -= thousands * 1000
        if more == 0:
            return result

    hundred_thousands = (more % 1000000) // 100000
    if hundred_thousands:
        tag = 'Hundred'
        if thousands == 0:
            tag += 'Thousand'

        result = conversion[hundred_thousands] + tag + result
    more -= hundred_thousands * 100000
    if more == 0:
        return result

    millions = (more % 100000000) // 1000000
    if millions:
        if millions < 21:
            result = conversion[millions] + "Million" + result
        else:
            units = millions % 10
            tens = millions - units
            result = conversion.get(tens, '') + conversion.get(units, '') + 'Million' + result
    more -= millions * 1000000
    if more == 0:
        return result

    hundred_millions = (more % 1000000000) // 100000000
    if hundred_millions:
        tag = 'Hundred'
        if millions == 0:
            tag += 'Million'
        result = conversion[hundred_millions] + tag + result

    return result


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test.rstrip('\n')) + 'Dollars')
    else:
        print('Data filename expected as argument!')
