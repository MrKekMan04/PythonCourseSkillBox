special_simbols = {"@", "№", "$", "%", "^", "&", "*", "(", ")"}

file_name = input("Название файла: ")

if file_name[0] in special_simbols:
    print("Ошибка: название начинается недопустимым символом")
elif file_name.endswith(".txt") or file_name.endswith(".docx"):
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx")
else:
    print("Файл назван верно.")
