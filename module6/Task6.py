data = {}

for i in range(int(input("Введите количество заказов: "))):
    surname, pizza, quantity = input(f"{i + 1} заказ: ").split(" ")

    if surname in data:
        if pizza in data[surname]:
            data[surname][pizza] += int(quantity)
        else:
            data[surname][pizza] = int(quantity)
    else:
        data[surname] = {pizza: int(quantity)}

line_break = "\n"

print(line_break.join([
    f"{surname}:{line_break}{line_break.join([f'{pizza}: {str(data[surname][pizza])}'
                                              for pizza in data[surname].keys()])}"
    for surname in data.keys()
]))
