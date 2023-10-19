longest_word = max(input("Введите строку: ").split(" "), key=lambda word: len(word))

print(f"Самое длинное слово: «{longest_word}».\nДлина этого слова: {len(longest_word)} символ.")
