lists_count = int(input("Введите количество списков в списке: "))
list_elements_count = int(input("Введите количество элементов во вложенном списке: "))

result = [
    [(list_index + 1) + lists_count * element_in_list_index for element_in_list_index in range(list_elements_count)]
    for list_index in range(lists_count)
]

print(result)
