def is_password_correct(password: str) -> bool:
    has_capitalize_letter = False
    numbers_count = 0

    for i in password:
        if has_capitalize_letter and numbers_count >= 3:
            break
        if i.isupper():
            has_capitalize_letter = True
        elif i.isdigit():
            numbers_count += 1

    return len(password) >= 8 and has_capitalize_letter and numbers_count >= 3


while not is_password_correct(input("Придумайте пароль: ")):
    print("Пароль ненадёжный. Попробуйте ещё раз.")

print("Это надёжный пароль.")
