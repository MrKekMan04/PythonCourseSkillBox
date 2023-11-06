from collections import Counter


def can_be_poly(string: str) -> bool:
    return 1 >= sum(1 for i in Counter(string).values() if i % 2 == 1)


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
