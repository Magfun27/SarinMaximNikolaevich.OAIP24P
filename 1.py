text = "Привет, мир!"
file = open("test.txt", "w", encoding="utf-8")
file.write(text)
file.close()
print("Файл создан!")


file = open("test.txt", "r", encoding="utf-8")
content = file.read()
file.close()
print("Содержимое файла:", content)


with open("test.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("Прочитано:", content)