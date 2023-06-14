def DosyaAra(path="."):
    from os import walk
    for main, subs, files in walk(path):
        results = subs + files
        break
    return results

DosyaAra()