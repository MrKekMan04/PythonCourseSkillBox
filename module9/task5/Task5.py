import collections

less_english_char = 65
greater_english_char = 122

with open("text.txt", "r", encoding="UTF-8") as file:
    clean_string = "".join([
        char.lower() for char in file.read() if less_english_char <= ord(char) <= greater_english_char
    ])

clean_string_data = collections.Counter(clean_string)
characters_data = sorted([(clean_string_data[letter], letter)
                          for letter in clean_string_data.keys()], key=lambda t: (-t[0], t[1]))
total_english_chars = sum(i[0] for i in characters_data)
line_break = "\n"

with open("analysis.txt", "w", encoding="UTF-8") as file:
    file.write(f"{line_break.join([f'{i[1]} {round(i[0] / total_english_chars, 3)}' for i in characters_data])}")
