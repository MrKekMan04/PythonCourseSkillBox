from collections.abc import Iterable


def invert(sequence: Iterable) -> list:
    result = []

    for i in sequence:
        if isinstance(i, Iterable):
            result += invert(i)
        else:
            result.append(i)
    return result


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(invert(nice_list))
