import math
from func_python import f, function_num, function_sort
from func_python import function_sqrt, function_hypot, function_pow

# Вывод четных чисел
def test_f():
    assert f(2) == True

# умножение всех элементов списка на 5
def test_function_num():
    assert function_num(5)

# делим список на четные и нечетные
def test_function_sort():
    assert function_sort(2) == 0




# Число пи
def test_function_pi():
    assert math.pi


# вычисление квадратного корня
def test_function_sqrt():
    assert function_sqrt(49)


# нахождение гипотенузы
def test_function_hypot():
    assert function_hypot(3, 4)


# возведение числа в степень
def test_function_pow():
    assert function_pow(3, 2)

