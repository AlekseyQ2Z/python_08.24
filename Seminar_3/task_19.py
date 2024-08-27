list_number = [1, 2, 3, 4, 5]
shift = 3
shift = shift % len(list_number)
for i in range(shift):
    first_element = list_number[0]
    for j in range(len(list_number) - 1):
        list_number[j] = list_number[j + 1]
    list_number[-1] = first_element
print(list_number)
