"""
import math
x = 17.421
y = 10.365*10**(-1)
z = 0.828*10**5
s = (((y+((x-1)**1/3))**1/4) / math.fabs(x-y) * (math.pow(math.sin(z),2) + math.tan(z)))
print(s)

"""
"""
import math
x = 17.421
y = 10.365*(10**(-3))
z = 0.828*(10**5)
s = ((y + ((x-1)**1/3))**1/4) / ((math.fabs(x-y)) * ((math.sin(z))**2 + math.tan(z)))
print("s = {0:.6f}".format(s))
"""

import math
y2 = 10.365*(10**(-3))
z2 = 0.828*(10**5)
print("Число y =", y2)
print("Число z =", z2)
x = float(input("Vvedite x:"))
y = float(input("Vvedite y:"))
z = float(input("Vvedite z:"))
a = (x-1)**1/3
b = (y+a)**1/4
c = abs(x-y)
d = (math.pow(math.sin(z),2)) + (math.tan(z))
s = b / (c * d)
print("s = {0:.6f}".format(s))