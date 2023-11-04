def get_offset_string(string: str, offset: int) -> str:
    return "".join(["".join(string[offset:]), "".join(string[:offset])])


first_string = input("Первая строка: ")
second_string = input("Вторая строка: ")

for i in range(len(first_string)):
    if get_offset_string(first_string, i) == second_string:
        print(f"Первая строка получается из второй со сдвигом {i}")
        break
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига")
