class LinkedList:
    def __init__(self) -> None:
        self.__count = 0
        self.__head: Node = None
        self.__current_iter_item = self.__head
        self.__tail: Node = self.__head

    def append(self, item):
        node = Node(item)
        if self.__head is None:
            self.__head = node
            self.__tail = self.__head
        self.__tail.set_next(node)
        self.__tail = node
        self.__count += 1

    def get(self, index: int):
        if index >= self.__count or index < 0:
            raise IndexError

        current_node = self.__head
        current_index = 0
        while current_index < index:
            current_node = current_node.get_next()
            current_index += 1
        return current_node

    def remove(self, index: int):
        if index >= self.__count or index < 0:
            raise IndexError

        current_node = None
        current_index = 0
        while current_index <= index - 1:
            current_node = current_node.get_next() if current_node is not None else self.__head
            current_index += 1
        delete_item: Node = current_node.get_next() if current_node is not None else self.__head
        if current_node is not None:
            current_node.set_next(delete_item.get_next() if delete_item is not None else None)
        if delete_item is self.__head:
            self.__head = delete_item.get_next() if delete_item is not None else None
        self.__count -= 1
        return current_node

    def __iter__(self):
        self.__current_iter_item = self.__head
        return self

    def __next__(self):
        if self.__current_iter_item is None:
            raise StopIteration
        else:
            returned = self.__current_iter_item
            self.__current_iter_item = self.__current_iter_item.get_next()
            return returned


class Node:
    def __init__(self, item) -> None:
        self.__item = item
        self.__next = None

    def set_next(self, node) -> None:
        self.__next = node

    def get_next(self):
        return self.__next

    def get_item(self):
        return self.__item
