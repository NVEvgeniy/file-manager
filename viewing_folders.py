# Просмотр папок

import os

def viewing_fo():
    result = os.listdir(os.getcwd())
    # распечатать все файлы и папки рекурсивно
    for result, dirnames, filenames in os.walk("."):
        # перебрать каталоги
        for dirname in dirnames:
            print("Каталог:", os.path.join(result, dirname))

viewing_fo()