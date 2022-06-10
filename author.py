import sys


def author_info():
    return 'Автор программы Новиков Евгений'
    while True:
        print('1. info')
        print('2. Выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            print(author_info())
        elif choice == '2':
            sys.exit()
        else:
            print('неверный пункт меню')
author_info()
