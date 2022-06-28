import sys

def menu_creator_program():
    def author_info():
        return 'Автор программы Новиков Евгений'

    if __name__ == '__main__':
        while True:
            print('1. info')
            print('2. Выход')

            choice = input('Выберите пункт меню')
            if choice == '1':
                print(author_info())
            elif choice == '2':
                sys.exit(0)
            else:
                print('неверный пункт меню')

menu_creator_program()

