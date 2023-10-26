class Element:
    def __init__(self, elements_combination: dict = None):
        self.elements_combination = elements_combination

    def __add__(self, other):
        class_not_instance = self.elements_combination.get(type(other))
        return None if class_not_instance is None else class_not_instance()


class Water(Element):
    def __init__(self):
        super().__init__({
            Air: Storm,
            Fire: Steam,
            Ground: Dirt,
            Dirt: Nature
        })


class Air(Element):
    def __init__(self):
        super().__init__({
            Fire: Lighting,
            Ground: Dust,
            Water: Storm
        })


class Fire(Element):
    def __init__(self):
        super().__init__({
            Ground: Lava,
            Water: Steam
        })


class Ground(Element):
    def __init__(self):
        super().__init__({
            Fire: Lava,
            Air: Dust,
            Water: Dirt
        })


class Storm(Element):
    pass


class Steam(Element):
    pass


class Dirt(Element):
    def __init__(self):
        super().__init__({
            Water: Nature
        })


class Lighting(Element):
    pass


class Dust(Element):
    pass


class Lava(Element):
    pass


class Nature(Element):
    pass
