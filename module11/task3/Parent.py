from Human import Human
from Child import Child


class Parent(Human):
    def __init__(self, name: str, age: int, children: set[Child]) -> None:
        super().__init__(name, age)

        self.children = children

    def feed_child(self, child: Child) -> bool:
        if child in self.children and child.is_hungry():
            child.eat()
            return True
        else:
            return False

    def calm_child(self, child: Child) -> bool:
        if child in self.children and child.is_calm():
            child.calm_down()
            return True
        else:
            return False

    def are_children_valid(self) -> bool:
        return all([self.get_age() - child.get_age() >= 16 for child in self.children])

    def get_info(self) -> str:
        return f"My name {self.get_name()}, I'm {self.get_age()}. I have {len(self.children)} children: {self.children}"
