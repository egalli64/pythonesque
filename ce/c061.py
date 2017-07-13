"""
CodeEval Decryption
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/61/
"""
message = '012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119'
keyed_alphabet = 'BHISOECRTMGWYVALUZDNFJKPQX'

table = {}
for i in range(len(keyed_alphabet)):
    table[keyed_alphabet[i]] = i

encrypted_words = message.split(' ')
clear_words = []
for cur in encrypted_words:
    clear_word = []
    for i in range(0, len(cur), 2):
        key = int(cur[i:i + 2])
        clear_word.append(chr(ord('A') + table[chr(ord('A') + key)]))
    clear_words.append(''.join(clear_word))

print(' '.join(clear_words))
