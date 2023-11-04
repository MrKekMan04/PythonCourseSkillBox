import datetime
import functools
from typing import Callable, Any


def logging(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            print(f"{func.__name__}\n{func.__doc__}")
            return func(*args, **kwargs)
        except Exception as e:
            with open("function_errors.log", "a", encoding="UTF-8") as log:
                log.write(f"[{datetime.datetime.now()}] - [ERROR] - {func.__name__} : {e}\n")

    return wrapper


@logging
def func_without_exceptions() -> None:
    """ Some doc of func_without_exceptions """
    print("Without exceptions...")


@logging
def func_with_exception() -> None:
    """ Some doc of func_with_exception """
    print("Throw exception...")
    raise Exception("Something doing wrong!")


@logging
def func_with_exception_two() -> None:
    """ Some doc of func_with_exception_two """
    print("Throw exception...")
    raise Exception("Something doing wrong 2!")


for f in [func_without_exceptions, func_with_exception, func_with_exception_two]:
    f()
