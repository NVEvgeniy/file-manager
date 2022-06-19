# Просмотр файлов

import os

def viewing_f():
    result = os.listdir(os.getcwd())
    # распечатать все файлы и папки рекурсивно
    for result, dirnames, filenames in os.walk("."):
        # перебрать файлы
        for filename in filenames:
            print("Файл:", os.path.join(result, filename))

    from menu import my_menu

viewing_f()
