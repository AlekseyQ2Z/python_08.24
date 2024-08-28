string_input = input("Введите буквы через пробел: ").split()
res = {}
for i in string_input:
    if i in res:
        print(f"{i}_{res[i]}", end=' ')
    else:
        print(i, end=' ')
    res[i] = res.get(i, 0) + 1
    