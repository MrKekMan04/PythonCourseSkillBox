def quick_sort(sequence: list) -> list:
    if len(sequence) == 0:
        return []
    reference_element = sequence[-1]
    left = []
    mid = []
    right = []

    for i in range(len(sequence)):
        if sequence[i] < reference_element:
            left.append(sequence[i])
        elif sequence[i] == reference_element:
            mid.append(sequence[i])
        else:
            right.append(sequence[i])

    return quick_sort(left) + mid + quick_sort(right)


print(quick_sort([5, 8, 9, 4, 2, 9, 1, 8]))
