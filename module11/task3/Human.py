class Human:
    def __init__(self, name: str, age: int) -> None:
        self.age = age
        self.name = name

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age
