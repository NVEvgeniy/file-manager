import os
import sys

def add_menu(f):
    def wrapper():
        result = f()
        menu = input('Вернуться в меню? y/n: ')
        if menu != 'y':
            sys.exit()
        return result
    return wrapper