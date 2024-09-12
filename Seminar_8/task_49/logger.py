from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные \n\n"
                    f" 1 Вариант: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f" 2 Вариант: \n"
                    f"{name};{surname};{phone};{address}\n"
                    f"Выберите вариант: "))
    while var != 1 and var != 2:
        print("Неравильный ввод")
        var = int(input(f"В каком формате записать данные \n\n"
                        f" 1 Вариант: \n"
                        f"{name}\n{surname}\n{phone}\n{address}\n\n"
                        f" 2 Вариант: \n"
                        f"{name};{surname};{phone};{address}\n"
                        f"Выберите вариант: "))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
    print("Вывожу данные из 1 файла: \n")
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == "\n" or i == len(data_first) - 1:
                data_first_list.append("".join(data_first[j:i+1]))
                j = i
        print("".join(data_first_list))
    print("Вывожу данные из 2 файла: \n")
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)


def edit_data():
    file_choice = int(input("Выберите файл для редактирования (1 или 2): "))
    if file_choice == 1:
        file_name = 'data_first_variant.csv'
    elif file_choice == 2:
        file_name = 'data_second_variant.csv'
    else:
        print("Неверный выбор")
        return

    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()

    print("Текущие данные:")
    print("".join(data))

    search_term = input("Введите имя или фамилию для поиска записи: ").strip()
    found = False
    for index, line in enumerate(data):
        if search_term in line:
            print(f"Запись найдена: {line}")
            found = True
            new_name = name_data()
            new_surname = surname_data()
            new_phone = phone_data()
            new_address = address_data()

            if file_choice == 1:
                data[index:index+4] = [f"{new_name}\n",
                                       f"{new_surname}\n", f"{new_phone}\n", f"{new_address}\n"]
            elif file_choice == 2:
                data[index] = f"{new_name};{new_surname};{new_phone};{new_address}\n"

            break

    if not found:
        print("Запись не найдена.")
        return

    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(data)

    print("Данные успешно обновлены.")


def delete_data():
    file_choice = int(input("Выберите файл для удаления записи (1 или 2): "))
    if file_choice == 1:
        file_name = 'data_first_variant.csv'
    elif file_choice == 2:
        file_name = 'data_second_variant.csv'
    else:
        print("Неверный выбор")
        return

    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()

    print("Текущие данные:")
    print("".join(data))

    search_term = input("Введите имя или фамилию для удаления записи: ").strip()
    found = False
    for index, line in enumerate(data):
        if search_term in line:
            print(f"Запись найдена: {line}")
            found = True
            if file_choice == 1:
                del data[index:index+5]
            elif file_choice == 2:
                del data[index]
            break

    if not found:
        print("Запись не найдена.")
        return

    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(data)

    print("Запись успешно удалена.")
