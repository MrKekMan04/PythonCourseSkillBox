passed = []

with open("first_tour.txt", "r", encoding="UTF-8") as first_tour_file:
    points_needed = int(first_tour_file.readline())

    for line in first_tour_file.readlines():
        surname, name, points = line.rstrip().split()
        points = int(points)

        if points > points_needed:
            passed.append((points, surname, name))

passed = tuple(reversed(sorted(passed)))

with open("second_tour.txt", "w", encoding="UTF-8") as second_tour_file:
    line_break = "\n"
    second_tour_file.write(
        f"{len(passed)}{line_break}"
        f"{line_break.join([f'{i + 1}) {passed[i][2][0]}. {passed[i][1]} {passed[i][0]}' for i in range(len(passed))])}"
    )
