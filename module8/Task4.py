from collections.abc import Iterable


def my_sum(*args: Iterable) -> int:
    total_sum = 0

    for item in args:
        total_sum += my_sum(*item) if isinstance(item, Iterable) else item
    return total_sum


print(my_sum([[1, 2, [3]], [1], 3], (1, 2, 3)))
