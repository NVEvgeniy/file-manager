
# menu = None

def my_menu():
    while True:
        menu = input('Вернуться в меню? y/n: ')
        if menu != 'y':
            break
        break


my_menu()

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