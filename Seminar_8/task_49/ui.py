from logger import input_data, print_data, edit_data, delete_data


def interface():
    while True:
        action = input("Выберите действие: \n1 - добавить данные\n2 - вывести данные\n3 - изменить данные\n4 - удалить данные\n5 - выйти: \n")
        if action == '1':
            input_data()
        elif action == '2':
            print_data()
        elif action == '3':
            edit_data()
        elif action == '4':
            delete_data()
        elif action == '5':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
