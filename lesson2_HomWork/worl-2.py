# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = 12
s = 1
# for i in range(1,num,1) :
#    s= s*i
#    print(s)


n = [i for i in range(1,num)]
def sum(n):
   s = s* n[i]
   return s


# res  = list(map(lambda x: s( *x), n))
print(sum(n))
