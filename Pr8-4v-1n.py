import random

def printmatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()


matrix = [[random.randint(-10, 10) for i in range(4)] for j in range(3)]
print('Исходная матрица:',matrix)
print(printmatrix(matrix))
s=[]
for i in range(len(matrix)):
    s.append(sum(matrix[i]))
print("Строка с наибольшей суммой:",matrix[s.index(max(s))],"Сумма элементов:",max(s), ";","Строка с наименьшей суммой:",matrix[s.index(min(s))],"Сумма элементов:",min(s))

def printmatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()
