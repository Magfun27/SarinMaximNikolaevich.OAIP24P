import sqlite3

NAME = "students.db"


def init_db():
    conn = sqlite3.connect(NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id         INTEGER PRIMARY KEY,
            name       TEXT    NOT NULL,
            group_name TEXT    NOT NULL,
            grade      INTEGER NOT NULL
        )
    """)

    cursor.execute("PRAGMA table_info(students)")
    columns = [col[1] for col in cursor.fetchall()]
    if "age" not in columns:
        cursor.execute("ALTER TABLE students ADD COLUMN age INTEGER DEFAULT 0")

    conn.commit()
    conn.close()



def get_connection():
    return sqlite3.connect(NAME)


def print_students(rows):
    if not rows:
        print("Записи не найдены.")
        return
    print(f"{'ID':<4} {'ФИО':<22} {'Группа':<10} {'Оценка':<6} {'Возраст'}")
    for r in rows:
        print(f"{r[0]:<4} {r[1]:<22} {r[2]:<10} {r[3]:<6} {r[4]}")


def seed_data():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM students")
    if cursor.fetchone()[0] == 0:
        data = [
            ("Иванов Иван",      "ИСП-126", 5, 19),
            ("Петров Пётр",      "ИСП-126", 4, 20),
            ("Сидоров Алексей",  "ИСП-225", 3, 18),
            ("Смирнова Анна",    "ИСП-225", 5, 19),
            ("Кузнецов Максим",  "ИСП-126", 4, 21),
        ]
        cursor.executemany(
            "INSERT INTO students (name, group_name, grade, age) VALUES (?, ?, ?, ?)",
            data,
        )
        conn.commit()
        print("Начальные данные (5 студентов) загружены.")
    conn.close()


def show_all():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print_students(rows)
    conn.close()


def add_student():
    name = input("ФИО студента: ").strip()
    group = input("Группа: ").strip()
    try:
        grade = int(input("Оценка (2-5): ").strip())
        age = int(input("Возраст: ").strip())
    except ValueError:
        print("Ошибка: оценка и возраст должны быть числами.")
        return

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, group_name, grade, age) VALUES (?, ?, ?, ?)",
        (name, group, grade, age),
    )
    conn.commit()
    print(f"Студент «{name}» добавлен (ID={cursor.lastrowid}).")
    conn.close()


def search_by_group():
    group = input("Введите название группы: ").strip()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE group_name = ?", (group,))
    print_students(cursor.fetchall())
    conn.close()


def search_by_grade():
    try:
        grade = int(input("Введите оценку: ").strip())
    except ValueError:
        print("Ошибка: введите число.")
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE grade = ?", (grade,))
    print_students(cursor.fetchall())
    conn.close()


def update_grade():
    try:
        student_id = int(input("ID студента: ").strip())
        new_grade = int(input("Новая оценка (2-5): ").strip())
    except ValueError:
        print("Ошибка: введите число.")
        return

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET grade = ? WHERE id = ?", (new_grade, student_id)
    )
    conn.commit()
    if cursor.rowcount:
        print(f"Оценка студента ID={student_id} изменена на {new_grade}.")
    else:
        print(f"Студент с ID={student_id} не найден.")
    conn.close()


def delete_student():
    try:
        student_id = int(input("ID студента для удаления: ").strip())
    except ValueError:
        print("Ошибка: введите число.")
        return

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    if cursor.rowcount:
        print(f"Студент ID={student_id} удалён.")
    else:
        print(f"Студент с ID={student_id} не найден.")

    print("\nОставшиеся студенты:")
    cursor.execute("SELECT * FROM students")
    print_students(cursor.fetchall())
    conn.close()


def avg_grade():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(grade) FROM students")
    avg = cursor.fetchone()[0]
    if avg is not None:
        print(f"Средняя оценка: {avg:.2f}")
    else:
        print("В таблице нет студентов.")
    conn.close()


def count_by_group():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT group_name, COUNT(*) FROM students GROUP BY group_name"
    )
    rows = cursor.fetchall()
    if rows:
        print("Группа      Кол-во")
        for g, c in rows:
            print(f"{g:<12}{c}")
    else:
        print("В таблице нет студентов.")
    conn.close()


def top_student():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM students ORDER BY grade DESC, age ASC LIMIT 1"
    )
    row = cursor.fetchone()
    if row:
        print(f"Лучший студент: {row[1]} (группа {row[2]}, "
              f"оценка {row[3]}, возраст {row[4]})")
    else:
        print("В таблице нет студентов.")
    conn.close()


def older_than():
    try:
        age = int(input("Введите возраст: ").strip())
    except ValueError:
        print("Ошибка: введите число.")
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE age > ?", (age,))
    print_students(cursor.fetchall())
    conn.close()


def main():
    init_db()
    seed_data()

    menu = """
===== УЧЁТ СТУДЕНТОВ =====
1. Показать всех студентов
2. Добавить студента
3. Найти студентов по группе
4. Найти студентов по оценке
5. Изменить оценку
6. Удалить студента
--- Дополнительно ---
7. Средняя оценка всех студентов
8. Кол-во студентов в каждой группе
9. Студент с самой высокой оценкой
10. Студенты старше указанного возраста
0. Выход
"""

    while True:
        print(menu)
        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            show_all()
        elif choice == "2":
            add_student()
        elif choice == "3":
            search_by_group()
        elif choice == "4":
            search_by_grade()
        elif choice == "5":
            update_grade()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            avg_grade()
        elif choice == "8":
            count_by_group()
        elif choice == "9":
            top_student()
        elif choice == "10":
            older_than()
        elif choice == "0":
            break
        else:
            print("Неверный пункт меню, попробуйте снова.")


if __name__ == "__main__":
    main()