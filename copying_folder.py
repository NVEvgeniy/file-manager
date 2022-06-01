import os
import shutil

# shutil.copy('123.py', '123_copy.py')
# Копирует выбранный файл
def copying():
    copy = input('Введите папку/файл, которые хотите копировать: ')
    my_copy = input('Введите  название копии папка/файл: ')

    shutil.copy(f"{copy}", f"{my_copy}")


copying()


