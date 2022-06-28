from decorator import add_menu
# Просмотр файлов

import os


@add_menu
def viewing_f():
    result = os.listdir(os.getcwd())
    # распечатать все файлы и папки рекурсивно
    for result, dirnames, filenames in os.walk("."):
        # перебрать файлы
        for filename in filenames:
            print("Файл:", os.path.join(result, filename))



viewing_f()


