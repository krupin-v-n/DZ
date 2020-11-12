# =======================================================Z3=======================================================

# Proc 18

# Описать функцию CircleS(R) вещественного типа, находящую площадь круга радиуса R (R — вещественное). 
# С помощью этой функции найти площади трех кругов с данными радиусами. 
# Площадь круга радиуса R вычисляется по формуле S = π·R2
# В качестве значения π использовать 3.14.

import math
a = []
for i in range(3):
    R = float(input())
    a.append(R)
def CircleS(R):
    return math.pi * R ** 2
for j in range(3):
    print("Площадь окружности равна: ", CircleS(a[j]))
    
# Proc 32

# Описать функцию DegToRad(D) вещественного типа, находящую величину угла в радианах, 
# если дана его величина D в градусах (D — вещественное число, 0 < D < 360). 
# Воспользоваться следующим соотношением:
# 180◦ = π радианов. В качестве значения π использовать 3.14. 
# С помощью функции DegToRad перевести из градусов в радианы пять данных углов.

pi = 3.14
a = []
for i in range(5):
    D = float(input())
    a.append(D)
def DegToRad(D):
    return D / 180
for j in range(5):
    if a[j] > 0 and a[j] < 360:
        print(DegToRad(a[j]), "радиан")
        

# Minmax 10

# Дано целое число N и набор из N целых чисел. Найти номер первого экстремального 
# (то есть минимального или максимального) элемента из данного набора.

a = []
N = int(input("Введите количество чисел: "))
for i in range(N):
    c = int(input("Введите число: "))
    a.append(c)
min = min(a)
max = max(a)
imin = a.index(min)
imax = a.index(max)
if imin < imax:
    print("Номер первого экстремального: ", imin+1) #imin+1 чтобы список начинался не с нуля.
if imin > imax:
    print("Номер первого экстремального: ", imax+1)
    

# Minmax 18

# Дано целое число N и набор из N целых чисел. Найти количество
# элементов, содержащихся между первым и последним максимальным элементом. 
# Если в наборе имеется единственный максимальный элемент, то
# вывести 0.

from array import *
a = []
N = int(input("Введите количество чисел: "))
for i in range(N):
    c = int(input("Введите число: "))
    a.append(c)
max1 = max(a)
imax1 = a.index(max1)
a.pop(imax1)
max2 = max(a)
imax2 = a.index(max2)
imax2 = imax2
if max1 == max2 or imax1 == imax2:
    print('0')
else:
    if imax1 > imax2:
        print(imax1 - imax2 - 1)
    if imax2 > imax1:
        print(imax2 - imax1 - 1)
        
# =======================================================Z4=======================================================

# Array 79

# Дан массив размера N. Осуществить сдвиг элементов массива вправо на одну позицию
# (при этом A1 перейдет в A2, A2 — в A3, ..., AN−1 — в AN, a исходное значение последнего элемента будет потеряно).
# Первый элемент полученного массива положить равным 0.

a = []
N = int(input("Введите количество элементов массива: "))
for i in range(N):
    c = int(input("Введите число: "))
    a.append(c)
a.insert(0, 0)
a.pop(-1)
print(a)
# Возможно решение должно быть сложнее, но ведь работает)

#Array 77

# Дан массив размера N. Возвести в квадрат все его локальные минимумы (то есть числа, меньшие своих соседей).

a = []
savei = []
N = int(input("Введите количество элементов массива: "))
for i in range(N):
    c = int(input("Введите число: "))
    a.append(c)
for i in range(1, N-1):
        if a[i] < a[i-1] and a[i] < a[i-1]:
            savei.append(i)
for j in range(len(savei)):
    h = savei[j]
    a[h] = a[h] ** 2
print(a)

# Matrix 64

# Дана матрица размера M × N. Удалить столбец, содержащий максимальный элемент матрицы.

import numpy as np
M = int(input("Количество строк: "))
N = int(input("Количество столбцов: "))
m = list(map(int, input("Введите элементы через пробел в одну строку: ").split()))
mnp = np.array(m).reshape(M, N)
max = 0
for i in range(3):
     for j in range(3):
        if mnp[i][j] > max:
            max = mnp[i][j]
            save = i
np.delete(mnp, save, axis = 1)
print(mnp)
#Пробовал способов 5, не помогает вообще ничего.. выводит матрицу без изменений

# Matrix 20

# Дана матрица размера M ×N. Для каждого столбца матрицы найти произведение его элементов.

import numpy as np
M = int(input("Количество строк: "))
N = int(input("Количество столбцов: "))
a = list(map(int, input("Введите элементы через пробел в одну строку: ").split()))
am = np.array(a).reshape(M, N)
p = 1
for j in range(M):
     for i in range(N):
          p = p * am[i,j]
     print('В столбце ', j+1, ' произведение =', p)
     p = 1

# KRUPIN V. N. IS-29
