n = int(input())
sp= []
for i in range(-n, n+1,1):
   sp.append(i)
   i+=1

print (sp)
l1 = int(input("Введи позицию 1 "))
l2 = int(input("Введи позицию 2 "))

print("Произведение позиций : ", sp[l1]*sp[l2])