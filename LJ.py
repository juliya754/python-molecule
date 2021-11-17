# -*- coding: utf-8 -*-

"""
Задача о расчете потенциалов для трех случаев расположения 4 атомов:
в линию, в квадрат, в тетраэдр. Расчет выполнен методом Леннарда-Джонса
Входные данные: координаты атомов
Выходные данные: значение потенциала
"""

from scipy.optimize import fmin
from math import sqrt


# функция расчета потенциала между 2 точками Леннарда-Джонса
def ULJ(r):
    return 4 * ((1 / r) ** 12 - (1 / r) ** 6)


# функция нахождения расстояния между думя точками по их координатам
def R(x0, y0, z0, x1, y1, z1):
    return (sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2 + (z0 - z1) ** 2))


# функция нахождения полного потенциала между атомами, расположенными в линию
# r1 - расстояние между 1 и 2 атомами, равное расстоянию между 3 и 4, r2 - между 2 и 3
def Utot1D(x):
    x0 = x[0]
    x1 = x[1]
    x2 = x[2]
    r1 = R(x0, 0., 0., x1, 0., 0.)
    r2 = R(x1, 0., 0., x2, 0., 0.)
    return 2 * ULJ(r1) + ULJ(r2)


# функция нахождения полного потенциала между атомами, расположенными квадратом
# r0 - расстояние между атомами
def Utot2D(x):
    x0 = x[0]
    x1 = x[1]
    r0 = R(x0, 0., 0., x1, 0., 0.)
    return 4 * ULJ(r0)


# функция нахождения полного потенциала между атомами, расположенными тетраэдером
# r0 - расстояние между связанными атомами
def Utot3D(x):
    x0 = x[0]
    y0 = x[1]
    z0 = x[2]
    x1 = x[3]
    y1 = x[4]
    z1 = x[5]
    r0 = R(x0, y0, z0, x1, y1, z1)
    return 6 * ULJ(r0)


print(fmin(Utot1D, (1., 2., 5.)))
print(fmin(Utot2D, (1., 2.)))
print(fmin(Utot3D, (1., 1., 1., 2., 2., 2.)))


