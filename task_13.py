days = int(input("Введите количество двей от 1 до 100: "))
thaw = 0
max_thaw = 0
if 1 < days < 100:
    while days > 0:
        temperature = int(input("Введите температуру: "))
        if temperature > 0:
            thaw += 1
            if thaw > max_thaw:
                max_thaw = thaw
        elif temperature < 0:
            thaw = 0
        days -= 1
else:
    print(f"Ошибка. Число {days} меньше 1 или больше 100")
print(f"Самая длинная оттепель {max_thaw} дней")