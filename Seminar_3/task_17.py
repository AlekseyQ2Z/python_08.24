input_string = input("Введите список чисел через запятую: ")
number_list = list(map(int, input_string.split(',')))
unique_numbers = []
for number in number_list:
    if number not in unique_numbers:
        unique_numbers.append(number)
unique_count = len(unique_numbers)
print(f"Количество уникальных чисел: {unique_count}")