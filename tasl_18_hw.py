size = int(input("Введите размер массива: "))
new_list = []
min_diff = 999
min_diff_number = 0
while size != 0: 
    temp = int(input(f"Введите чило: "))
    new_list.append(temp)
    size -= 1
number = int(input("Введите искомое число: "))
for i in range(len(new_list)):
    diff = abs(number - new_list[i])
    if diff < min_diff:
        min_diff_number = new_list[i]
        min_diff = diff
print(min_diff_number)