# Stepwise word
# author: Manny egalli64@gmail.com
# info: http://thisthread.blogspot.com/2017/01/codeeval-stepwise-word.html
#       https://www.codeeval.com/open_challenges/202/

import sys


def get_longest_word(line):
    words = line.split()
    selected = ''
    for word in words:
        if len(word) > len(selected):
            selected = word
    return selected


def solution(line):
    word = get_longest_word(line)
    result = []
    for i in range(len(word)):
        result.append('*' * i + word[i])
    return ' '.join(result)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()

    else:
        print('Data filename expected as argument!')