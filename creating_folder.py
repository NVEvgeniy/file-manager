import os
import sys
from decorator import add_menu
# Создает папку



@add_menu
def creation():
    def creating(question):
        folder = f"{input(question)}"
        return os.mkdir(folder)

    creating('Введите название папки: ')
    # Меню для повтора команды
    while True:
        action = input('Хотите еще создать папку y/n: ')
        if action == 'y':
            creating('Введите название папки: ')
        elif action == 'n':
            print('Выбранные папки добавлены.')
            break
        else:
            break
    # from menu import my_menu

creation()





