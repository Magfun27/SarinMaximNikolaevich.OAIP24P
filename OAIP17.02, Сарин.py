import json

file_name = "projects.json"

def load_data():
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def show_projects(projects):
    if not projects:
        print("\nНет проектов.")
        return
    print("\nСписок проектов:")
    for i, project in enumerate(projects, start=1):
        print(f"{i}. {project['name']} (Статус: {project['status']})")

def create_project(projects):
    name = input("Введите название проекта: ").strip()
    if not name:
        print("Название не может быть пустым.")
        return
    new_project = {
        "name": name,
        "status": "планирование",
        "tasks": []
    }
    projects.append(new_project)
    save_data(projects)
    print(f"Проект '{name}' создан со статусом 'планирование'.")

def add_task(projects):
    if not projects:
        print("Сначала создайте проект.")
        return
    show_projects(projects)
    try:
        choice = int(input("Выберите номер проекта: ")) - 1
        if choice < 0 or choice >= len(projects):
            print("Неверный номер.")
            return
    except ValueError:
        print("Введите число.")
        return
    task_text = input("Введите описание задачи: ").strip()
    if not task_text:
        print("Задача не может быть пустой.")
        return
    projects[choice]["tasks"].append(task_text)
    save_data(projects)
    print("Задача добавлена.")

def show_tasks(projects):
    if not projects:
        print("Нет проектов.")
        return
    show_projects(projects)
    try:
        choice = int(input("Выберите номер проекта: ")) - 1
        if choice < 0 or choice >= len(projects):
            print("Неверный номер.")
            return
    except ValueError:
        print("Введите число.")
        return
    tasks = projects[choice]["tasks"]
    if not tasks:
        print("В этом проекте пока нет задач.")
    else:
        print(f"\nЗадачи проекта '{projects[choice]['name']}':")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def change_status(projects):
    if not projects:
        print("Нет проектов.")
        return
    show_projects(projects)
    try:
        choice = int(input("Выберите номер проекта: ")) - 1
        if choice < 0 or choice >= len(projects):
            print("Неверный номер.")
            return
    except ValueError:
        print("Введите число.")
        return
    print("Доступные статусы: планирование, в работе, готов")
    new_status = input("Введите новый статус: ").strip().lower()
    if new_status not in ["планирование", "в работе", "готов"]:
        print("Некорректный статус. Используйте: планирование, в работе, готов")
        return
    projects[choice]["status"] = new_status
    save_data(projects)
    print(f"Статус проекта изменён на '{new_status}'.")

def main():
    projects = load_data()
    while True:
        print("\n Менеджер проектов и задач ")
        print("1. Показать проекты")
        print("2. Создать проект")
        print("3. Добавить задачу")
        print("4. Показать задачи в проекте")
        print("5. Изменить статус проекта")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            show_projects(projects)
        elif choice == "2":
            create_project(projects)
        elif choice == "3":
            add_task(projects)
        elif choice == "4":
            show_tasks(projects)
        elif choice == "5":
            change_status(projects)
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()
