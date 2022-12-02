#Последовательность

n = int(input())
list= 0
for i in range(1,n+1):
   list+= round((1+(1/i))**i,2)
   print(list)
   i= i+1

print("сумма последовательностей", list)
