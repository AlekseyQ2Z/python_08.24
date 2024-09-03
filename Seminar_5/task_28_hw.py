def summ(n, m):
    if m == 0:
        return n
    else:
        return summ(n + 1, m - 1)
num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
print(summ(num_1, num_2))