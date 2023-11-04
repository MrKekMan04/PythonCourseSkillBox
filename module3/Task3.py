shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

optimized_shop = {}

for i in shop:
    if i[0] in optimized_shop:
        optimized_shop[i[0]].append(i[1])
    else:
        optimized_shop[i[0]] = [i[1]]

gear = input("Название детали: ")

if gear in optimized_shop:
    print(f"Количество деталей: {len(optimized_shop[gear])}\nОбщая стоимость: {sum(optimized_shop[gear])}")
else:
    print("Количество деталей: 0\nОбщая стоимость: 0")
