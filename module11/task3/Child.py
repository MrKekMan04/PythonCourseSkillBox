from Human import Human


class Child(Human):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)

        self.calm_state = False
        self.hungry_state = False

    def calm_down(self) -> None:
        self.calm_state = False

    def eat(self) -> None:
        self.hungry_state = False

    def is_calm(self) -> bool:
        return self.calm_state

    def is_hungry(self) -> bool:
        return self.hungry_state
