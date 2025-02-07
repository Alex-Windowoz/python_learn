import re

capacity = {'TB': 1099511627776, 'GB': 1073741824, 'MB': 1048576, 'KB': 1024, 'B': 1}
with open('input.txt', 'r') as fi:
    lines = fi.readlines()
    # print(lines)
    table = []
    for i in range(len(lines)):
        table.append(re.split("[.' '\n]", lines[i]))

    print(table)
    table.sort()
    table.sort(key=lambda i: i[1])
    print(table)
    ii = 0
    summ = 0
    output = ''

    for i in range(len(table)):
        if table[ii][1] != table[i][1]:
            for key, value in capacity.items():
                if int(summ / capacity.get(key)) > 0:
                    output += f'----------\nSummary: {int(summ / capacity.get(key))} {key}\n\n'
                    break

            summ = 0
            ii = i
        output += table[i][0] + '.' + table[i][1] + '\n'
        summ += int(table[i][2]) * capacity[table[i][3]]


    for key, value in capacity.items():
        if int(summ / capacity.get(key)) < 0:
            output += f'----------\nSummary: {round(summ / capacity.get(key))} {key}\n'
            break
    print(output)

    with open('output.txt', 'w') as fo:
        fo.write(output)
        fo.close()
    fi.close()
