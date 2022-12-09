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

# n1 = '123aaa1234'
# n2 = 'aa'
# i = 0
# count = 0
# while i < len(n1):
#    sr = n1[i : i + len(n2)]
#    print(sr)
#    if sr == n2:
#       count += 1
#       i += len(n2)
#    else:
#       i += 2
# print(count)

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

# 3 seminar
# list = [1,2,3,3,3,4,5,6,7,8,8,8]
# newList = []
# for i in list:
#    if list.count(i) ==1:
#       newList.append(i)

# print(*newList)

# 2
# list = [1, 5, 2, 4, 3]
# new_list = []
# for i in range(len(list)-1):
#    if list[i] < list[i+1]:
#          new_list.append(list[i+1])

# print(*new_list)
#3
# import time
# def random(n):
#    str_time = str(time.time())
#    str_time = str_time.replace('.','')
#    number = int(str_time) % n
#    return number

# print(random(1000))

#4
# list = []
# number = 12
# for i in range(5):
#    list.append(input())

# print(list)
# for i in range(5):
#    if str(number) in list[i]:
#       print("Yes")
#    else:
#       continue

# list = []
# for i in range(5):
#    list.append(input())
# if any('12' in el for el in list ):
#    print("yes")

# print(list)

#5
# list = ['qwe','asd', 'zxs', 'ertqwe']
# n = 'qwe'
# s = 0
# count = 0
# for i in range(len(list)):
#    if list[i] == n :
#       count+=1

#       if (count == 2):
#          s= i
#    else:
#       print('no')

# print(s)

#Новая лекция
# x,y = [int(i) for i in input().split()]
# print(x+y)

# словарь

# access = {'login' : 'ivan', 'password': '123'}
# login = input()
# password = input()

# if login == access['login'] and password == access['password'] :
#    print('Вход разрешен')
# Наполнить словарь
# slovar = {}

# slovar['city'] = 'Moscow'

# подсчет количества
# sp = [1,222,2,2,3,3,4,4,4,4,5]

# slov = {}
# for el in sp:
#    if el not in slov:
#       slov[el] = 1
#    else:
#       slov[el] += 1
# print(slov)
# print(slov.get(2))

# задачи
# 1
# my_list = [int(i) for i in input().split(' ')]
# print(min(my_list), max(my_list))

# 2
# import math
# a,b,c = [int(i) for i in input().split()]
# d = b**2 - 4 * a * c
# if  d>0:
#    print( (-b - math.sqrt(d)) /( 2*a))
#    print( (-b + math.sqrt(d)) /( 2*a))
# elif d == 0 :
#    print( -b / (2 * a))
# else:
#    print('Корней нет')

# 3
# x = int(input())
# y = int(input())
# max_n= max(x,y)
# count = 1

# if max_n % x == 0  and max % y == 0:
#    print(max_n)
# elif
#    count += 1
#    max_n *= count
# 4

# sp = ['one', 'two', 'one', 'tho', 'three']
# slov ={}
# for el in sp:
#    slov[el] = slov.get(el,0) + 1
#    if slov[el] >1 :
#       print( el, slov[el])
#    else: continue
# slovar = {}
# slovar['hello'] = 'hi'
# slovar['goodbye'] = 'bye'
# slovar['list'] = 'array'
# slovo = 'goodbye'
# for key, value in slovar.items():
#    if slovo == key :
#       print(value)
#    else:
#       print(key)


# print(slovar)
# print(list(slovar.keys()))
# print(slovar.items())
from math import pi

d =  len(input("Введите число для заданной точности числа Пи:\n").split('.')[1] ) -1

print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')







