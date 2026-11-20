import math


def _check(*values):
    '''
    Проверяет, что все значения являются неотрицательными числами

        Параметры:
            values : проверяемые значения

        Исключения:
            TypeError : если значение не является числом (int или float)
            ValueError : если значение отрицательное
    '''
    for value in values:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"Ожидалось число, получено {type(value).__name__}")
        if value < 0:
            raise ValueError("Значение не может быть отрицательным")


def area(r):
    '''
    Возвращает площадь круга

        Параметры:
            r (int) : целое положительное число (радиус круга)
        
        Возвращаемое значение:
            area (float) : вещественное положительное число (площадь круга)
    '''
    _check(r)
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает длину окружности круга

        Параметры:
            r (int) : целое положительное число (радиус круга)
        
        Возвращаемое значение:
            perimeter (float) : вещественное положительное число (длина окружности круга)
    '''
    _check(r)
    return 2 * math.pi * r