from logger import add_note, edit_note, delete_note, show_notes, show_note_by_id, show_notes_by_date

def interface():
    """Интерфейс приложения заметок."""
    while True:
        print("\nМеню заметок:")
        print("1. Добавить заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Показать все заметки")
        print("5. Показать заметку по ID")
        print("6. Показать заметки по дате")
        print("7. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            edit_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            show_notes()
        elif choice == "5":
            show_note_by_id()
        elif choice == "6":
            show_notes_by_date()
        elif choice == "7":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте еще раз.")