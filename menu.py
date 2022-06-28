
import sys


def my_menu(question):
    menu = input(question)
    if menu != 'y':
        sys.exit()

my_menu('Вернуться в меню? y/n: ')







# def creating_f_menu():
#     while True:
#         print('1. создать папку')
#         print('2. создать файл')
#         point = input('Выберите пункт меню: ')
#         if point == '1':
#             from creating_folder import creation
#         elif point == '2':
#             from creating_folder import creating_file
#             break
#         break
# creating_f_menu()