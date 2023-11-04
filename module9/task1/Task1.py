import re


with open("numbers.txt", "r", encoding="UTF-8") as numbers_file:
    with open("answer.txt", "w", encoding="UTF-8") as answer_file:
        answer_file.write(str(sum(map(int, filter(None, re.split(r"[\n ]", numbers_file.read()))))))
