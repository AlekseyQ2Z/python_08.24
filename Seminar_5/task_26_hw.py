def power(n, m):
    if m == 0:
        return 1
    elif m == 1:
        return n
    else:
        return n * power(n, m - 1)

num = int(input("Введите число: "))
pow = int(input("Введите степень: "))
print(power(num, pow))