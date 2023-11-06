import functools
import time
from typing import Callable, Any


class LoggerDecorator:
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs) -> Any:
        print(f"Вызов функции {self.func.__name__}\n"
              f"Аргументы: {args}, {kwargs}")
        time_start = time.time()
        func_result = self.func(*args, **kwargs)

        print(f"Результат: {func_result}\n"
              f"Время выполнения: {time.time() - time_start} секунд")

        return func_result


@LoggerDecorator
def complex_algorithm(arg1, arg2) -> Any:
    algorithm_result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                algorithm_result += i + j
    return algorithm_result


result = complex_algorithm(10, 50)
