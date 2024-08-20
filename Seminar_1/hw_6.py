number = int(input("Введите номер билета: "))
first_pass = number // 1000
second_pass = number % 1000
if first_pass % 10 + first_pass // 10 % 10 + first_pass // 100 % 10 == second_pass % 10 + second_pass // 10 % 10 + second_pass // 100 % 10:
    print(f"Билет {number} счастливый")
else:
    print(f"Билет {number} не счастливый")
