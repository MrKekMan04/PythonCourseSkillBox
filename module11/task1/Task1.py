import random
from Warrior import Warrior


class Program:
    @staticmethod
    def main():
        first_warrior = Warrior()
        second_warrior = Warrior()

        while not first_warrior.is_dead() and not second_warrior.is_dead():
            match random.randint(0, 2):
                case 0:
                    second_warrior.take_damage(first_warrior.get_power())
                    print(f"Атаковал первый юнит. У второго юнита осталось {second_warrior.get_health()} здоровья")
                case 1:
                    first_warrior.take_damage(second_warrior.get_power())
                    print(f"Атаковал второй юнит. У первого юнита осталось {first_warrior.get_health()} здоровья")

        print(f"Одержал победу {'первый' if second_warrior.is_dead() else 'второй'} юнит")


if __name__ == '__main__':
    Program.main()
