# Создание файлов

def creating_fl():
    my_file = input('Введите имя файла: ')
    with open(f"{my_file}.py", 'x'):
        pass

creating_fl()