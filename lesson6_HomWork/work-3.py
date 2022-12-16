# вывести нечетные числа и возвести в квадрат
# 1 вариант
sp = [i**2 for i in range(1,31) if not i%2]
print(sp)
# 2 вариант через фильтр
sp1 = [i**2 for i in range(1,31)]
res1= list(filter(lambda x: x%2==0, sp))
print(res1)
# Вывести числа которые меньше 300
res = list(filter(lambda x: x < 300, sp))
print(res)

