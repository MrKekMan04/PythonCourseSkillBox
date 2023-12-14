from abc import ABC, abstractmethod


class Property(ABC):
    def __init__(self, worth: float) -> None:
        self.worth = worth

    @abstractmethod
    def calculateTax(self):
        ...


class Apartment(Property):
    def __init__(self, worth: float) -> None:
        super().__init__(worth)

    def calculateTax(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth: float) -> None:
        super().__init__(worth)

    def calculateTax(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth: float) -> None:
        super().__init__(worth)

    def calculateTax(self):
        return self.worth / 500
