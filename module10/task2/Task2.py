import random
import os

total_sum = 0
has_error = False

output_file_path = os.path.join("out_file.txt")

if os.path.exists(output_file_path):
    os.remove(output_file_path)

try:
    while total_sum < 777:
        user_number = int(input("Введите число: "))

        if random.randint(0, 13) == 6:
            raise RuntimeError

        total_sum += user_number

        with open(output_file_path, "a", encoding="UTF-8") as file:
            file.write(str(user_number) + "\n")
except RuntimeError:
    has_error = True
    print("Вас постигла неудача!")
else:
    print("Вы успешно выполнили условие для выхода из порочного цикла!")
