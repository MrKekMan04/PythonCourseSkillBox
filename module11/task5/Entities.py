import random


class Home:
    def __init__(self) -> None:
        self.fridge_fullness = 50
        self.money = 0

    def waste_food(self, amount: int) -> int:
        amount = min(self.fridge_fullness, amount)
        self.fridge_fullness -= amount
        return amount

    def waste_money(self, amount: int) -> int:
        amount = min(self.money, amount)
        self.money -= amount
        return amount

    def put_money(self, amount: int) -> None:
        self.money += amount

    def put_food(self, amount: int) -> None:
        self.fridge_fullness += amount

    def get_food_amount(self) -> int:
        return self.fridge_fullness

    def get_money(self) -> int:
        return self.money


class Human:
    def __init__(self, name: str, home: Home) -> None:
        self.name = name
        self.satiety = 50
        self.home = home

    def eat(self) -> None:
        self.satiety += self.home.waste_food(40) * 2

    def work(self) -> None:
        self.home.put_money(50)
        self.satiety -= 20

    def play(self) -> None:
        self.satiety -= 10

    def buy_food(self):
        self.home.put_food(self.home.waste_money(30) * 4)

    def is_dead(self) -> bool:
        return self.satiety <= 0

    def live(self) -> None:
        choice = random.randint(1, 7)
        if self.satiety < 20:
            self.eat()
        elif self.home.get_food_amount() < 10:
            self.buy_food()
        elif self.home.get_money() < 50 or choice == 1:
            self.work()
        elif choice == 2:
            self.eat()
        else:
            self.play()
