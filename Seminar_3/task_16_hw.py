size = int(input("Введите размер массива: "))
new_list = []
count = 0
while size != 0: 
    temp = int(input(f"Введите чило: "))
    new_list.append(temp)
    size -= 1
number = int(input("Введите искомое число: "))
for i in range(len(new_list)):
    if number == new_list[i]:
        count += 1
print(count)