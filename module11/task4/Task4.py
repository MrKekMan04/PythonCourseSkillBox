from Elements import *


class Program:
    @staticmethod
    def main():
        water = Water()
        ground = Ground()

        dirt = water + ground
        print(dirt)

        nature = dirt + water
        print(nature)

        none = water + Steam()
        print(none)


if __name__ == '__main__':
    Program.main()
