matrix = []
s = []

with open('Ромадин Данил Алексеевич_УБ-23_Vvod.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        matrix.append(list(map(int, line.rstrip().split())))

for i in range(len(matrix)):
    s.append(sum(matrix[i]))

s1 = matrix[s.index(max(s))]
s2 = max(s)
s3 = matrix[s.index(min(s))]
s4 = min(s)
with open('Ромадин Данил Алексеевич_УБ-23_Vivod.txt', 'w') as f:
    f.write(str("Строка с наибольшей суммой:"))
    f.write(str(s1))
    f.write(str("Сумма элементов:"))
    f.write(str(s2))
    f.write(str("Строка с наименьшей суммой:"))
    f.write(str(s3))
    f.write(str("Сумма элементов:"))
    f.write(str(s4))





















