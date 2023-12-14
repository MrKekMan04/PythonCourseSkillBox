from Entities import *


class Program:
    @staticmethod
    def main():
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)

        print([i.get_item() for i in linked_list])
        print(linked_list.get(0).get_item())
        print(linked_list.get(1).get_item())
        print(linked_list.get(2).get_item())
        linked_list.remove(0)
        print([i.get_item() for i in linked_list])
        linked_list.remove(1)

        print(linked_list.get(0).get_item())
        print([i.get_item() for i in linked_list])


if __name__ == '__main__':
    Program.main()
