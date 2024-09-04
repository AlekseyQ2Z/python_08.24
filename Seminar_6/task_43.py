list1 = list()
for i in range(int(input("Введите размер массива: "))):
    list1.append(int(input(f"Введите {i+1} элемент массива: ")))
temp = 0
for i in range(0, len(list1) - 1):
    for j in range(i + 1, len(list1)):
        if i != j and list1[i] == list1[j]:
            temp += 1
print(f"В данном массиве {temp} пар(ы)")
