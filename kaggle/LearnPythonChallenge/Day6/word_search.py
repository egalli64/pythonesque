# Learn Python Challenge: Day 6 Exercises

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    results = []
    for i, doc in enumerate(doc_list):
        tokens = doc.split()
        words = [x.rstrip('.,').lower() for x in tokens]
        if keyword.lower() in words:
            results.append(i)
    return results


def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    results = {}
    for keyword in keywords:
        results[keyword] = word_search(doc_list, keyword)
    return results


if __name__ == '__main__':
    print(word_search(
        ['The Learn Python Challenge Casino', 'They bought a car, and a horse', 'Casinoville?'],
        'casino'
    ))

    print(multi_word_search(
        ['The Learn Python Challenge Casino', 'They bought a car and a casino', 'Casinoville?'],
        ['casino', 'they']
    ))
