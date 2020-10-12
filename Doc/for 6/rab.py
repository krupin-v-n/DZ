#For 6 (с фóнкциями)
'''
p = float(input("Цена за 1 кг конфет: "))
def func(x):
   return 1 + x * 2 / 10
for i in range(1, 6):
   save = p
   p = p * func(i)
   print("Цена ", func(i), " кг конфет: ", p)
   p = save
'''
#For 6 (с фóнкциями и чтением)
f = open("import.txt")
j = f.read()
z = float(j)
f.close()
print("Цена за 1 кг конфет: ", z)

def func(x):
   return 1 + x * 2 / 10

f2 = open("export.txt", 'w')

for i in range(1, 6):
   save = z
   z = z * func(i)
   text = "Цена " + str(func(i)) + " кг конфет: " + str(z) + '\n'
   f2.write(text)
   z = save
f2.close()
