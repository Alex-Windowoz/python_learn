import csv

with open('wares.csv', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';', quotechar='"')
    rows = [(r[0], int(r[1])) for r in reader]
rows.sort(key=lambda x: x[1])
print(rows)
res = []
sum_t = 1000
if rows[0][1] > sum_t:
    print('error')
else:
    while rows and sum_t >= rows[0][1]:
        count = sum_t // rows[0][1]
        if count > 10:
            count = 10

        sum_t -= count * rows[0][1]
        res.extend([rows[0][0]] * count)
        rows.pop(0)

print((", ".join(res)))