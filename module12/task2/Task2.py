import os.path
import random

from CustomException import *


class Program:

    @staticmethod
    def main():
        karma_destination = 500
        karma = 0

        if os.path.exists("karma.log"):
            os.remove("karma.log")

        while karma < karma_destination:
            try:
                karma += Program.one_day()
            except CustomException as e:
                with open("karma.log", "a", encoding="UTF-8") as file:
                    file.write(e.get_cause() + "\n")

    @staticmethod
    def one_day():
        if random.randint(0, 10) == 1:
            exceptions = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
            raise random.choice(exceptions)()
        return random.randint(1, 8)


if __name__ == '__main__':
    Program.main()
