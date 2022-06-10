import os
import sys
# Создает папку
import sys


def creation():
    def creating(question):
        os.mkdir(f"{input(question)}")

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
    from menu import my_menu
creation()



# def creating(question):
#     folder = input(question)
#     os.mkdir(folder)
#
# creating('Введите название папки: ')
# if __name__ == '__main__':
#     # Меню для повтора команды
#     while True:
#         action = input('Хотите еще создать папку y/n: ')
#         if action == 'y':
#             creating('Введите название папки: ')
#         elif action == 'n':
#             print('Выбранные папки добавлены.')
#             break
#         else:
#             break
#         sys.exit()







