def compress_string(string: str) -> str:
    result = ""
    last_char = None
    chars_count = 0

    for char in string:
        if char != last_char:
            if last_char is not None:
                result += f"{last_char}{chars_count}"
            last_char = char
            chars_count = 0
        chars_count += 1

    if chars_count > 0:
        return result + f"{last_char}{chars_count}"


print(f"Закодированная строка: {compress_string(input('Введите строку: '))}.")
