import bisect

containers_count = int(input("Количество контейнеров: "))

containers = list(reversed([int(input("Количество контейнеров: ")) for _ in range(containers_count)]))
index = bisect.bisect_left(containers, int(input("Введите вес нового контейнера: ")))

print(f"Номер, который получит новый контейнер: {len(containers) - index + 1}")
