from zipfile import ZipFile

with ZipFile('1.zip') as myzip:
    print(myzip.namelist())
    # for name in myzip.namelist():
    #     # if name[-1] == '/':
    #     #
    #     #     print(name[0::-2])
    #     #
    #     # else:
    #     #     print(name)
    # print(myzip.filelist)

    # for dir in myzip.namelist():
    #     print(myzip.filename)

    for z in myzip.filelist:
        name = z.filename
        if name[-1] == '/':  # каталог
            print('  ' * (name.count('/') - 1) + z.orig_filename.split('/')[-2])

        else:
            print('  ' * (name.count('/')) + z.orig_filename.split('/')[-1])
