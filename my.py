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

#3
# a = int(input())

# for i in range(-a, a+1):
#    print(i, end = " , ")

#4
# a = float(input())

# print(int(a* 10) % 10)

#5
# a = int(input())

# if a % 5 == 0 and a % 10 == 0  and a % 15 == 0 and a % 30 != 0 :
#    print('Yes')
# else :
#    print('no')

a = '2sadasc22553....14'
a.split(',')
s = 0
for i in range(len(a)):
   if a[i].isdigit():
      s = s + int(a[i])
   else :
      continue
print(s)