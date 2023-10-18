vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}

user_input = input("Введите текст: ")
vowels_in_input = [letter for letter in user_input if letter in vowels]

print(f"Список гласных букв: {vowels_in_input}\nДлина списка: {len(vowels_in_input)}")
