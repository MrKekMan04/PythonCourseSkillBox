FIRST_RUSSIAN_CHAR = 1040
LAST_RUSSIAN_CHAR = 1103

message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))

new_message = [
    chr(FIRST_RUSSIAN_CHAR + ((ord(i) - FIRST_RUSSIAN_CHAR + offset) % (LAST_RUSSIAN_CHAR - FIRST_RUSSIAN_CHAR + 1)))
    for i in message
]

print("".join(new_message))
