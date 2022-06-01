import os

# Удаляет папку

def removal():
    def delete_f(question_three):
        delete = input(question_three)
        os.rmdir(delete)
    delete_f('Введите название папки/файла: ')

    while True:
        action = input('Хотите еще удалить папку y/n: ')
        if action == 'y':
            delete_f('Введите название папки: ')
        elif action == 'n':
            print('Выбранные папки успешно удалены.')
            break
        continue

removal()


# def delete_f(question_three, question_four):
#     delete = input(question_three)
#     os.rmdir(delete)
#     while True:
#         action = input(question_four)
#         if action == 'y':
#             delete_f('Введите название папки/файла: ', 'Удалить папку/файл y/n: ')
#         else:
#             break
#
# delete_f('Введите название папки/файла: ', 'Удалить папку/файл y/n: ')
