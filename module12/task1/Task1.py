from Entities import *


class Program:
    @staticmethod
    def main():
        entities = [Apartment, Car, CountryHouse]
        money = float(input("Введите количество денег: "))
        tax_sum = 0

        for i, entity in enumerate(["квартир", "машин", "дач"]):
            for j in range(int(input(f"Введите количество {entity}: "))):
                tax_sum += entities[i](int(input(f"fВведите стоимость {j}: "))).calculateTax()

        delta = abs(money - tax_sum)
        print(f"{'После уплаты налогов у вас останется' if money >= tax_sum else 'На уплату налогов вам не хватит'}"
              f" {delta} денег")


if __name__ == '__main__':
    Program.main()
