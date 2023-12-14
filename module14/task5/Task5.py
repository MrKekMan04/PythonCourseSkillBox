import functools
from typing import Callable, Any, Dict

HASH: Dict[Callable, Dict[Any, Any]] = dict()


def hashed(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        func_hash = {}
        if func in HASH:
            func_hash = HASH[func]
            if args in func_hash:
                return HASH[func][args]
        result = func(*args, **kwargs)
        func_hash[args] = result
        HASH[func] = func_hash
        return result

    return wrapper


@hashed
def fibonacci(n: int) -> int:
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(200))
