def get_data(data_count: int, message: str) -> dict:
    data = {}

    for i in range(data_count):
        key = int(input(message.format(i + 1)))

        if key in data:
            data[key] += 1
        else:
            data[key] = 1
    return data


rollers_count = int(input("Количество роликов: "))
rollers = get_data(rollers_count, "Размер пары {0}: ")

humans_count = int(input("Количество людей: "))
humans = get_data(humans_count, "Размер ноги человека {0}: ")

humans_with_rollers_count = 0

for human_size in humans.keys():
    if human_size in rollers:
        humans_with_rollers_count += min(humans[human_size], rollers[human_size])

print(f"Наибольшее количество людей, которые могут взять ролики: {humans_with_rollers_count}")
