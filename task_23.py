new_list = [0, -1, 5, 2, 3]
temp = int()
for i in range(1, len(new_list)):
    if new_list[i] > new_list[i - 1]:
        temp += 1
print(temp)