import random

origin = [random.randint(-100, 100) for _ in range(10)]

print(f"Оригинальный список: {origin}\n"
      f"Новый список: {[(origin[i], origin[i + 1]) for i in range(0, len(origin), 2)]}")
