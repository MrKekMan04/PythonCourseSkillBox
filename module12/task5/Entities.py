class TaskManager:
    def __init__(self) -> None:
        self.tasks = PriorityQueue()

    def new_task(self, name: str, priority: int) -> None:
        self.tasks.put(priority, name)

    def delete_task(self, task: tuple[str, int]) -> None:
        self.tasks.remove(task[1], task[0])

    def __str__(self) -> str:
        return str(self.tasks)


class PriorityQueue:
    def __init__(self) -> None:
        self.items: list[tuple[str, int]] = []

    def put(self, priority, item) -> None:
        self.items.append((priority, item))
        self.__sort()

    def remove(self, priority, item) -> None:
        self.items.remove((priority, item))
        self.__sort()

    def __sort(self) -> None:
        self.items.sort(key=lambda task: (task[0], task[1]))

    def __str__(self) -> str:
        return str(self.items)
