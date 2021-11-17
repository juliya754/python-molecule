# -*- coding: utf-8 -*-

"""
Задача о расчете потенциалов для молекулы углерода C20.
Расчет выполнен методом Леннарда-Джонса
Входные данные: координаты атомов в формате файла .xyz
Выходные данные: значение потенциала
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
from math import sqrt

eps0 = 0.003006844311289
eps1 = 0.002412851881927
sigma0 = 3.4
sigma1 = 3.805


def R(x0, y0, z0, x1, y1, z1):
    return (sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2 + (z0 - z1) ** 2))


def ULJ(r, eps, sigma):
    return 4 * eps * ((sigma / r) ** 12 - 2 * (sigma / r) ** 6)


with open('E:/КТМФО/python/C20-Ih.xyz', 'r') as f:
    f.readline()
    f.readline()
    lst = f.readlines()
    lst = [[float(n) for n in x.split() if n != 'C'] for x in lst]
b = np.array(lst).transpose()
lenght = np.array(b[0]).__len__()

# функция не закончена
Utot = 0.
for i in range(lenght):
    for j in range(lenght):
        if i != j:
            r = R(b[0][i], b[1][i], b[2][i], b[0][j], b[0][j], b[0][j])
            Utot += ULJ(r, eps0, sigma0)

print(Utot)

Utot = 0.
for i in range(lenght):
    for j in range(lenght):
        if i != j:
            r = R(b[0][i], b[1][i], b[2][i], b[0][j], b[0][j], b[0][j])
            Utot += ULJ(r, eps1, sigma1)

print(Utot)


fig = plt.figure()
ax = fig.gca(projection='3d')

for i in range(0, lenght):
    ind = np.array([int(b[4][i]) - 1, int(b[5][i]) - 1, int(b[6][i]) - 1])
    for j in range(3):
        c = np.array([b[0][i], b[0][ind[j]]])
        d = np.array([b[1][i], b[1][ind[j]]])
        e = np.array([b[2][i], b[2][ind[j]]])

        ax.plot(c, d, e, '-og', linewidth=5, ms=20, alpha=0.9, mfc='lime')

plt.show()
