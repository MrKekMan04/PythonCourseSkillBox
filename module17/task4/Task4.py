from collections import Counter

message = "Today is a beautiful day! The sun is shining and the birds are singing."


def count_unique_characters(string: str) -> int:
    return sum(1 for i in Counter(string).values() if i == 1)


unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
