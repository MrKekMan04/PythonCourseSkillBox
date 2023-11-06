import re

PHONE_NUMBER_PATTERN = re.compile(r"\b[8|9]\d{9}\b")


def is_number_valid(phone_number: str) -> bool:
    return re.match(PHONE_NUMBER_PATTERN, phone_number) is not None


NUMBERS = ['9999999999', '999999-999', '99999x9999', "99999999999", "999999999F", "8999999999", "F9999999999"]

for i, number in enumerate(NUMBERS):
    print(f"{i} номер: {'всё в порядке' if is_number_valid(number) else 'не подходит'}")
