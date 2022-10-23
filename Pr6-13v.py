"""
1. Дан одномерный массив целых чисел. Проверить, есть ли в нем одинаковые
элементы. Вывести эти элементы и их индексы.
2. Дан одномерный массив из 8 элементов. Заменить все элементы массива
меньшие 15 их удвоенными значениями. Вывести на экран монитора
преобразованный массив.
"""
#1
from random import randint

s = [randint(1,20) for i in range(15)]
print(s) # List

f = []
m2 = []
ind = 0

for i in range(len(s)):
    if s[i] not in f:
        if s.count(s[i]) > 1:
            f.append(s[i])
            ind = s.index(s[i])
            print("Число -", s[i], "Индекс -", ind)

for i in range(len(s)):
    if s[i] < 15:
        m2.append(s[i]*2)
print(m2)




