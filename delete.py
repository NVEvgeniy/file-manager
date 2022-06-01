import os


def delete_f():
    while True:
        print('1. удалить папку')
        print('2. удалить файл')
        point = input('Выберите пункт меню: ')
        if point == '1':
            from delete_folder import removal
        elif point == '2':
            from delete_file import removal_file
            break
        break
delete_f()