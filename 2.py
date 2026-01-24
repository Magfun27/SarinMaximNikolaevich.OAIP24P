def save_idea():
    idea = input("Введите свою идею: ")

    with open("ideas.txt", "a", encoding="utf-8") as file:
        file.write(idea + "\n")
    print("Идея сохранена!")


def read_ideas():
    try:
        with open("ideas.txt", "r", encoding="utf-8") as file:
            ideas = file.read()

        if ideas:
            print("\n=== ВАШИ ИДЕИ ===")
            print(ideas)
        else:
            print("У вас пока нет идей")

    except FileNotFoundError:
        print("Файл с идеями еще не создан")


def clear_ideas():
    with open("ideas.txt", "w", encoding="utf-8") as file:
        file.write("")
    print("Все идеи удалены")


def main():
    while True:
        print("\n=== ПРОСТОЙ ДНЕВНИК ИДЕЙ ===")
        print("1. Добавить идею")
        print("2. Посмотреть все идеи")
        print("3. Очистить дневник")
        print("4. Выход")

        choice = input("Выберите действие (1-4): ")

        if choice == "1":
            save_idea()
        elif choice == "2":
            read_ideas()
        elif choice == "3":
            clear_ideas()
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Пожалуйста, введите число от 1 до 4")


if __name__ == "__main__":
    main()