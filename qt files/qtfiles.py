import random
from random import randrange

f = open('lines.txt', encoding='utf-8')
lines = f.readlines()
# random.choice(lines)
nbyte = len(lines)
if nbyte:
    print(lines[randrange(nbyte)])
f.close()

# for num, line in enumerate(f):
#     print(line)
