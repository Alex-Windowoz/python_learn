from zipfile import ZipFile
import json

count = 0
with ZipFile('moscow 2.zip') as myzip:
    for z in myzip.filelist:
        name = z.filename
        # print('  ' * (name.count('/')) + z.orig_filename.split('/')[-1])
        # print((z.orig_filename.split('/')[-1])[0])
        # print(name)
        if name[-5::] == '.json' and (z.orig_filename.split('/')[-1])[0] != '.':
            with open(str(name)) as search_moscow:
                data = json.load(search_moscow)
                # print(data['city'])
                if data['city'] == 'Москва':
                    count += 1
print(count)
