first_list = [1, 5, 3]
second_list = [1, 5, 1, 5]
third_list = [1, 3, 1, 5, 3, 3]

first_merge_list = first_list + second_list
fives_count = first_merge_list.count(5)

second_merge_list = [i for i in first_merge_list if i != 5] + third_list
threes_count = second_merge_list.count(3)

print(f"Количество цифр 5 при первом объединении: {fives_count}")
print(f"Количество цифр 3 при втором объединении: {threes_count}")
print(f"Итоговый список: {second_merge_list}")
