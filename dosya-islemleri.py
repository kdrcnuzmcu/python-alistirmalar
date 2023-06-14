path = "text files/What is Data Science.txt"

def KelimeSay(path, word):
    from re import findall

    with open(path, "r", encoding="utf8") as text:
        content = text.read()
        print(len(findall(word, content)))

KelimeSay(path, "are")