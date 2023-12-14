from MyCollection import MyDict


class Program:
    @staticmethod
    def main():
        my_dict = MyDict()

        print(my_dict.get("key"))


if __name__ == '__main__':
    Program.main()
