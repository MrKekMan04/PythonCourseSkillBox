n = int(input("Введите число N: "))


class IterClass:
    def __init__(self, stop_n: int) -> None:
        self.__n = stop_n
        self.__current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current < self.__n:
            self.__current += 1
            return self.__current ** 2
        else:
            raise StopIteration


def iter_fun(stop_n: int) -> iter:
    for i in range(1, stop_n + 1):
        yield i ** 2


iter_class = IterClass(n)
iter_expression = [i ** 2 for i in range(1, n + 1)]
iter_f = [i for i in iter_fun(n)]
iter_c = [i for i in iter_class]

print(f"{iter_expression}\n{iter_f}\n{iter_c}")
