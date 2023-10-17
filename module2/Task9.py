def get_id(numbers: list) -> str:
    result = []
    for i in range(len(numbers) - 1, -1, -1):
        if type(numbers[i]) is int and numbers[i] % 2 == 0:
            result.append(str(numbers[i]))
    return "".join(result)


experiments_results = [1, 2, 3, 4]

print(get_id(experiments_results))
