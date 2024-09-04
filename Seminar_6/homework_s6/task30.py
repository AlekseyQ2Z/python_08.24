# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

# pytest -v tests\test_30.py

def arithmetic_progression(first: int,
                           diff: int,
                           quantity: int) -> list[int]:
    """Возвращает список арифметической прогрессии по заданным:
    1) первый элемент
    2) разность
    3) количество элементов"""
    list_1 = list()
    if quantity == 0:
        return list_1
    else:
        list_1.append(first)
        for i in range(quantity - 1):
            list_1.append(list_1[i] + diff)
        return list_1


# first_1 = int(input("Введите первый элемент прогрессии: "))
# diff_1 = int(input("Введите разность элементов в прогрессии: "))
# quantity_1 = int(input("Введите количество элементов в прогрессии: "))
# print(arithmetic_progression(first_1, diff_1, quantity_1))
