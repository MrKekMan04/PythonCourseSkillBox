from Entities import TaskManager


class Program:
    @staticmethod
    def main():
        manager = TaskManager()

        manager.new_task("сделать уборку", 4)
        manager.new_task("помыть посуду", 4)
        manager.new_task("отдохнуть", 1)
        manager.new_task("поесть", 2)
        manager.new_task("сдать ДЗ", 2)

        print(str(manager))

        manager.delete_task(("поесть", 2))
        print(manager)


if __name__ == '__main__':
    Program.main()
