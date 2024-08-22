from math import sqrt

sum_number = int(input("Введите сумму чисел: "))
multiply_number = int(input("Введите произведение чисел: "))
discriminant = sum_number * sum_number - 4 * multiply_number
if discriminant < 0:
    print("Ошибка ввода")
else:
    sqrt_discriminant = int(sqrt(discriminant))
    number_1 = (sum_number + sqrt_discriminant) // 2
    number_2 = sum_number - number_1
    print(f"Петя задумал числа {number_1} и {number_2}")
