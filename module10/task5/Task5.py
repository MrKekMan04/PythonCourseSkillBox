import math


def calculate_sqrt(user_input: str) -> float:
    try:
        user_input = float(user_input)
    except ValueError:
        raise ValueError("Введено НЕ число")

    if user_input < 0:
        raise ValueError("Введено ОТРИЦАТЕЛЬНОЕ число!")
    return math.sqrt(user_input)


try:
    answer = calculate_sqrt(input("Введите число: "))
except Exception as e:
    print(e)
else:
    print(f"Ответ: {answer}")
