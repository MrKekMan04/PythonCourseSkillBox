films = {"Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов", "Мементо",
         "Отступники", "Деревня"}

favourites_films = set()
favourites_count = int(input("Сколько фильмов хотите добавить? "))

for i in range(favourites_count):
    film = input("Введите название фильма: ")

    if film in films:
        if film in favourites_films:
            print("Фильм уже добавлен в избранные!")
        else:
            favourites_films.add(film)
    else:
        print(f"Ошибка: фильма {film} у нас нет :(")

print(f"Ваш список любимых фильмов: {', '.join(favourites_films)}")
