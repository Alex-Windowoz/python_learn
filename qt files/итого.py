f = open('prices.txt', encoding='utf-8')
lines = f.readlines()
table = []
summ = 0
for i in range(len(lines)):
    table.append(lines[i].split())
    summ += float(table[i][1]) * float(table[i][2])

print('%.2f' % summ)
