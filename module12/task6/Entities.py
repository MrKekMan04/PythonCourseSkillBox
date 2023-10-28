import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_square(self) -> float:
        ...


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def calculate_square(self) -> float:
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, height: float, width: float) -> None:
        self.height = height
        self.width = width

    def calculate_square(self) -> float:
        return self.height * self.width


class Triangle(Shape):
    def __init__(self, side: float, height: float) -> None:
        self.side = side
        self.height = height

    def calculate_square(self) -> float:
        return 1 / 2 * self.side * self.height
