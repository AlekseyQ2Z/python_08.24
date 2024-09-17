import json
from datetime import datetime

FILE_NAME = "notes.json"

def load_notes():
    """Загружает заметки из файла."""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_notes(notes):
    """Сохраняет заметки в файл."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=4)

def get_next_id(notes):
    """Возвращает следующий ID для новой заметки."""
    if notes:
        return max(note["id"] for note in notes) + 1
    else:
        return 1

def add_note():
    """Добавляет новую заметку."""
    notes = load_notes()
    note_id = get_next_id(notes)
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")  # Измененный формат даты

    new_note = {
        "id": note_id,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }

    notes.append(new_note)
    save_notes(notes)
    print("Заметка успешно добавлена!")

def edit_note():
    """Редактирует существующую заметку."""
    notes = load_notes()
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            note["title"] = input(f"Текущий заголовок: {note['title']}. Введите новый заголовок: ")
            note["body"] = input(f"Текущий текст: {note['body']}. Введите новый текст: ")
            note["timestamp"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")  # Измененный формат даты
            save_notes(notes)
            print("Заметка успешно обновлена!")
            return
    print("Заметка с таким ID не найдена.")

def delete_note():
    """Удаляет заметку по ID."""
    notes = load_notes()
    note_id = int(input("Введите ID заметки для удаления: "))
    notes = [note for note in notes if note["id"] != note_id]
    save_notes(notes)
    print("Заметка удалена.")

def show_notes():
    """Показывает все заметки."""
    notes = load_notes()
    if not notes:
        print("Заметок пока нет.")
    else:
        for note in notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата: {note['timestamp']}")

def show_note_by_id():
    """Выводит заметку по ID."""
    notes = load_notes()
    note_id = int(input("Введите ID заметки: "))
    for note in notes:
        if note["id"] == note_id:
            print(f"Заголовок: {note['title']}\nТекст: {note['body']}\nДата: {note['timestamp']}")
            return
    print("Заметка с таким ID не найдена.")

def show_notes_by_date():
    """Показывает заметки за определенную дату."""
    notes = load_notes()
    date = input("Введите дату в формате DD-MM-YYYY: ")
    filtered_notes = [note for note in notes if note["timestamp"].startswith(date)]
    if not filtered_notes:
        print("Заметок на эту дату не найдено.")
    else:
        for note in filtered_notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата: {note['timestamp']}")