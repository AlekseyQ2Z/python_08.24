length = int(input("Введите длинну шоколадки в дольках: "))
width = int(input("Введите ширину шоколадки в дольках: "))
broken = int(input("Введите сколько долек Вы хотите отломить: "))
if (broken % length == 0 or broken % width == 0) and broken < length * width:
    print(f"YES, {broken} долек можно отломить одним разломом")
else:
    print(f"NO, {broken} долек нельзя отломить одним разломом")