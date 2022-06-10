import math

# filter
# Вывод четных чисел
numbers = [1, 2, 3, 4, 5, 6]

def f(x):
    '''
    :param x: число списка
    :return: вывод четных чисел
    '''
    if (x % 2) == 0:
        return True
    else:
        return False

result = filter(f, numbers)
print(list(result))

# map
# умножение всех элементов списка на 5
def function_num(x):
    '''
    :param x: число списка
    :return: вывод произведения чисел
    '''
    return x*5

print(list(map(function_num, numbers)))

# sorted
# делим список на четные и нечетные

def function_sort(x):
    '''
    :param x: число списка
    :return: вывод четных чисел в левой части списка
    '''
    return x%2

print(sorted(numbers, key=function_sort))


# Функции math
# Число пи

print(math.pi)

# sqrt
# вычисление квадратного корня
def function_sqrt(x):
    '''
    :param x: число
    :return: квадратный корень числа x
    '''
    result = math.sqrt(x)
    return result
number = math.sqrt(49)
print(number)



# hypot
# нахождение гипотенузы
def function_hypot(x, y):
    '''
    :param x: длина катета 1
    :param y: длина катета 2
    :return: вычисление гипотенузы
    '''
    result = (math.hypot(x, y))
    return result
number = function_hypot(3, 4)
print(number)


# pow
# возведение числа в степень
def function_pow(a, b):
    '''
    :param a: число
    :param b: степень
    :return: возведение числа в степень
    '''
    result = (math.pow(a, b))
    return result
number = math.pow(3, 2)
print(number)