quantity = int(input("Введите количество монеток лежащих на столе: "))
eagle = 0
tails = 0
for i in range(quantity):
    side = int(input("Введите сторону монеты, 1 это решка, 0 это орёл: "))
    if side == 0:
        eagle += 1
    elif side == 1:
        tails += 1
    else:
        print("Ошибка, введена неверная сторона")
        i += 1
if eagle > tails:
    print(f"Надо перевернуть {tails} решки")
elif eagle < tails:
    print(f"Надо перевернуть {eagle} орла")
else:
    print(f"Надо перевернуть {eagle} орла или решки")