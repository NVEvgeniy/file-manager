# Создание файлов

def creating_fl(file_name):
    with open(f"{input(file_name)}.py", 'x'):
        pass
    from menu import my_menu
creating_fl('Введите имя файла: ')