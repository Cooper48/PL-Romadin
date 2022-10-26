import random

def printmatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()

matrix = [[random.randint(-10,10) for i in range(3)] for j in range(3)]
print("Исходная матрица:", printmatrix(matrix))

matrix = [[1 if j>0 else 0 for j in i] for j in matrix]
for i in range(len(matrix)):
    print(*[matrix[i][j] if j<=i else '' for j in range(len(matrix[i]))],'')
