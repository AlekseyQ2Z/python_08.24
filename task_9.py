number = int(input("Введите целое число: "))
n = 1
while number != 0:
    n *= number
    number -= 1
print(f"Его факториал равен {n}")