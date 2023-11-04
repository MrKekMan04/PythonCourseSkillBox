def print_num(num: int) -> None:
    if num > 1:
        print_num(num - 1)
    print(num)


print_num(int(input("Введите num: ")))
