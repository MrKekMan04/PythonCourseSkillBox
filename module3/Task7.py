humans = [i + 1 for i in range(int(input("Количество человек: ")))]
offset = int(input("Какое число в считалке? "))
index = 0

while len(humans) > 1:
    print(f"\nТекущий круг людей: {humans}\n"
          f"Начало счёта с номера {humans[index]}")
    retired_index = (index + offset - 1) % len(humans)
    print(f"Выбывает человек под номером {humans[retired_index]}")
    humans.remove(humans[retired_index])
    index = retired_index % len(humans)

print(f"\nОстался человек под номером {humans[0]}")
