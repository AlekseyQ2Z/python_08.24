list1 = list()
for i in range(int(input("Введите размер первого массива: "))):
    list1.append(int(input(f"Введите {i+1} элемент первого массива: ")))
list2 = list()
for i in range(int(input("Введите размер второго массива: "))):
    list2.append(int(input(f"Введите {i+1} элемент второго массива: ")))
print()
list3 = ["Вот элементы первого массива, которых нет во втором массиве:"]
count = 0
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            count += 1
    if count == 0:
        list3.append(str(list1[i]))
    count = 0
print(" ".join(list3))
