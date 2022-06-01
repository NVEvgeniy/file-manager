import os
import sys
import random


# Меню консольного файлового менеджера


while True:
    print('1. создать папку')
    print('2. создать файл')
    print('3. удалить (файл/папку)')
    print('4. копировать (файл/папку)')
    print('5. просмотр содержимого рабочей директории')
    print('6. посмотреть только папки')
    print('7. посмотреть только файлы')
    print('8. просмотр информации об операционной системе')
    print('9. создатель программы')
    print('10. играть в викторину')
    print('11. мой банковский счет')
    print('12. выход')


    choice = input('Выберите пункт меню: ')
    if choice == '1':
        from creating_folder import creation
        """
        При создании папки, новая папка отображается только после того, как полностью завершу программу
        """
        from menu import my_menu
        """
        С 'break' папка отображается, но программа полностью завершается. Подскажите, как сделать, чтобы и новая папка 
        отображалась сразу и программа в дальнейшем выходила в главное меню. 
        """

    elif choice == '2':
        from creating_file import creating_fl
    elif choice == '3':
        from delete import delete_f
        from menu import my_menu
    elif choice == '4':
        from copying_folder import copying
        break
    elif choice == '5':
        from viewing_the_directory import viewing_direct
        from menu import my_menu
    elif choice == '6':
        from viewing_folders import viewing_fo
        from menu import my_menu
    elif choice == '7':
        from viewing_files import viewing_f
        from menu import my_menu
    elif choice == '8':
        print('My OS is', sys.platform)
        from menu import my_menu
    elif choice == '9':
        pass
    elif choice == '10':
        from quiz_date import quiz_d
    elif choice == '11':
        from bank_account import actions_with_account
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')




# - смена рабочей директории (*необязательный пункт);


