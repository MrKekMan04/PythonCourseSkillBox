def is_ip_correct(ip: str) -> (bool, str):
    digits = ip.split('.')

    if len(digits) != 4:
        return False, "Адрес — это четыре числа, разделённые точками"
    for digit in digits:
        if not digit.isdigit() or type(int(digit)) is not int:
            return False, f"{digit} — это не целое число"
        digit = int(digit)
        if digit > 255:
            return False, f"{digit} превышает 255"
        elif digit < 0:
            return False, f"{digit} меньше 0"
    return True, "IP-адрес корректен"


is_correct, cause = is_ip_correct(input("Введите IP: "))

print(cause)
