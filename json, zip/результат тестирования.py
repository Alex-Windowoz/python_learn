import json

with open('scoring.json') as scoring:
    data = json.load(scoring)
summ = 0
test_i = 0
n_ok = 0
for i in range(len(data["scoring"])):
    n_ok = len(data["scoring"][i]['required_tests'])
    for j in range(n_ok):
        if input() == 'ok':
            # print(data["scoring"][i]['required_tests'][j])
            test_i += 1
    summ += test_i * data["scoring"][i]['points'] // n_ok
    test_i = 0
print(summ)
