
lst = list(map(int, input("Введите числа через пробел:\n").split()))

def sum_odd_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")
sum_odd_index(lst)
