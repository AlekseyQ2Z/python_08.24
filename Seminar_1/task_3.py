import math
n = int()
for i in range(3):
    n = math.ceil(n + int(input(f"Введите количество учащихся в {i + 1} классе: ")) / 2)
print(f'Необходимо {n} парт(ы)')
