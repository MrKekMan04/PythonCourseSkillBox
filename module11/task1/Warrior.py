class Warrior:
    def __init__(self) -> None:
        self.health = 100
        self.power = 20

    def take_damage(self, amount: int) -> None:
        self.health -= amount

    def is_dead(self) -> bool:
        return self.health <= 0

    def get_power(self) -> int:
        return self.power

    def get_health(self) -> int:
        return self.health
