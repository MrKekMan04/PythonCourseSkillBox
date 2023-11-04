default_list = [1, 2, 3, 4, 5]

offset = int(input("Сдвиг: "))

print(f"Изначальный список: {default_list}")
print(f"Сдвинутый список: {[default_list[i % len(default_list)] for i in range(-offset, len(default_list) - offset)]}")
