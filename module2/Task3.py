video_cards_count = int(input("Количество видеокарт: "))
video_cards = []
max_series = float("-inf")

for i in range(video_cards_count):
    video_card = int(input(f"Видеокарта {i + 1}: "))
    video_cards.append(video_card)
    max_series = max(max_series, video_card)

print(f"Старый список видеокарт: {video_cards}")
print(f"Новый список видеокарт: {[video_card for video_card in video_cards if video_card != max_series]}")
