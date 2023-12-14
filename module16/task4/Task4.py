import functools
from typing import Callable, Any


def decorator_with_args_for_any_decorator(func: Callable) -> Callable:
    @functools.wraps(func)
    def decorator(*args, **kwargs) -> Any:
        print(f"Переданные арги и кварги в декоратор: {args} {kwargs}")
        return func

    return decorator


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        return func(*args, **kwargs)

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
