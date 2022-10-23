"""
1. Вычислить сумму и число положительных элементов матрицы A[N, N],
находящихся над главной диагональю.
"""
m = int(input("Введите кол-во строк\n"))
n = int(input("Введите кол-во столбцов\n"))
a = []
for i in range(m):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    a.append(b)

print("Исходный массив:")

for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()

s = []
for i in range(m):
    for j in range(n):
        if i < j:
            if a[i][j] > 0:
                s.append(a[i][j])
print("Сумма = ",sum(s),"Длина =", len(s))