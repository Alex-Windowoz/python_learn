keys = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
        "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
        "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
        "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
        "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
        "б": "b", "ю": "ju", "ё": "jo"}

fin = open('cyrillic.txt', 'r')
fout = open('transliteration.txt', 'w')
transliteration = fin.read()
if len(transliteration) == 0:
    exit()

for key in keys:
    transliteration = transliteration.replace(key, keys[key])
transliteration = transliteration.swapcase()

for key in keys:
    transliteration = transliteration.replace(key, keys[key].capitalize().swapcase())
transliteration = transliteration.swapcase()

fout.write(transliteration)
