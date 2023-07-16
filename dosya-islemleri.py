from re import findall

file_path = "text files/What is Data Science.txt"


def kelime_say(path, word):
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


kelime_say(file_path, "are")
