from Entities import *


class Program:
    @staticmethod
    def main():
        try:
            Shape()
        except TypeError:
            print("passed")

        print(Circle(2).calculate_square())
        print(Rectangle(2, 4).calculate_square())
        print(Triangle(2, 2).calculate_square())


if __name__ == '__main__':
    Program.main()
