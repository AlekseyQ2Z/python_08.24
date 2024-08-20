number = int(input("Введите трехзначное число: "))
if number < 100 or number > 999:
    print(f"Число {number} не рехзначное")
else:
    print(f"Сумма цифр числа {number} равна {number % 10 + number // 10 % 10 + number // 100 % 10}")