# # Меню для повтора команды
# def creation():
#     def creating(question):
#         folder = f"{input(question)}"
#         return os.mkdir(folder)
#
#     creating('Введите название папки: ')
#
#     try:
#         action = input('Хотите еще создать папку y/n: ')
#         result = action == 'y' if action == 'y' else action == 'n'
#         creating('Введите название папки: ')
#     except ValueError:
#         print('Неверно ввели данные, введите "y" или "n"')
#     # else:
#     #     print('В ходе выполнения небыло ошибок')
#
# creation()

purchase_all = {}
#
# for key, value in purchase_all.items():
#     print(f'{key} - {value}')

purchase_all = [f'{key} - {value}' for key, value in purchase_all.items()]