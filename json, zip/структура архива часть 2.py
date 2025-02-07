from zipfile import ZipFile


def human_read_format(size):
    sufix = ['Б', 'КБ', 'МБ', 'ГБ']
    i = 0
    while size > 1024:
        size = size / 1024
        i += 1
    size = round(size)
    return str(size) + sufix[i]


with ZipFile('1.zip') as myzip:
    for z in myzip.filelist:
        name = z.filename
        if name[-1] == '/':  # каталог
            print('  ' * (name.count('/') - 1) + z.orig_filename.split('/')[-2])

        else:
            print('  ' * (name.count('/')) + z.orig_filename.split('/')[-1] + ' ' + human_read_format(z.file_size))
