import functools
import time
from typing import Callable, Any


def wait_for_calling(seconds: float) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            time.sleep(seconds)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@wait_for_calling(seconds=2)
def do_something():
    print("doing...")


do_something()
