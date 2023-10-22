from collections import Counter

with open("registrations.txt", "r", encoding="UTF-8") as file:
    registrations = [i.rstrip() for i in file.readlines()]

bad_registrations = []
good_registrations = []


def validate_registration(registration: str) -> None:
    if len(registration.split()) != 3:
        raise IndexError
    name, mail, age = registration.split()

    for letter in name:
        if not letter.isalpha():
            raise NameError

    mail_data = Counter(mail)

    if ("@" not in mail_data or mail_data["@"] != 1) or ("." not in mail_data or mail_data["."] != 1):
        raise SyntaxError

    age = int(age)
    if 10 > age or age > 99:
        raise ValueError


for reg in registrations:
    try:
        validate_registration(reg)
    except IndexError:
        bad_registrations.append(f"{reg}\tНЕ присутствуют все три поля")
    except NameError:
        bad_registrations.append(f"{reg}\tПоле «Имя» содержит НЕ только буквы")
    except SyntaxError:
        bad_registrations.append(f"{reg}\tПоле «Имейл» НЕ содержит @ и точку")
    except ValueError:
        bad_registrations.append(f"{reg}\tПоле «Возраст» НЕ представляет число от 10 до 99")
    else:
        good_registrations.append(reg)

with open("registrations_bad.log", "w", encoding="UTF-8") as file:
    file.write("\n".join(bad_registrations))

with open("registrations_good.log", "w", encoding="UTF-8") as file:
    file.write("\n".join(good_registrations))
