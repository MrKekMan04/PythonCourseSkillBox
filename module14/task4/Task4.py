import functools
import random
from typing import Dict, Callable, Any

CALLS: Dict[Callable, int] = dict()


def counter(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if func in CALLS:
            CALLS[func] += 1
        else:
            CALLS[func] = 1
        print(f"Функция {func.__name__} вызывается {CALLS[func]} раз!")
        return func(*args, **kwargs)

    return wrapper


@counter
def first_func() -> None:
    print("Called first func!")


@counter
def second_func() -> None:
    print("Called second func!")


for f in [first_func, second_func]:
    for i in range(random.randint(1, 20)):
        f()

print(CALLS)
