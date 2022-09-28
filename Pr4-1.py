i = int(input("Введите 1ое число\n"))
j = int(input("Введите 2ое число\n"))

if not(i > j):
    print("1ое число должно быть больше 2ого\n")
    exit(1);
while i >= j:
    if i % 2 != 0:
        print(i)
    i -= 1