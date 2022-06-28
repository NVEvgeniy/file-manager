import sys
import os
# Меню консольного файлового менеджера


while True:
    print('1. создать папку')
    print('2. создать файл')
    print('3. удалить (файл/папку)')
    print('4. копировать (файл/папку)')
    print('5. просмотр содержимого рабочей директории')
    print('6. сохранить содержимое рабочей директории в файл')
    print('7. посмотреть только папки')
    print('8. посмотреть только файлы')
    print('9. просмотр информации об операционной системе')
    print('10. создатель программы')
    print('11. играть в викторину')
    print('12. мой банковский счет')
    print('13. выход')


    choice = input('Выберите пункт меню: ')
    if choice == '1':
        from creating_folder import creation
    elif choice == '2':
        from creating_file import creating_fl
    elif choice == '3':
        from delete import delete_f
    elif choice == '4':
        from copying_folder import copying
    elif choice == '5':
        from viewing_the_directory import viewing_direct
    elif choice == '6':
        pass
    elif choice == '7':
        from viewing_folders import viewing_fo
    elif choice == '8':
        from viewing_files import viewing_f
    elif choice == '9':
        print('My OS is', sys.platform)
    elif choice == '10':
        print('Автор программы Новиков Евгений')
    elif choice == '11':
        from quiz_date import quiz_d
    elif choice == '12':
        from account import actions_with_account
    elif choice == '13':
        break
    else:
        print('Неверный пункт меню')






# - смена рабочей директории (*необязательный пункт);


