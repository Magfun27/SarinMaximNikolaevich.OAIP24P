import json

data_1 = [
{
    "Book_ID": 1,
    "Title": "Преступление и наказание",
    "Author": "Фёдор Достоевский",
    "Publication_Date": "1866",
    "ISBN": "978-5-699-75632-1"
},
{
    "Book_ID": 2,
    "Title": "Война и мир",
    "Author": "Лев Толстой",
    "Publication_Date": "1869",
    "ISBN": "978-5-17-079256-6"
},
{
    "Book_ID": 3,
    "Title": "Мастер и Маргарита",
    "Author": "Михаил Булгаков",
    "Publication_Date": "1967",
    "ISBN": "978-5-699-81442-4"
}
]
data_2 = [{
    "Book_ID": 1,
    "Title": "Преступление и наказание",
    "Author": "Фёдор Достоевский",
    "Publication_Date": "1866",
    "ISBN": "978-5-699-75632-1"
},
{
    "Book_ID": 2,
    "Title": "Война и мир",
    "Author": "Лев Толстой",
    "Publication_Date": "1869",
    "ISBN": "978-5-17-079256-6"
},
{
    "Book_ID": 3,
    "Title": "Мастер и Маргарита",
    "Author": "Михаил Булгаков",
    "Publication_Date": "1967",
    "ISBN": "978-5-699-81442-4"
}]
data_3 = [{
    "Loan_ID": 1,
    "Book_ID": 1,
    "Reader_ID": 1,
    "Issue_Date":"2023-04-01",
    "Return_Date": "2023-04-30"
},
{
    "Loan_ID": 2,
    "Book_ID": 2,
    "Reader_ID": 2,
    "Issue_Date": "2023-04-15",
    "Return_Date": "2023-05-15"
},
{
    "Loan_ID": 3,
    "Book_ID": 3,
    "Reader_ID": 3,
    "Issue_Date": "2023-04-20",
    "Return_Date": "2023-05-20"
}]

with open("books.json", "w", encoding="utf-8") as file:
    json.dump(data_1, file, ensure_ascii=False, indent=2)

with open("readers.json", "w", encoding="utf-8") as file:
    json.dump(data_1, file, ensure_ascii=False, indent=2)

with open("loans.json", "w", encoding="utf-8") as file:
    json.dump(data_1, file, ensure_ascii=False, indent=2)


with open("books.json", "r", encoding="utf-8") as file:
    books = json.load(file)

print("\nБаза данных книг:\n")
for book in books:
    print(f"Book_ID: {book['Book_ID']}\nTitle: {book['Title']}\nAuthor: {book['Author']}\nPublication Date: {book['Publication_Date']}\nISBN: {book['ISBN']}\n")

with open("readers.json", "r", encoding="utf-8") as file:
    readers = json.load(file)

for reader in readers:
    print(f"  ID читателя: {reader['Reader_ID']}")
    print(f"  ФИО: {reader['Last_Name']} {reader['First_Name']} {reader['Middle_Name']}")
    print(f"  Дата рождения: {reader['Birth_Date']}")
    print(f"  Адрес: {reader['Address']}")
    print(f"  Телефон: {reader['Phone']}")
    print(f"  Дата регистрации: {reader['Registration_Date']}")