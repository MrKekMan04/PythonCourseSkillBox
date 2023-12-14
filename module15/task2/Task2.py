from MyMath import MyMath


class Program:
    @staticmethod
    def main():
        res_1 = MyMath.circle_len(radius=5)
        res_2 = MyMath.circle_sq(radius=6)
        print(res_1)
        print(res_2)


if __name__ == '__main__':
    Program.main()
