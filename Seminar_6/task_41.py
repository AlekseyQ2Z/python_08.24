list1 = list()
for i in range(int(input("Введите количество элементов в массиве: "))):
    list1.append(int(input(f"Введите {i+1} элемент массива: ")))
temp = 0
for i in range(1, len(list1) - 1):
    if list1[i+1] < list1[i] > list1[i-1]:
        temp += 1
print(
    f"Количество элементов у которых два соседних элемента меньше этого элемента: {temp}")
