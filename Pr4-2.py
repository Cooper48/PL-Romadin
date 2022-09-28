i = int(input("Введите число\n"))
j = 1
sum = 0
for a in range(1, i + 1):
    j *= a
    sum += j
print(sum)