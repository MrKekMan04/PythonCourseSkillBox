import collections

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

dict_1 = collections.Counter(array_1)
dict_2 = collections.Counter(array_2)
dict_3 = collections.Counter(array_3)

set_1 = set(array_1)
set_2 = set(array_2)
set_3 = set(array_3)

print(f"Задача 1:\n"
      f"Решение без множеств: {[key for key in dict_1.keys() if key in dict_2 and key in dict_3]}\n"
      f"Решение с множествами: {set_1.intersection(set_2).intersection(set_3)}")

print(f"Задача 2:\n"
      f"Решение без множеств: {[key for key in dict_1.keys() if key not in dict_2 and key not in dict_3]}\n"
      f"Решение с множествами: {set_1.difference(set_2).difference(set_3)}")
