# #1
# a = int(input())
# b = int(input())

# if a**2 == b  or b**2 == a:
#    print("число является квадратом")
# else :
#    print("нет")


# #2
# num = 0
# max_num = 0
# while num < 5:
#    number = int(input())
#    if number > max_num:
#       max_num= number
#    num += 1

# print(max_num)

# sp = list()
# for i in range(5) :
#    n = int(input())
#    sp.append(n)
# print(max(sp))

# 3
# a = int(input())

# for i in range(-a, a+1):
#    print(i, end = " , ")

# 4
# a = float(input())

# print(int(a* 10) % 10)

# 5
# a = int(input())

# if a % 5 == 0 and a % 10 == 0  and a % 15 == 0 and a % 30 != 0 :
#    print('Yes')
# else :
#    print('no')

# a = '2sadasc22553....14'
# a.split(',')
# s = 0
# for i in range(len(a)):
#    if a[i].isdigit():
#       s = s + int(a[i])
#    else :
#       continue
# print(s)

# 2. Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B
# включительно, в порядке убывания. В этой задаче можно обойтись без инструкции

# a = int(input())
# b = int(input())

# for i in range(a-(a-1) % 2, b-1,-2) :
#   print(i)

# 3

# n = int(input())

# for i in range(n) :
#    print((-3) ** i ,end = " ")

# 4 Паллиндром

# n = input()
# n.split()

# if n[0] == n[4] and n[1] == n[3] :
#    print("Yes")
# else :
#    print("No")

# print(n[::-1])


# 5

# a = (input())

# a1 = a//100
# a3 = a%10
# a2 = a%100 // 10

# print (a[0],a[2], sep="")

# 6

n1 = '123aaa1234'
n2 = 'aa'
i = 0
count = 0
while i < len(n1):
   sr = n1[i : i + len(n2)]
   print(sr)
   if sr == n2:
      count += 1
      i += len(n2)
   else:
      i += 2
print(count)

# 7

# n = int(input())
# print((n** 0.5))
# for i in range(1, int(n** 0.5)):
#    print(i**2)

# 8
# n = None
# sum=0
# count = 0
# while n!=0 :
#     n= int(input())
#     sum += n
#     count+=1

# print(sum/count)
# n = None
# sp = []
# while n != 0:
#    n = int(input())
#    sp.append(n)

# print(sum(sp)/len(sp))
