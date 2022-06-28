import os

# Удаляет файл

def removal_file():
    def delete_f(question_three):
        delete = input(question_three)
        os.remove(delete)
    delete_f('Введите название файла: ')
    # Меню для повтора команды
    while True:
        action = input('Хотите еще удалить файл y/n: ')
        if action == 'y':
            delete_f('Введите название файла: ')
        elif action == 'n':
            print('Выбранные файлы успешно удалены.')
            break
        else:
            break

removal_file()