# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

# pytest -v tests\test_32.py


def is_in_mass(num_lst: list[int],
               min_num: int,
               max_num: int) -> list[int]:
    """Возвращает список индексов элементов списка, которые
    находятся в диапазоне [min_num,max_num] """
    list_2 = list()
    for i in range(len(num_lst)):
        if max_num >= num_lst[i] >= min_num:
            list_2.append(i)
    return list_2


# list_1 = list(map(int, input("Введите список чисел через пробел: ").split()))
# min_num_1 = int(input("Введите минимальное число: "))
# max_num_1 = int(input("Введите максимальное число: "))
# print(is_in_mass(list_1, min_num_1, max_num_1))
