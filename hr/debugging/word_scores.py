"""
HackerRank - Practice - Python - Debugging - Words Score

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/words-score/problem


"""
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    """
    each word in words scores 1 if odd number of vowels (as defined above) else 2
    return the sum of scores for all words
    """
    scores = []
    for word in words:
        vowels = [map(word.count, 'aeiouy')]
        scores.append(1 if len(vowels) else 2)
    return sum(scores)

if __name__ == '__main__':
    # input()  # discarded header
    # print(score_words(input().split()))
    print(score_words('hacker book'.split()))
