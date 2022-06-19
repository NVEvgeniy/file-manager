"""
5. В программе консольный файловый менеджер есть пункт "просмотр содержимого рабочей директории";
6. Добавить пункт "сохранить содержимое рабочей директории в файл";

7. При выборе этого пункта создать файл listdir.txt (если он есть то пересоздать) и сохранить туда содержимое
рабочей директории следующим образом: сначала все файлы, потом все папки, пример как может выглядеть итоговый файл.


files: victory.py, bill.py, main.py
dirs: modules, packages
"""
import os
import pickle
import json



onlyfiles = [f for f in os.listdir() if os.path.isfile(f)]
onlydirs = [f for f in os.listdir() if os.path.isdir(f)]
# files = (f"'files: ', {onlyfiles}\n'dirs:', {onlydirs}")
# print(files)
files = ('files: ', onlyfiles)
dirs = ('dirs: ', onlydirs)
with open('listdir.txt', 'w') as f:
    f.write(f'{json.dump(files, f)}\n')
    f.write(f'{json.dump(dirs, f)}')



with open('listdir.txt', 'r') as f:
    lines = f.readlines()
    result = f.readline()
    print(result)



result = json.dumps(files)
result1 = json.dumps(dirs)

files_recovery = json.loads(result)
print(files_recovery)
dirs_recovery = json.loads(result1)
print(dirs_recovery)






