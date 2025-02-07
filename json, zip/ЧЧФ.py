def human_read_format(size):
    sufix = ['Б', 'КБ', 'МБ', 'ГБ']
    i = 0
    while size > 1024:
        size = size / 1024
        i += 1
    size = round(size)
    return str(size) + sufix[i]


print(human_read_format(15000))
