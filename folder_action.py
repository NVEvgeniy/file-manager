# Меню для повтора команды
def creation_menu(question, object_name):
    while True:
        action = input(question)
        if action == 'y':
            creating = (object_name)
        elif action == 'n':
            print('Выбранные папки добавлены.')
            break
        else:
            break
        break
creation_menu('Хотите еще создать папку y/n: ', 'Введите название папки: ')
