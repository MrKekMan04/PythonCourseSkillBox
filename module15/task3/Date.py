from typing import Type, Any, TypeVar

import re


class NoPublicConstructor(type):
    def __call__(cls, *args, **kwargs):
        raise TypeError(
            f"{cls.__module__}.{cls.__qualname__} has no public constructor"
        )

    def _create(cls: Type[TypeVar], *args: Any, **kwargs: Any) -> TypeVar:
        return super().__call__(*args, **kwargs)


class Date(metaclass=NoPublicConstructor):
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls: 'Date', date: str) -> 'Date':
        if cls.is_date_valid(date):
            return cls._create(*date.split("-"))

    @classmethod
    def is_date_valid(cls: 'Date', date: str) -> bool:
        """
        Not a complicated check.
        It is better to use the built-in modules
        """
        m = re.match(r"(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{4})", date)
        return 1 <= int(m.group("day")) <= 31 and 1 <= int(m.group("month")) <= 12 and 0 <= int(m.group("year"))

    def __str__(self) -> str:
        return f"{self.day}-{self.month}-{self.year}"
