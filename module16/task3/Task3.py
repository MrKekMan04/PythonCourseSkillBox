import datetime
import functools
from typing import Callable, Any


def log(func: Callable, format_str: str) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Запускается `{func.__name__}`. Дата и время запуска: {datetime.datetime.now().strftime(format_str)}")

        return func(*args, **kwargs)

    return wrapper


def log_methods(format_str: str) -> Callable:
    def decorate(cls) -> Any:
        for method_name in dir(cls):
            if not method_name.startswith("__"):
                setattr(cls, method_name, log(getattr(cls, method_name), format_str))
        return cls

    return decorate


@log_methods("%b %d %Y — %H:%M:%S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("%b %d %Y - %H:%M:%S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
