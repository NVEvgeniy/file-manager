# просмотр содержимого рабочей директории
import os

def viewing_direct():
    # распечатать все файлы и папки в текущей директории
    result = os.listdir(os.getcwd())
    # перебрать папки и файлы
    for i in result:
        print(i)
viewing_direct()
