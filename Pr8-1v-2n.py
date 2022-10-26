"""
2. Дана матрица B[N, М]. Найти в каждой строке матрицы
максимальный и минимальный элементы и поменять их с первым и
последним элементами строки соответственно.
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

for i, row in enumerate(a):
    max = min = 0
    for j, elem in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    row[max], row[0] = row[0], row[max]
    row[min], row[-1] = row[-1], row[min]
    
def printmatrix(matrix): #Функция преобразования массива в матрицу
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()
        
print(printmatrix(a))
