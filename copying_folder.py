import os
import shutil

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


def copying(question, question_copy):
    shutil.copy(f"{input(question)}", f"{input(question_copy)}")

    from menu import my_menu

copying('Введите папку/файл, которые хотите копировать: ', 'Введите  название копии папка/файл: ')