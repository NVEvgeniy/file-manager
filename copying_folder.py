import os
import shutil
from decorator import add_menu


# shutil.copy('123.py', '123_copy.py')
# Копирует выбранный файл
# def copying():
#     copy = input('Введите папку/файл, которые хотите копировать: ')
#     my_copy = input('Введите  название копии папка/файл: ')
#
#     shutil.copy(f"{copy}", f"{my_copy}")
#
#
# copying()

@add_menu
def copying(question, question_copy):
    shutil.copy(f"{input(question)}", f"{input(question_copy)}")


copying('Введите папку/файл, которые хотите копировать: ', 'Введите  название копии папка/файл: ')