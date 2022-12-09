# 1
from math import pi


d =  len(input("Введите число для заданной точности числа Пи:\n").split('.')[1] )

print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')

