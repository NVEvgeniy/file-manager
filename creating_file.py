from decorator import add_menu
# Создание файлов

@add_menu
def creating_fl(file_name):
    with open(f"{input(file_name)}.py", 'x'):
        pass

creating_fl('Введите имя файла: ')