from re import findall

file_path = "text files/What is Data Science.txt"


def word_count(path, word):
    """
    This function counts a word in a text.
    Parameters
    ----------
    path: string
    word: string
    """
    with open(path, "r", encoding="utf8") as text:
        content = text.read()
        print(len(findall(word, content)))


word_count(file_path, "are")
