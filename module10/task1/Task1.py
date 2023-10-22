with open("people.txt", "r", encoding="UTF-8") as file:
    names = [i.rstrip() for i in file.readlines()]

total_len = 0

for i in range(len(names)):
    try:
        total_len += len(names[i])
        if len(names[i]) < 3:
            raise RuntimeWarning
    except RuntimeWarning:
        print(f"Ошибка: менее трёх символов в строке {i + 1}.")

print(f"Общее количество символов: {total_len}.")
