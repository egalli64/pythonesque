"""
CodeEval URI Comparison
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/80/
"""
import sys
import re


def get_site(chunk):
    pos = chunk.find(':')
    if pos == -1:
        return chunk, 80

    port = int(chunk[pos + 1:])
    return chunk[:pos], port


def decode(chunk):
    match = True
    while match:
        match = re.search('%([0-9a-fA-F][0-9a-fA-F])', chunk)
        if match:
            sub_hex = match.group(0)
            sub_plain = bytes.fromhex(match.group(1)).decode('utf-8')
            chunk = chunk.replace(sub_hex, sub_plain)
    return chunk


def solution(first, second):
    pos = first.find('//')
    if first[:pos].upper() != second[:pos].upper():
        return False

    end_1 = first.find('/', pos + 2)
    host_1, port_1 = get_site(first[pos:end_1 if end_1 != -1 else len(first)])

    end_2 = second.find('/', pos + 2)
    host_2, port_2 = get_site(second[pos:end_2 if end_2 != -1 else len(second)])

    if port_1 != port_2:
        return False

    if host_1.upper() != host_2.upper():
        return False

    if end_1 == -1 and end_2 == -1:
        return True
    if end_1 == -1 or end_2 == -1:
        return False

    page_1 = decode(first[end_1 + 1:])
    page_2 = decode(second[end_2 + 1:])

    return page_1 == page_2

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                lhs, rhs = test.rstrip('\n').split(';')
                print(solution(lhs, rhs))
    else:
        print('Data filename expected as argument!')
