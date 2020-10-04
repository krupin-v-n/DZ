'''
#Крупин Владимир Николаевич ИС - 29

#If 12
a, b, c = (int(input()) for i in range(3))
if a > b and a > c:
    print(a)
if b > a and b > c:
    print(b)
if c > b and c > a:
    print(c)

#If 9
A = float(input('Введите А: '))
B = float(input('Введите B: '))
save = float
if A > B:
    save = A
    A = B
    B = save
print('A: ', A, 'B: ', B)

#For 10
N = int(input())
s = 1
for i in range(1,N):
    s = s + 1 / i
print("Сумма равна: ", s)

#For 6
p = float(input("Цена 1 кг конфет: "))
for i in range(1,6):
    save = p
    p = p * (1 + i * 2 / 10)
    print("Цена ", (1 + i * 2 / 10), " кг конфет: ", p)
    p = save

#While 28
e = int(input("Введите число >0: "))
Ak1 = 0
Ak = 2
K = 1
k = 1
while abs(Ak - Ak1) >= e:
   k += 1
   Ak1 = Ak
   Ak = 2 + 1 / Ak1
print(k, Ak1, Ak)

#While 11
N = int(input())
K = 0
S = 0
while K < N:
    K = K + 1
    S = S + K
print(K, S)

#Series 3
a = []
for i in range(10):
    b = float(input("Введите число: "))
    a.append(b)
print("Среднее арифметическое: ", sum(a) / len(a))

#Series 13
a = []
N = int(input("Чисел в наборе: "))
for i in range(N):
    b = int(input("Введите число: "))
    a.append(b)
s = 0
for i in range(N):
    if a[i] > 0 and a[i] % 2 == 0:
        s = s + a[i]
print(s)

#ЗАДАНИЯ С ФУНКЦИЯМИ (Не уверен, что я правильно понял задание, но суть операции я понял. 
Использовал примитивно.. не не знаю куда еще её можно вставить)

#For 6 с функциями
p = float(input("Цена 1 кг конфет: "))
def func(x): 
    return 1 + x * 2 / 10
for i in range(1,6):
    save = p
    p = p * func(i)
    print("Цена ", func(i), " кг конфет: ", p)
    p = save

#For 10 с функциями
N = int(input())
s = 1
def function(x):
    return 1 / x
for i in range(1,N):
    s = s + function(i)
print("Сумма равна: ", s)
'''
