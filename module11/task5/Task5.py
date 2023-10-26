from Entities import *


class Program:
    @staticmethod
    def main():
        home = Home()
        human2 = Human("Mary", home)
        human1 = Human("Peter", home)
        day = 0
        while (not human1.is_dead() or not human2.is_dead()) and day < 365:
            human1.live()
            human2.live()
            day += 1
            print(day)


if __name__ == '__main__':
    Program.main()
