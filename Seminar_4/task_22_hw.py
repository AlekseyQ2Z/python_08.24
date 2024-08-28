size_array_1 = int(input("Введите размер первого множества: "))
size_array_2 = int(input("Введите размер второго множества: "))
array_1 = set()
for i in range(size_array_1):
    array_1.add(int(input(f"Введите {i + 1} элемент первого множества: ")))
array_2 = set()
for i in range(size_array_2):
    array_2.add(int(input(f"Введите {i + 1} элемент второго множества: ")))
sort_list = list(sorted(array_1 & array_2))
print(sort_list)
