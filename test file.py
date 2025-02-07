from pprint import pprint

file = open('text.txt', mode='rb')
print(file.read(10))
data = file.read()
print(data[::-1])

file.close()