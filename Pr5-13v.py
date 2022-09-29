s = input("Введите строку\n")

string = s[s.find('(') + 1:s.find(')')]
print(string)

