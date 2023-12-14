from typing import Any
from collections import deque


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self._cache = dict()
        self.__capacity = capacity
        self.__used = deque(maxlen=capacity)
        self.__count = 0

    def print_cache(self) -> None:
        print(self._cache)

    def get(self, key: Any) -> Any:
        if key in self._cache:
            self.__used.remove(key)
            self.__used.append(key)
            return self._cache.get(key)

    @property
    def cache(self) -> Any:
        while (last_key := self.__used.popleft()) is None or last_key not in self._cache:
            pass
        return last_key

    @cache.setter
    def cache(self, new_elem: tuple[Any, Any]) -> None:
        self.__count += 1
        if self.__count > self.__capacity:
            key_to_remove = self.cache
            if key_to_remove is not None:
                del self._cache[key_to_remove]
        self._cache[new_elem[0]] = new_elem[1]
        self.__used.appendleft(new_elem[0])
