import math


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    if number == 2:
        return True

    for i in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def crypto(sequence: iter) -> iter:
    return [item for i, item in enumerate(sequence) if is_prime(i)]


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))
