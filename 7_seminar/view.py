def greeting():
    print('Hello im calculator!\nSelect: \n1 - calculate;\n2 - converter;')
    select = int(input())
    return select


def get_math_example():
    example = input("Введи выражение :")
    return example


def view_result(result):
    print("Мое решение :",  result)


def get_massa():
    mass = float(input("Введите массу в киллограмах :"))
    return mass


def view_result_mass(result):
    print("перевод из кг в граммы: ", result, "грамм")
