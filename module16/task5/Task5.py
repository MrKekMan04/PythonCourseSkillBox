from typing import Callable, Any


def singleton(cls: Callable) -> Callable:
    def wrapper() -> Any:
        if singleton.instance is None:
            singleton.instance = cls

        return singleton.instance

    singleton.instance = None

    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
