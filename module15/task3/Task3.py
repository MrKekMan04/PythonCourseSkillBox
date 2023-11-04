from Date import Date


class Program:
    @staticmethod
    def main():
        d = Date.from_string("12-11-1920")
        print(d)


if __name__ == '__main__':
    Program.main()
