# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

a = input()
a.split()
s = 0
for i in range(len(a)):
   if a[i].isdigit():
      s = s + int(a[i])
   else :
      continue
print(s)