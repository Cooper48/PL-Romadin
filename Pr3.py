"""
x = 2a + 2b, a < b
x = a - b + 1, a > b
x = b^2 - b, a = b
"""

a = int(input("Введите первое число\n"))
b = int(input("Введите второе число\n"))
if a < b:
    x = 2*a + 2*b
elif a > b:
    x = a - b + 1
elif a == b:
    x = b**2 - b
print("Ответ:", x)
