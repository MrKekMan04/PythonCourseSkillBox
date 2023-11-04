def is_palindrome(numbers: list, start_index: int) -> bool:
    for i in range((len(numbers) - start_index) // 2):
        if numbers[start_index + i] != numbers[-(i + 1)]:
            return False
    return True


sequence = [int(input("Число: ")) for _ in range(int(input("Количество чисел: ")))]

for i in range(len(sequence)):
    if is_palindrome(sequence, i):
        print(f"Нужно приписать чисел: {i}\n"
              f"Сами числа: {sequence[i - 1::-1]}")
        break
