def count_uppercase_lowercase(text: str) -> (int, int):
    upper, lower = 0, 0

    for i in text:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return upper, lower


text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)

print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
