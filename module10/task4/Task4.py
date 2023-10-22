import os

CHAT_PATH = os.path.join("chat.txt")


def get_chat_history() -> str:
    if os.path.exists(CHAT_PATH):
        with open(CHAT_PATH, "r", encoding="UTF-8") as chat:
            return chat.read()
    return ""


def write_message(message: str) -> None:
    with open(CHAT_PATH, "a", encoding="UTF-8") as chat:
        chat.write(f"{message}\n")


name = input("Введите ваше имя: ")

while True:
    do = input("Выберите действие:\n1. Посмотреть текущий текст чата.\n2. Отправить сообщение.\nДействие: ")

    if do == "1":
        print(get_chat_history())
    elif do == "2":
        write_message(f"{name}:\t{input('Введите сообщение: ')}")
    else:
        print("Не удалось распознать команду.")
