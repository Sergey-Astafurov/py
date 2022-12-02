#5 Перемешивание
import random
lenlist = int(input("Длинна массива"))
i=0
sp=[]
while i < lenlist:
   n = random.randint(0,10)
   sp.append(n)
   i+= 1
print(sp)


print("Перемешанный массив",random.sample(sp,len(sp)))