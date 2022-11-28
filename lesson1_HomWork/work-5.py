import math

Ax = round(int(input("Введи Х1 ")))
Ay = round(int(input("Введи У1 ")))
Bx = round(int(input("Введи Х2 ")))
By = round(int(input("Введи У2 ")))
s = math.sqrt(pow(Bx - Ax, 2)+ pow(By - Ay,2))
print(s)
