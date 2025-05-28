"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Program: Baby Vocab
Given a list of words, associate each word to its count, then call the function to print the histogram word/count
"""

FILE_NAME = "cip/w6/challenges/e3_words.txt"


def main():
    words = load_words_from_file(FILE_NAME)
    counter = {}
    for word in words:
        counter[word] = counter.setdefault(word, 0) + 1

    for key, value in counter.items():
        print_histogram_bar(key, value)


def print_histogram_bar(word, count):
    """
    Prints one bar in the histogram.

    Uses formatted strings to do so. The
        {word : <8}
    adds white space after a string to make
    the string take up 8 total characters of space.
    This makes all of our words on the left of the
    histogram line up nicely. On the other end,
        {'x' * count}
    takes the 'x' string and duplicates it by 'count'
    number of times. So 'x' * 5 would be 'xxxxx'.

    Calling print_histogram_bar("mom", 7) would print:
        mom     : xxxxxxx
    """
    print(f"{word : <8}: {'x' * count}")


def load_words_from_file(filepath):
    """
    Loads words from a file into a list and returns it.
    We assume the file to have one word per line.
    Returns a list of strings. You should not modify this
    function.
    """
    words = []
    with open(filepath, "r") as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != "":
                words.append(cleaned_line)

    return words


if __name__ == "__main__":
    main()
